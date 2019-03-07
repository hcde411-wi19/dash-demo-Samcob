# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np
import pandas as pd


# Exercise 2
# Create another visualization of your choice of data and chart type.
# You can use pandas to help loading data, or just hard-coded the data is fine.

#Static Data
stats = ["HP", "Attack", "Defense", "Sp. Attack", "Sp. Defence", "Speed"]
charizard = [78, 84, 78, 109, 85, 100]
venusaur = [80, 82, 83, 100, 100, 80]
blastoise = [79, 83, 100, 85, 105, 78]
mewtwo = [106, 110, 90, 154, 90, 130]


# initialize Dash environment
app = dash.Dash(__name__)

# set up an layout
app.layout = html.Div(children=[
    # H1 title on the page
    html.H1(children='Pokemon Stat Comparison'),

    # a div to put a short description
    html.Div(children='''
        This is a simple Dash application that compares the stats of a few classic pokemon.
    '''),

    # append the visualization to the page
    dcc.Graph(
        id='Starter Pokemon Comparison',
        figure={
            'data': [{
                'marker': {'color': 'red', 'size': '10'},
                'mode': 'markers+lines',
                'name': 'Charizard',
                'type': 'scatter',
                'x': stats,
                'y': charizard
            },{
                'marker': {'color': 'green', 'size': '10'},
                'mode': 'markers+lines',
                'name': 'Venusaur',
                'type': 'scatter',
                'x': stats,
                'y': venusaur
            }, {
                'marker': {'color': 'blue', 'size': '10'},
                'mode': 'markers+lines',
                'name': 'Blastoise',
                'type': 'scatter',
                'x': stats,
                'y': blastoise
            }, {
                'marker': {'color': 'purple', 'size': '10'},
                'mode': 'markers+lines',
                'name': 'Mewtwo',
                'type': 'scatter',
                'x': stats,
                'y': mewtwo
            }],
            'layout': {
                'title': 'Pokemon Stats',
                'xaxis': {'title': 'Stats'},
                'yaxis': {'title': 'Value'}
            }
        }

    )
])

if __name__ == '__main__':
    # start the Dash app
    app.run_server(debug=True)
