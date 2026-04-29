import streamlit as st
import requests

st.title("🚀 AI-Powered Loan Approval System")
st.write(" ")
st.write(""" Welcome to the Loan Approval Prediction Platform — an end-to-end Machine Learning solution designed to automate and enhance credit decision-making.

This system leverages advanced machine learning techniques to evaluate loan applications based on key applicant attributes such as age, income, education, credit history, and financial behavior. By analyzing these factors, the model predicts whether a loan should be approved, enabling faster, more consistent, and data-driven decisions.""")
st.divider()


st.subheader("🔍 What This Project Does")
st.write(""" Our model assesses loan eligibility using the following features:

Personal details: age, gender, education
Financial status: income, home ownership
Loan details: amount, intent, interest rate
Credit profile: credit score, credit history length
Risk indicators: previous loan defaults

The goal is to reduce manual effort, minimize bias, and improve accuracy in loan approval processes. """)
st.divider()


st.subheader("⚙️ Technology Stack")

st.write(""" 

This project follows modern MLOps practices to ensure scalability, reproducibility, and reliability:

Machine Learning for predictive modeling
MLflow (via DagsHub) for experiment tracking and model versioning
DVC (Data Version Control) for dataset and pipeline management
Docker for containerization and deployment consistency
FastAPI / Streamlit  for serving the model through an interactive interface""")

st.divider()
st.subheader("📊 Key Features")
st.write(""" Automated loan approval prediction
Reproducible ML pipeline with version control
Experiment tracking and model comparison
Scalable and portable deployment using Docker
User-friendly interface for real-time predictions""")
st.divider()

st.subheader("🎯 Objective")
st.write("To build a robust, transparent, and production-ready system that helps financial institutions make smarter lending decisions while reducing risk and operational overhead.")