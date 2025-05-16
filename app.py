import streamlit as st
import pandas as pd
import duckdb

production_log = [
    {"machine_id": "M1", "production_date": "2024-04-01", "units_produced": 480, "expected_units": 600},
    {"machine_id": "M2", "production_date": "2024-04-01", "units_produced": 300, "expected_units": 300},
    {"machine_id": "M3", "production_date": "2024-04-01", "units_produced": 250, "expected_units": 400},
    
    {"machine_id": "M1", "production_date": "2024-04-02", "units_produced": 510, "expected_units": 600},
    {"machine_id": "M2", "production_date": "2024-04-02", "units_produced": 280, "expected_units": 300},
    {"machine_id": "M3", "production_date": "2024-04-02", "units_produced": 390, "expected_units": 400},

    {"machine_id": "M1", "production_date": "2024-04-03", "units_produced": 600, "expected_units": 600},
    {"machine_id": "M2", "production_date": "2024-04-03", "units_produced": 290, "expected_units": 300},
    {"machine_id": "M3", "production_date": "2024-04-03", "units_produced": 410, "expected_units": 400},

    {"machine_id": "M1", "production_date": "2024-04-04", "units_produced": 450, "expected_units": 600},
    {"machine_id": "M2", "production_date": "2024-04-04", "units_produced": 310, "expected_units": 300},
    {"machine_id": "M3", "production_date": "2024-04-04", "units_produced": 420, "expected_units": 400},

    {"machine_id": "M1", "production_date": "2024-04-05", "units_produced": 470, "expected_units": 600},
    {"machine_id": "M2", "production_date": "2024-04-05", "units_produced": 290, "expected_units": 300},
    {"machine_id": "M3", "production_date": "2024-04-05", "units_produced": 350, "expected_units": 400},
]

df_prod_logs = pd.DataFrame(production_log)

machines = [
    {"machine_id": "M1", "machine_name": "Machine Alpha", "installation_date": "2020-01-01"},
    {"machine_id": "M2", "machine_name": "Machine Beta", "installation_date": "2021-03-15"},
]

df_machines = pd.DataFrame(machines)

answer = """
SELECT
    machine_name,
    SUM(units_produced) AS units_produced_30_last_days,
    SUM(expected_units) AS units_expected_30_last_days,
    units_produced_30_last_days / units_expected_30_last_days AS productivity
FROM df_machines
LEFT JOIN df_prod_logs
USING(machine_id)
WHERE CAST(production_date AS DATE) <= CURRENT_DATE - INTERVAL 30 DAYS
GROUP BY machine_name
HAVING(productivity < 0.85)
"""

solution = duckdb.sql(answer).df()

with st.sidebar :
    option = st.selectbox("What subject would you like to work on ?",
                        ("RH", "production"),
data = {"a" : [1, 2, 3], "b" : [4, 5, 6]}


st.write("Hello World")

with st.sidebar :
    option = st.selectbox("What would you like to review ?",
                        ("joins", "groupby", "windows function"),
                        index = None,
                        placeholder="Select a theme")
    st.text(f"vous avez choisi : {option}")


st.write("Suivi de performance machine (TRS ou OEE)")
st.write("Quelle est la performance moyenne de chaque machine au cours des 30 derniers jours ? Quelles machines ont un rendement inférieur à 80 % ?")

st.header("Enter your code :")
query = st.text_area(label="Write your SQL command", key="user_input")


tab1, tab2 = st.tabs(["Tables", "Solution"])

with tab1:
    st.write("table : machine")
    st.dataframe(df_machines)
    st.write("table : Logs de production")
    st.dataframe(df_prod_logs)
    st.write("tables attendue")
    st.dataframe(solution)

with tab2:
    st.write(answer)