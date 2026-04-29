
from fastapi import FastAPI,Request,Depends
from fastapi.security import OAuth2AuthorizationCodeBearer
import joblib
from backend.logger import logging
from pydantic import BaseModel
import pandas as pd
app = FastAPI(
    version="0.0.1",
    description="This is a loan approval prediction model",
    summary="Predict if user gets loan or not",
    contact={"phone": "916317619X"}
)


class LoanData(BaseModel):
    person_age: float
    person_gender: str
    person_education: str
    person_income: float
    person_home_ownership: str
    loan_amnt: float
    loan_intent: str 
    loan_int_rate: float
    cb_person_cred_hist_length: float
    credit_score: float
    previous_loan_defaults_on_file: str



@app.get("/")
async def home_page():
    return{"message":"loaded succesfully"}

@app.post("/predict")
async def predict_data(data: LoanData):
    with open("preprocess.joblib","rb") as f:
        preprocess=joblib.load(f)
    input_dict = data.dict()
    # Convert dict → DataFrame with one row
    df = pd.DataFrame([input_dict])
    
    # Apply preprocessing
    processed = preprocess.transform(df)
    with open("loan_predict.joblib","rb") as f:
        model=joblib.load(f)
    
    # Predict
    prediction = model.predict(processed)
    return {"prediction": int(prediction[0])}
