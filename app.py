from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib
import uvicorn

# Load the pre-trained model pipeline
model = joblib.load("model_pipeline.pkl")

# Initialize FastAPI
app = FastAPI(
    title="Cricket Win Predictor API",
    description="API to predict if team1 wins against team2 based on match context.",
    version="1.0"
)

# Define the input schema using Pydantic
class PredictionInput(BaseModel):
    team1: str
    team2: str
    season: int = 2023           # Default to the latest season
    city: str = "NeutralCity"    # Default neutral city
    venue: str = "NeutralVenue"  # Default neutral venue
    toss_winner: str = None      # If not provided, we'll assume team1 wins the toss
    toss_decision: str = None    # If not provided, we'll assume 'bat'
    dl_applied: int = 0          # Default to 0 (not applied)

@app.post("/predict")
def predict(input: PredictionInput):
    try:
        toss_winner = input.toss_winner if input.toss_winner else input.team1
        toss_decision = input.toss_decision if input.toss_decision else "bat"

        data = pd.DataFrame({
            "season": [input.season],
            "city": [input.city],
            "team1": [input.team1],
            "team2": [input.team2],
            "toss_winner": [toss_winner],
            "toss_decision": [toss_decision],
            "venue": [input.venue],
            "dl_applied": [input.dl_applied]
        })

        prediction = model.predict(data)[0]
        prediction_prob = model.predict_proba(data)[0, 1]
        
        result = {
            "team1": input.team1,
            "team2": input.team2,
            "prediction": int(prediction),
            "win_probability": float(prediction_prob)
        }
        return result
    except Exception as e:
        print("Error during prediction:", e)
        raise e

# To run the API, execute this file directly.
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
