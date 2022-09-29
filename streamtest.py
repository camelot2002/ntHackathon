import streamlit as st
import altair as alt
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime

data = pd.read_csv('dataset.csv')

st.set_page_config("Northern Trust", layout='wide')

choice_options = list(data.columns[1:])
time_options = ["Daily", "Weekly", "Quarterly", "Yearly"]

format_date = "%d/%m/%y"

data_melted = pd.melt(
    data, id_vars=['Date'], var_name='parameter', value_name='value')


col1, col2, col3 = st.columns(3)
with col1:
    st.selectbox("Default Currency", ["USD"])
with col2:
    choice = st.selectbox("Select the Country value", choice_options)
with col3:
    time = st.selectbox("Select the time range", time_options)
with st.container():
    value = data.iloc[:, data]
    c = alt.Chart(data_melted, title='Exchange Rate').mark_line().encode(
        x='Date', y=data[choice].tolist(), color='parameter').interactive()
    st.altair_chart(c)
    price_max = data[choice].max()
    price_min = data[choice].min()
    st.write("The Max value between is: ", price_max)
    st.write("The Min value between is: ", price_min)
