from dash import Dash, html, dcc, callback, Output, Input

import plotly.express as px 

import pandas 

sourceFile = pandas.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv")

app = Dash(__name__)

app.layout = html.Div([
    html.H1(children="Evolution de la population", style={'textAlign' : 'center'}), 
    dcc.Dropdown(sourceFile.country.unique(), 'Benin', id='selection'),
    dcc.Graph(id='graph-content')
])

@callback(
    Output('graph-content', 'figure'), 
    Input('selection', 'value')
)

def update_graph(value):
    graph = sourceFile[sourceFile.country==value]

    return px.area(graph, x='year', y='pop')

if __name__ == '__main__': 
    app.run(debug=True)

