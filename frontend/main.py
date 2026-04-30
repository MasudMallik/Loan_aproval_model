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
    response = requests.post("https://loan-aproval-model.onrender.com/logout",headers={"Authorization": f"Bearer {st.session_state.token["token"]}"})
    del st.session_state["user"]
    if response.status_code == 200:
        st.sidebar.success("Logged out successfully")
    else:
        st.sidebar.error("Logout failed")



pages.run()
