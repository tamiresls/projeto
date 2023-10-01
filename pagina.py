from dash import Dash, Output, Input
from header import header
from dash.html import Div
from body import body
import pandas as pd
import plotly.express as px

app = Dash(__name__)


@app.callback(
    Output('grafico', 'figure'),
    Input('opcoes', 'value'),
    Input('agrupamento', 'value')
)

def create_chart(opcoes, agrupamento):
    vendas = pd.read_csv('vendas.csv')
    with open('produtos.csv', 'r', encoding='utf-8', errors='ignore') as file:
        produtos = pd.read_csv(file)
    combined_data = pd.merge(produtos, vendas, left_on='produtos_id', right_on='item_id', how='inner')
    if agrupamento == 'Itens':
        soma = vendas.groupby('item_id').sum().reset_index()
        fig = px.bar(soma, x='item_id', y=opcoes, 
                     labels={'item_id': 'Itens', 'preco_de_venda': 'Valor de Venda', 'qtde': 'Quantidade de Venda'},
                     color_discrete_sequence=['SlateGray'])
    elif agrupamento == 'Família':
        soma = combined_data.groupby('tipo')[opcoes].sum().reset_index()
        fig = px.bar(soma, x='tipo', y=opcoes, 
                     labels={'tipo': 'Família', 'preco_de_venda': 'Valor de Venda', 'qtde': 'Quantidade de Venda'}, 
                     color_discrete_sequence=['SlateGray'])

    return fig


app.layout = Div(
    children = [
        header,
        body
        ]
    )

app.run_server(debug=True, port=8000)