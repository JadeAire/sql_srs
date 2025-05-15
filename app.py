import streamlit as st
import pandas as pd
import duckdb

data = {"a" : [1, 2, 3], "b" : [4, 5, 6]}


st.write("Hello World")

query = st.text_area(label="Write your SQL command")
st.write(f"Voici votre requête : {query}")


df = pd.DataFrame(data)

st.dataframe(duckdb.sql(query).df())