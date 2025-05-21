import pandas as pd
import duckdb

production_log = [
    {
        "machine_id": "M1",
        "production_date": "2024-04-01",
        "units_produced": 480,
        "expected_units": 600,
    },
    {
        "machine_id": "M2",
        "production_date": "2024-04-01",
        "units_produced": 300,
        "expected_units": 300,
    },
    {
        "machine_id": "M3",
        "production_date": "2024-04-01",
        "units_produced": 250,
        "expected_units": 400,
    },
    {
        "machine_id": "M1",
        "production_date": "2024-04-02",
        "units_produced": 510,
        "expected_units": 600,
    },
    {
        "machine_id": "M2",
        "production_date": "2024-04-02",
        "units_produced": 280,
        "expected_units": 300,
    },
    {
        "machine_id": "M3",
        "production_date": "2024-04-02",
        "units_produced": 390,
        "expected_units": 400,
    },
    {
        "machine_id": "M1",
        "production_date": "2024-04-03",
        "units_produced": 600,
        "expected_units": 600,
    },
    {
        "machine_id": "M2",
        "production_date": "2024-04-03",
        "units_produced": 290,
        "expected_units": 300,
    },
    {
        "machine_id": "M3",
        "production_date": "2024-04-03",
        "units_produced": 410,
        "expected_units": 400,
    },
    {
        "machine_id": "M1",
        "production_date": "2024-04-04",
        "units_produced": 450,
        "expected_units": 600,
    },
    {
        "machine_id": "M2",
        "production_date": "2024-04-04",
        "units_produced": 310,
        "expected_units": 300,
    },
    {
        "machine_id": "M3",
        "production_date": "2024-04-04",
        "units_produced": 420,
        "expected_units": 400,
    },
    {
        "machine_id": "M1",
        "production_date": "2024-04-05",
        "units_produced": 470,
        "expected_units": 600,
    },
    {
        "machine_id": "M2",
        "production_date": "2024-04-05",
        "units_produced": 290,
        "expected_units": 300,
    },
    {
        "machine_id": "M3",
        "production_date": "2024-04-05",
        "units_produced": 350,
        "expected_units": 400,
    },
]

machines = [
    {
        "machine_id": "M1",
        "machine_name": "Machine Alpha",
        "installation_date": "2020-01-01",
    },
    {
        "machine_id": "M2",
        "machine_name": "Machine Beta",
        "installation_date": "2021-03-15",
    },
]

df_prod_logs = pd.DataFrame(production_log)
df_machines = pd.DataFrame(machines)

with duckdb.connect(database="data/sql.duckdb", read_only = False) as con : 
    con.execute("CREATE TABLE IF NOT EXISTS production_logs AS SELECT * FROM df_prod_logs")
    con.execute("CREATE TABLE IF NOT EXISTS machines AS SELECT * FROM df_machines")
    con.sql("SELECT * FROM machines").show()