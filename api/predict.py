import json
import pickle
from http.server import BaseHTTPRequestHandler
from pathlib import Path

import pandas as pd

MODEL_PATH = Path(__file__).parent / "model.pkl"

with open(MODEL_PATH, "rb") as f:
    MODEL = pickle.load(f)

FEATURE_ORDER = [
    "Age",
    "Person Income",
    "Employee Experience",
    "Loan Amount",
    "Loan interest Rate",
    "Loan percentage",
    "Credit History",
    "Credit Score",
    "Gender_male",
    "Education_Bachelor",
    "Education_Doctorate",
    "Education_High School",
    "Education_Master",
    "Home Onwership_OTHER",
    "Home Onwership_OWN",
    "Home Onwership_RENT",
    "Loan Intent_EDUCATION",
    "Loan Intent_HOMEIMPROVEMENT",
    "Loan Intent_MEDICAL",
    "Loan Intent_PERSONAL",
    "Loan Intent_VENTURE",
    "Previous Loan_Yes",
]


def build_row(payload: dict) -> pd.DataFrame:
    """Turn friendly form input into the exact one-hot row the model expects."""

    gender = payload.get("gender", "female")
    education = payload.get("education", "Associate")
    home = payload.get("home_ownership", "MORTGAGE")
    intent = payload.get("loan_intent", "DEBTCONSOLIDATION")
    previous_loan = payload.get("previous_loan", "No")

    row = {
        "Age": float(payload.get("age", 0)),
        "Person Income": float(payload.get("income", 0)),
        "Employee Experience": float(payload.get("employment_experience", 0)),
        "Loan Amount": float(payload.get("loan_amount", 0)),
        "Loan interest Rate": float(payload.get("interest_rate", 0)),
        "Loan percentage": float(payload.get("loan_percent_income", 0)),
        "Credit History": float(payload.get("credit_history", 0)),
        "Credit Score": float(payload.get("credit_score", 0)),
        "Gender_male": 1 if gender == "male" else 0,
        "Education_Bachelor": 1 if education == "Bachelor" else 0,
        "Education_Doctorate": 1 if education == "Doctorate" else 0,
        "Education_High School": 1 if education == "High School" else 0,
        "Education_Master": 1 if education == "Master" else 0,
        "Home Onwership_OTHER": 1 if home == "OTHER" else 0,
        "Home Onwership_OWN": 1 if home == "OWN" else 0,
        "Home Onwership_RENT": 1 if home == "RENT" else 0,
        "Loan Intent_EDUCATION": 1 if intent == "EDUCATION" else 0,
        "Loan Intent_HOMEIMPROVEMENT": 1 if intent == "HOMEIMPROVEMENT" else 0,
        "Loan Intent_MEDICAL": 1 if intent == "MEDICAL" else 0,
        "Loan Intent_PERSONAL": 1 if intent == "PERSONAL" else 0,
        "Loan Intent_VENTURE": 1 if intent == "VENTURE" else 0,
        "Previous Loan_Yes": 1 if previous_loan == "Yes" else 0,
    }

    return pd.DataFrame([[row[c] for c in FEATURE_ORDER]], columns=FEATURE_ORDER)


class handler(BaseHTTPRequestHandler):
    def _send(self, status, body):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(body).encode())

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_POST(self):
        try:
            length = int(self.headers.get("Content-Length", 0))
            payload = json.loads(self.rfile.read(length) or b"{}")

            row = build_row(payload)
            proba = MODEL.predict_proba(row)[0]
            prediction = int(MODEL.predict(row)[0])

            self._send(
                200,
                {
                    "prediction": prediction,
                    "approved": prediction == 0,
                    "probability_default": round(float(proba[1]), 4),
                    "probability_repay": round(float(proba[0]), 4),
                },
            )
        except Exception as e:
            self._send(400, {"error": str(e)})
