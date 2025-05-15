import streamlit as st
import pandas as pd
import duckdb

data = {"a" : [1, 2, 3], "b" : [4, 5, 6]}


st.write("Hello World")

option = st.selectbox("What would you like to review ?", 
                      ("joins", "groupby", "windows function"),
                      index = None,
                      placeholder="Select a theme")

query = st.text_area(label="Write your SQL command")



df = pd.DataFrame(data)

if query :
    st.write(f"Voici votre requête : {query}")
    st.dataframe(duckdb.sql(query).df())