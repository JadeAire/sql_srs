import pandas as pd
import duckdb

with duckdb.connect(database="data/sql.duckdb", read_only = False) as con : 
    con.execute("CREATE TABLE IF NOT EXISTS production_logs AS SELECT * FROM 'data/raw_data/production_logs.json'")
    con.execute("CREATE TABLE IF NOT EXISTS machines AS SELECT * FROM 'data/raw_data/machines.json'")