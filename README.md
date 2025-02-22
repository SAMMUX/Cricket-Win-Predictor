# Cricket Win Predictor

A FastAPI-based API for predicting cricket match outcomes. This project uses machine learning (with XGBoost and other models) to predict whether Team 1 will win against Team 2 based on match-related features.

## Overview

The **Cricket Win Predictor** is designed to:
- **Predict Match Outcomes:** Given inputs such as teams, season, city, venue, toss details, and more, the API returns a prediction (win/lose) along with a win probability for Team 1.
- **Provide a RESTful API:** Built with [FastAPI](https://fastapi.tiangolo.com/) and served with [Uvicorn](https://www.uvicorn.org/).
- **Be Easy to Deploy:** The project is set up for deployment on platforms like Heroku, Render, or any cloud service that supports Python.

## Features

- **FastAPI & Uvicorn:** High-performance asynchronous API.
- **Machine Learning Prediction:** Uses pre-trained model pipelines (e.g., XGBoost, scikit-learn) to make predictions.
- **Interactive Documentation:** Automatically generated Swagger UI available at `/docs`.
- **Easy Deployment:** Ready for continuous deployment with GitHub and Heroku integration.


## Installation & Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/<your_username>/cric-win-predictor.git
   cd cric-win-predictor
2. **Set Up a Virtual Environment:**
    python3 -m venv venv
    source venv/bin/activate
3. **Install Dependencies:**
    pip install -r requirements.txt
4. **Run the Application Locally:**
    python -m uvicorn app:app --reload

## Usage
### Predicting a Match Outcome
### Request:
Make a POST request to /predict with a JSON payload. For example, using cURL:
curl -X POST "http://127.0.0.1:8000/predict" \
-H "Content-Type: application/json" \
-d '{
  "team1": "India",
  "team2": "Pakistan",
  "season": 2025,
  "city": "Dubai",
  "venue": "Dubai International Stadium",
  "toss_winner": "Pakistan",
  "toss_decision": "bat",
  "dl_applied": 0
}'

### Response:
{
    "team1": "India",
    "team2": "Pakistan",
    "prediction": 1,
    "win_probability": 0.617796778678894
}

## Testing with Postman
Open Postman and create a new POST request to http://127.0.0.1:8000/predict.
Set the Content-Type header to application/json.
Paste your JSON payload in the body and send the request.


