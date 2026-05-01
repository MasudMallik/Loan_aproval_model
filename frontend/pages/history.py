import streamlit as st
import requests
import pandas as pd
st.set_page_config(layout="wide")
if "user" not in st.session_state:
    st.warning("For previewing your history please login first")
else:
    response=requests.post("http://127.0.0.1:8000/get_data",headers={"Authorization": f"Bearer {st.session_state.token["token"]}"})
    if response.status_code==200:
        st.write("History...")
        data = response.json()
        # Extract the list
        records = data["data"]

        # Convert to DataFrame
        df = pd.DataFrame(records)

        st.dataframe(df,use_container_width=True)
        