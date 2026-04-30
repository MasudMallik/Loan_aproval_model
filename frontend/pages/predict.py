import streamlit as st
import requests
st.title("Loan Approval Prediction")


if "user" in st.session_state:
     st.subheader(f"User: {st.session_state.user}")
else:
     st.subheader("User: Guest")

age=st.number_input("Enter your age",max_value=70,min_value=18,value=18)
gender=st.radio("gender",["male","female"])
education=st.selectbox("Education: ",['Master', 'Associate', 'High School', 'Bachelor', 'Doctorate'])
income=st.number_input("Enter Income: ",value=1000,min_value=1000,step=500)
home_ownership=st.selectbox("Home Ownership: ",['RENT', 'OWN', 'OTHER', 'MORTGAGE'])
loan_amount=st.number_input("Loan Amount: ",step=1000,value=50000)
loan_intent=st.selectbox("Loan Intent: ",['MEDICAL', 'PERSONAL', 'EDUCATION', 'DEBTCONSOLIDATION', 'VENTURE','HOMEIMPROVEMENT'])
loan_int_rate=st.number_input("Loan Intent Rate: ")
Tenure=st.number_input(" length of applicant’s recorded credit history: ")
credit_sc=st.number_input("Credit Score: ")
prev_lon=st.selectbox("Ever failed to repay the loan",["No","Yes"])

if st.button("Classify",type="primary"):
    data={
        "person_age": age,
    "person_gender":gender,
    "person_education": education,
    "person_income": income,
    "person_home_ownership":home_ownership, 
    "loan_amnt": loan_amount,
    "loan_intent": loan_intent,
    "loan_int_rate": loan_int_rate,
    "cb_person_cred_hist_length":Tenure,
    "credit_score": credit_sc,
    "previous_loan_defaults_on_file":prev_lon,
    }
    with st.status("please wait. model is loading...."):
            response=requests.post("https://loan-aproval-model.onrender.com/predict",json=data)
            if response.status_code==200:
                st.success("Succesfully classify the user")
            else:
                st.error("Please try again some time letter")
              
    if response.status_code==200:
        ans=response.json()
        if ans["prediction"]==1:
            st.success("Application Approved")
        else:
            st.warning("Application Rejected")
        

        if "user" in st.session_state:
            data["Application"]="Approved" if ans["prediction"]==1 else "rejected"
            response=requests.post("https://loan-aproval-model.onrender.com/save_data",json=data,headers={"Authorization": f"Bearer {st.session_state.token["token"]}"})
            if response.status_code==200:
                st.write("data loaded succesfully")
   
st.divider()
st.write("!! For storing the results please login...")
st.divider()
        
