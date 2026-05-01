from logger import logging
import pandas as pd

try:
    df=pd.read_csv("data\loan_data.csv")
    logging.info("data frame succesfully loaded")
except Exception:
    logging.info("data not loaded")
 