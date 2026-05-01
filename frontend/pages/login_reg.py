import streamlit as st
import requests


if "login" not in st.session_state:
    st.session_state.login = True

if "flag" not in st.session_state:
    st.session_state.flag = False 

def login():
        
        st.title("Login")
        email = st.text_input("Enter email", placeholder="email@gmail.com")
        password = st.text_input(
            "Enter password",
            placeholder="At least 1 uppercase, lowercase, special character, and digit",
            type="password"
        )

        col1, col2 = st.columns(2)

        if col1.button("Login", type="primary", use_container_width=True):
            if email and password:
                response = requests.post(
                    "https://loan-aproval-model.onrender.com/user_login",
                    json={"email": email, "password": password}
                )
                if response.status_code == 200:
                    result=response.json()
                    if(result.get("login")==False):
                        st.info("you dont have an account please create it")
                    elif "error" in result:
                         st.error("password didnt match")
                    else:
                        token=requests.post("https://loan-aproval-model.onrender.com/token",
                                             json={
                                                  "name":result.get("name"),"email":result.get("email")
                                             })
                        if token.status_code==200:
                             st.session_state.token=token.json()
                             st.session_state.user=result.get("name")
                             st.switch_page("pages/predict.py")
                else:
                    st.error("Login failed ❌")
            else:
                st.warning("Please enter both email and password")

        if col2.button("New user", type="primary", use_container_width=True):
            st.session_state.login=False
            st.rerun()

def registration():
        
        
        st.title("Registration")
        st.text("Enter your Details : ")
        st.divider()
        
        name=st.text_input(label="Enter your full name: ",placeholder="Abc Def")
        col1, col2 = st.columns(2)
        col2.write(" ")
        col2.write(" ")
        email=col1.text_input(label="Enter your email-Id: ",placeholder="email@gmail.com",)
        if col2.button("Send otp",type="primary",use_container_width=True):
            response=requests.post("https://loan-aproval-model.onrender.com/send_code",params={"email":email})
            if response.status_code==200:
                st.success("otp send in your email")
            else:
                st.error("otp not send please try agin letter")
        otp=col1.text_input("Enter otp",placeholder="Enter 6 digit otp ")
        col2.write(" ")
        col2.write(" ")
        if col2.button("Confirm",type="primary",use_container_width=True):
            response=requests.post("https://loan-aproval-model.onrender.com/verification",params={
                "otp":otp,
                "email":email
            })
            if response.status_code==200:
                answer=response.json()
                if answer.get("Verification")=="Succesfull":
                    st.success("otp verified")
                    st.session_state.flag=True
                else:
                    st.error("otp mismatch")
                    st.session_state.flag=False

        password = st.text_input(
            "Enter password",
            placeholder="6 digit password",
          
        )
        confirm_password = st.text_input(
            "Confirm password",
            placeholder="6 digit password",
         
        )
        col1, col2 = st.columns(2)

        if col2.button("Already have an account", type="primary", use_container_width=True):
            st.session_state.login=True
            st.rerun()
        if col1.button("Registration", type="primary", use_container_width=True,disabled= not st.session_state.flag):
                st.session_state.clear()
                response=requests.post("https://loan-aproval-model.onrender.com/user_register",
                json={
                    "name":name,
                    "email":email,
                    "password":password
                })
                st.write(response.json)
                if response.status_code == 200:
                    data = response.json()
                    st.session_state.user_details = data

                    if data.get("user_details") == "True":
                        st.info("You already have an account, please login...")
                    else:
                                tok=requests.post("https://loan-aproval-model.onrender.com/token",
                                                  json={"name":name,"email":email,})
                                if tok.status_code==200:
                                    token=tok.json()
                                    st.session_state.token=token
                                    st.session_state.user=name
                                st.success("Successfully logged in")
                                st.switch_page("pages/predict.py")
                else:
                     st.error("please try again some time letter")
        if "flag" not in st.session_state:
            st.write("verify your email then only you can registrer your self")
             


if st.session_state.login==True:
    login()
else:
    registration()