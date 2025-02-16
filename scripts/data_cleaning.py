import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)
    df_clean = df.dropna().drop_duplicates()
    df_clean.to_csv("cleaned_data.csv", index=False)
    print("Dados limpos e salvos com sucesso!")

# Exemplo de uso:
# clean_data("dataset.csv")
