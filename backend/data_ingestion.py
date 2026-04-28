from logger import logging
import pandas as pd

try:
    df=pd.read_csv("D:\Loan_aproval\Loan_aproval_model\data\loan_data.csv")
    logging.info("data frame succesfully loaded")
except Exception:
    logging.info("data not loaded")
