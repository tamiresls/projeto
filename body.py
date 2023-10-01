from dash.html import Div
from dash.dcc import Graph, Dropdown
from data import vendas, produtos
import plotly.express as px


body = Div(
    id = 'body',
    style={
        'margin': '20px 3% 0 3%',
        'marginLeft': '3%',
        'marginRight': '3%'
    },
    children= [
        Dropdown(
            id = 'opcoes',
            options= [{'label': 'Valor de Venda','value':'preco_de_venda'},
                      {'label': 'Quantidade de Venda', 'value': 'qtde'}],
            value= 'preco_de_venda',
            style={
                'background-color': 'pink',
                'border': '0.2px solid gray',
                'color': 'black',
                'border-radius': '5px'
            }
        ),
        Dropdown(
            id = 'agrupamento',
            options= ['Itens', 'Família'],
            value= 'Itens',
            style={
                'background-color': 'pink',
                'border': '0.2px solid gray',
                'color': 'black',
                'border-radius': '5px'
            }
        ),
        Graph(
            id = 'grafico',
            style={
                'background-color': 'gray',
                'border': '2px solid gray',
                'box-shadow': '5px 5px 5px black',
                'border-radius': '8px'
            }
        )
        
    ]
)