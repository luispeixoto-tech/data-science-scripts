#🔹 Português: Esse script treina um modelo de regressão linear para prever valores numéricos.
#🔹 English: This script trains a linear regression model to predict numerical values.

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error


# Carregar os dados
df = pd.read_csv("dataset.csv")

# Selecionar variáveis preditoras e alvo
X = df[['variavel1', 'variavel2']]
y = df['target']

# Separar os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Treinar o modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Fazer previsões
y_pred = model.predict(X_test)

# Avaliação do modelo
mae = mean_absolute_error(y_test, y_pred)
print(f"Erro Absoluto Médio: {mae}")

# Salvar modelo treinado
import joblib
joblib.dump(model, "linear_regression_model.pkl")
print("Modelo salvo com sucesso!")

###
#📌 Este script:
#✅ Carrega um dataset, separa treino/teste.
#✅ Treina um modelo de regressão linear.
#✅ Mede o erro do modelo com Mean Absolute Error (MAE).
#✅ Salva o modelo treinado (linear_regression_model.pkl).
#

#
#
#📌 This script:
#✅ Loads a dataset, separates training/testing.
#✅ Trains a linear regression model.
#✅ Measures the model error with Mean Absolute Error (MAE).
#✅ Saves the trained model (linear_regression_model.pkl).
#
