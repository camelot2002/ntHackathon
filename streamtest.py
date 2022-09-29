import numpy as np
import pandas as pd
import glob
import os
import altair as alt
import streamlit as st
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt

df1 = pd.read_csv("dataset.csv")
w=pd.read_csv("weekly.csv")

def main_page():
    st.markdown("Exchange Rates")


    choice_options = df1.columns[1:]
    time_options = [ "Monthly","Weekly", "Quarterly"]
    year1 = range(2012,2023)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        choice=st.selectbox("Default Currency", choice_options)

    with col2:
        choice2 = st.selectbox("Select the Country value", choice_options)
    with col3:
        frequency = st.selectbox("Select the time range", time_options)
    with col4:
        year2 = st.selectbox("Select the time range", year1)


    def plot(choice,filter):
        dataset = pd.DataFrame(df1)
        # df1['year']=year(df1['Date'])
        dataset["rel"]=dataset[choice2]/dataset[choice]
        a=dataset.loc[dataset[choice2].idxmax()]
        b = dataset.loc[dataset[choice2].idxmin()]
        st.write("MAX")
        st.write(a["rel"])
        st.write("MIN")
        st.write(b["rel"])




        line_chart = alt.Chart(dataset).mark_line().encode(
            x=alt.X("Date:T",scale=alt.Scale(domain=list(filter))),

            # x=alt.X("Date:T",scale=alt.Scale(domain=(str(year),str(int(year)+1 )))),
            y=alt.Y("rel"),


        ).interactive()
        st.altair_chart(line_chart,use_container_width=True)
        pass

    if frequency == "Monthly":
        filter = pd.date_range(start='01-01-{}'.format(year2), end='30-12-{}'.format(year2), freq='D')
        with st.container():
            plot(choice, filter)
    elif frequency == "Weekly":
        filter = pd.date_range(start='01-01-{}'.format(year2), end='01-12-{}'.format(year2), freq='W')
        with st.container():
            plot(choice, filter)

    elif frequency == "Quarterly":
        filter = ('01-01-{}'.format(year2), '04-01-{}'.format(year2),'08-01-{}'.format(year2),'12-01-{}'.format(year2) )
        with st.container():
            plot(choice, filter)







    st.sidebar.markdown("Exchange Rates")

def page2():
    st.markdown("Currency Convertor️")
    tup=df1.columns[1:]
    list1=list(tup)
    option1 = st.selectbox(
        'From',
       tup)
    list1.remove(option1)
    tup1=tuple(list1)
    option2 = st.selectbox(
        'To',tup1
        )
    title = st.text_input('Enter Amount')

    if title.isnumeric()==True:
        df2=df1.tail(1)
        calc=float(df2[option2]/df2[option1])
        title1 = st.text_input('Output',calc)

    st.sidebar.markdown("Currency Convertor️")



page_names_to_funcs = {
    "Exchange Rates": main_page,
    "Currency Convertor": page2,

}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()





