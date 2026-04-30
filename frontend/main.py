import streamlit as st
import requests


home=st.Page(
    page="pages/home_page.py",
    title="home page",
    icon="🏠",
    default=True,
)
predict=st.Page(
    page="pages/predict.py",
    title="Predict",
    icon="🔮"
)
log_reg=st.Page(
    page="pages/login_reg.py",
    title="Login and Registration",
    icon="🆕"
)

hist=st.Page(
    page="pages/history.py",
    icon="⏮️",
    title="History"
)

pages=st.navigation(
    [home,predict,log_reg,hist]
)

import streamlit as st
import requests

# Sidebar logout button
if st.sidebar.button("Logout"):
    # Call backend logout endpoint
    response = requests.post("http://127.0.0.1:8000/logout")
    if response.status_code == 200:
        st.sidebar.success("Logged out successfully")
    else:
        st.sidebar.error("Logout failed")



pages.run()
# if st.button("click to predict"):
#     response=requests.post("http://127.0.0.1:8000/predict",json={
#         "person_age": 22,
#     "person_gender": "female",
#     "person_education": "Master",
#     "person_income": 71948,
#     "person_home_ownership":"RENT", 
#     "loan_amnt": 35000,
#     "loan_intent": "PERSONAL",
#     "loan_int_rate": 16.02,
#     "cb_person_cred_hist_length": 3,
#     "credit_score": 561,
#     "previous_loan_defaults_on_file": "No",
#     })
# # 22	female	Master	71948	0	RENT	35000	PERSONAL	16.02	0.49	3	561	No	1
    
#     print(response)
#     st.write(response.json())
