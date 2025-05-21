import streamlit as st
import pandas as pd
import duckdb

subjects = ["bash", "sql", "git", "python"]
types_exercice = ['trouver fonction','expliquer fonction','résoudre problématique','tous']

# answer = """
# SELECT
#     machine_name,
#     SUM(units_produced) AS units_produced_30_last_days,
#     SUM(expected_units) AS units_expected_30_last_days,
#     units_produced_30_last_days / units_expected_30_last_days AS productivity
# FROM df_machines
# LEFT JOIN df_prod_logs
# USING(machine_id)
# WHERE CAST(production_date AS DATE) <= CURRENT_DATE - INTERVAL 30 DAYS
# GROUP BY machine_name
# HAVING(productivity < 0.85)
# """

# solution = duckdb.sql(answer).df()

with st.sidebar:
    option = st.selectbox(
        "What subject would you like to work on ?",
        subjects,
        index=None,
        placeholder="Select a subject",
    )

if option :
    st.header(f"You are in {option} section")
else : 
    st.header(f"Please select a subject, on the lateral bar")

# st.header("Enter your code :")
# query = st.text_area(label="Write your SQL command", key="user_input")


# tab1, tab2 = st.tabs(["Tables", "Solution"])

# with tab1:
#     st.write("table : machine")
#     st.dataframe(df_machines)
#     st.write("table : Logs de production")
#     st.dataframe(df_prod_logs)
#     st.write("tables attendue")
#     st.dataframe(solution)


# with tab2:
#     st.write(answer)
