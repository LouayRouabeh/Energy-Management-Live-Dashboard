import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import dash
import matplotlib.pyplot as plt
import dash_html_components as html
import dash_core_components as dcc
from app import app

from dash.dependencies import Input, Output

df = pd.read_excel('EleConsumption.xlsx', sheet_name='RegGround')

tab1 = html.Div([dcc.Graph(
    figure=px.scatter(df, x='HDD 18(666)', y='consumption(666)', trendline='ols')
), dcc.Graph(
    figure=px.scatter(df, x='HDD 18(667)', y='consumption(667)', trendline='ols')
)])

regression = html.Div([
    dcc.Tabs(id="tabs", value='tab-1', children=[
        dcc.Tab(label='ground', value='tab-1'),
        dcc.Tab(label='floor 1', value='tab-2'),
        dcc.Tab(label='floor 2', value='tab-3'),
        dcc.Tab(label='floor 3', value='tab-4')
    ]),
    html.Div(id='tabs-content')
]

)


@app.callback(Output('tabs-content', 'children'),
              Input('tabs', 'value'))
def render_content(tab):
    if tab == 'tab-1':
        return html.Div([
            tab1
        ])
    elif tab == 'tab-2':
        return html.Div([
            html.H3('first floor')
        ])
    elif tab == 'tab-3':
        return html.Div([
            html.H3('second floor')
        ])
    elif tab == 'tab-4':
        return html.Div([
            html.H3('third floor')
        ])
