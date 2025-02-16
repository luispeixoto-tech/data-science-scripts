import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def exploratory_analysis(file_path):
    df = pd.read_csv(file_path)
    print(df.describe())
    print(df.isnull().sum())

    plt.figure(figsize=(10,5))
    sns.histplot(df['variavel_interessante'], bins=30, kde=True)
    plt.title("Distribuição da Variável")
    plt.show()

# Exemplo de uso:
# exploratory_analysis("dataset.csv")
