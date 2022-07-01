import streamlit as st
import numpy as np
import pandas as pd
from data.create_data import create_table
import requests
def app():
    st.title('History')

    st.markdown("Our Tweets")
    res = requests.get(f"http://127.0.0.1:5000/getAllTweets")
    data = res.json()
    df = pd.DataFrame(data['Tweets'])
    st.table(df)

    st.write('Navigate to `home` page to enter the data')