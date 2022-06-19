import streamlit as st
import numpy as np
import pandas as pd
from data.create_data import create_table

def app():
    st.title('History')

    st.write("This is a sample data stats in the mutliapp.")
    st.markdown("### Sample Data")
    df = create_table()
    st.write(df)

    st.write('Navigate to `home` page to enter the data')