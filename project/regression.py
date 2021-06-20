import pandas as pd
import plotly.express as px

import dash_html_components as html
import dash_core_components as dcc
from app import app

from dash.dependencies import Input, Output

df = pd.read_excel('EleConsumption.xlsx', sheet_name='RegGround')
df2 = pd.read_excel('EleConsumption.xlsx', sheet_name='RegFirst')
df3 = pd.read_excel('EleConsumption.xlsx', sheet_name='RegSecond')
df4 = pd.read_excel('EleConsumption.xlsx', sheet_name='RegThird')

tab1 = html.Div([dcc.Graph(
    figure=px.scatter(df, x='CDD 18(666)', y='consumption(666)', trendline='ols')
), dcc.Graph(
    figure=px.scatter(df, x='CDD 18(667)', y='consumption(667)', trendline='ols')
)])

tab2 = html.Div([dcc.Graph(
    figure=px.scatter(df2, x='CDD25(670)', y='consumption(670)', trendline='ols')
), dcc.Graph(
    figure=px.scatter(df2, x='CDD25(669)', y='consumption(669)', trendline='ols')
), dcc.Graph(
    figure=px.scatter(df2, x='CDD25(659)', y='consumption(659)', trendline='ols')
), dcc.Graph(
    figure=px.scatter(df2, x='CDD25(658)', y='consumption(658)', trendline='ols')
)])

tab3 = html.Div([dcc.Graph(
    figure=px.scatter(df3, x='CDD25(672)', y='consumption(672)', trendline='ols')
), dcc.Graph(
    figure=px.scatter(df3, x='CDD25(671)', y='consumption(671)', trendline='ols')
)])

tab4 = html.Div([dcc.Graph(
    figure=px.scatter(df4, x='CDD25(673)', y='consumption(673)', trendline='ols')
), dcc.Graph(
    figure=px.scatter(df4, x='CDD25(674)', y='consumption(674)', trendline='ols')
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
            tab2
        ])
    elif tab == 'tab-3':
        return html.Div([
            tab3
        ])
    elif tab == 'tab-4':
        return html.Div([
            tab4
        ])
