import pandas as pd


vendas = pd.read_csv('vendas.csv')

with open('produtos.csv', 'r', encoding='utf-8', errors='ignore') as file:
    produtos = pd.read_csv(file)


#tipos_de_colunas = vendas.dtypes

#print(tipos_de_colunas)
