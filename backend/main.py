
from fastapi import FastAPI,Request,Depends,BackgroundTasks
from fastapi.security import OAuth2PasswordBearer
from upstash_redis import Redis
import joblib
from backend.logger import logging
from backend.modules.hashed import check_password,create_hashed_password
from backend.modules.send_email import send_otp
from backend.modules.token import create_token,decode_token
from pydantic import BaseModel,EmailStr,Field
import pandas as pd
import os
from dotenv import load_dotenv
from pymongo import MongoClient

client=MongoClient(os.getenv("mongodb"))
load_dotenv()
outh2=OAuth2PasswordBearer(tokenUrl="token")

redis_ = Redis(url=os.getenv("redis_url"),token=os.getenv("redis_token"))
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

class login(BaseModel):
    email:EmailStr
    password:str=Field(...,min_length=6)

class register(BaseModel):
    name:str
    email:EmailStr
    password:str=Field(...,min_length=6)
    



async def send_email_for_otp(email:str):
    otp=await send_otp(email)
    if otp:
        redis_.setex(f"{email}:otp",300,otp)
    else:
        redis_.setex(f"{email}:otp",300,None)


@app.post("/token")
async def user_token(request:Request):
    data=await request.json()
    token=create_token(data)
    return {"token":token,"access_type":"bearer"}


@app.post("/send_code")
async def verification_otp(email:EmailStr,background_task:BackgroundTasks):
    background_task.add_task(send_email_for_otp,email)

@app.post("/verification")
def check(otp:str,email:EmailStr):
    sended_otp=redis_.get(f"{email}:otp")
    if sended_otp==otp:
        return {"Verification":"Succesfull"}
    else:
        return{"Verification":"otp mismatch "}


@app.get("/")
async def home_page():
    return{"message":"loaded succesfully"}

@app.post("/user_login")
def user_login_(user:login):
    db=client["user_db"]
    collections=db["all_users"]
    k=collections.find_one({"email":user.email})
    if not k:
        return {"login":False}
    else:
        if(check_password(user.password,k.get("password"))):
            return {"login":True,"name":k.get("name"),"email":k.get("email")}
        else:
            return {"login":False,"error":"password didnt match"}
        
@app.post("/user_register")
async def user_register_(user:register):
    new_hash_pw=create_hashed_password(user.password)
    db=client["user_db"]
    collection=db["all_users"]
    exist=collection.find_one({"email":user.email})
    if exist:
        return {"user_details":"True"}
    collection.insert_one({"name":user.name,"email":user.email,"password":new_hash_pw})
    return {"user_details":"successfully created"}


@app.post("/predict")
async def predict_data(data: LoanData):
    with open("preprocess.joblib","rb") as f:
        preprocess=joblib.load(f)
    input_dict = data.dict()
    df = pd.DataFrame([input_dict])

    processed = preprocess.transform(df)
    with open("loan_predict.joblib","rb") as f:
        model=joblib.load(f)
    
    # Predict
    prediction = model.predict(processed)
    return {"prediction": int(prediction[0])}
