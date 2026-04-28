import pandas as pd
from logger import logging
from sklearn.preprocessing import OneHotEncoder,OrdinalEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline


try:
    df=pd.read_csv("D:\Loan_aproval\Loan_aproval_model\data\loan_data.csv")
    logging.info("data_loaded succesfully")
except Exception:
    logging.info("data not loaded")

df_0=df[df["loan_status"]==0]
df_1=df[df["loan_status"]==1]
df=pd.concat([df_1,df_0[:len(df_1)]])
df=df.sample(frac=1,random_state=42,ignore_index=True)

x=df[['person_age', 'person_gender', 'person_education', 'person_income', 'person_home_ownership', 'loan_amnt', 'loan_intent','loan_int_rate', 'cb_person_cred_hist_length','credit_score', 'previous_loan_defaults_on_file']].copy()
y=df["loan_status"].copy()

#extract string values
x_str=x.select_dtypes(exclude="number")

#extract numbers
x_int=x.select_dtypes(include="number")

#create column transformers
preprocess=ColumnTransformer(
    transformers=[
        ("onehotenc",OneHotEncoder(),['person_gender', 'person_home_ownership','loan_intent', 'previous_loan_defaults_on_file']),
        ("education",OrdinalEncoder(categories=[['High School', 'Associate', 'Bachelor', 'Master', 'Doctorate']]),["person_education"]),
        ("standard",StandardScaler(),x_int.columns)
    ],
    remainder="passthrough"
)

#transform the data
preprocess.fit(x)
new_x=preprocess.transform(x)
#convert them into new dataframe
new_x=pd.DataFrame(new_x,columns=preprocess.get_feature_names_out())
new_data=pd.concat([new_x,y],axis=1)

#download the dataset
try:
    new_data.to_csv("data/preprocessed.csv")
    logging.info("preprocess data doenload")
except Exception:
    logging.info("exception occur")