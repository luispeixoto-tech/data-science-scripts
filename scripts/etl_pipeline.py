#🔹 Português: Esse script faz extração, transformação e carregamento de dados.
#🔹 English: This script performs extract, transform, and load (ETL) operations.

import pandas as pd
import sqlite3

def extract_data(file_path):
    return pd.read_csv(file_path)

def transform_data(df):
    df_clean = df.dropna().drop_duplicates()
    return df_clean

def load_data(df, db_name="database.db"):
    conn = sqlite3.connect(db_name)
    df.to_sql("dados_processados", conn, if_exists="replace", index=False)
    conn.close()
    print("Dados carregados no banco de dados com sucesso!")

# Pipeline ETL
df = extract_data("dataset.csv")
df_transformed = transform_data(df)
load_data(df_transformed)


#📌 Este script:
#✅ Extrai dados de um arquivo CSV.
#✅ Transforma os dados limpando valores nulos e duplicatas.
#✅ Carrega os dados em um banco SQLite (database.db).
#
#📌 This script:
#✅ Extracts data from a CSV file.
#✅ Transforms the data by cleaning null values ​​and duplicates.
#✅ Loads the data into an SQLite database (database.db).

