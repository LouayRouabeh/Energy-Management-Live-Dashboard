import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import numpy as np

app = dash.Dash()
colors = {'backgound': '#111111', 'text': '#7FDBFF'}

app.layout = html.Div(children=[html.H1('hello Dash!', style={'textAlign': 'center', 'color': colors['text']}),

                                dcc.Graph(id='example', figure={'data': [
                                    {'x': [1, 2, 3], 'y':[4, 1, 2],
                                        'type':'bar', 'name':'SF'},
                                    {'x': [1, 2, 3], 'y':[2, 4, 5],
                                        'type':'bar', 'name':'NYC'}
                                ],
                                    'layout':{
                                    'plot_bgcolor': colors['backgound'],
                                    'paper_bgcolor': colors['backgound'],
                                    'font': {'color': colors['text']},
                                    'title': 'BAR PLOTS!'
                                }})
                                ], style={'backgoundColor': colors['backgound']})
np.random.seed(42)
random_x = np.random.randint(1, 101, 100)
random_y = np.random.randint(1, 101, 100)
app.layout = html.Div([dcc.Graph(id='scatterplot',
                                 figure={'data': [
                                    go.Scatter(x=random_x,
                                               y=random_y,
                                               mode='markers',
                                               marker={
                                                   'size': 12,
                                                   'color': 'rgb(200,204,53)',
                                                   'symbol': 'pentagon',
                                                   'line': {'width': 2}
                                               }
                                               )],
                                         'layout': go.Layout(title='My Scatterplot',
                                                             xaxis={
                                                                 'title': 'some X title'}
                                                             )}
                                 ),
                       dcc.Graph(id='scatterplot2',
                                 figure={'data': [
                                    go.Scatter(x=random_x,
                                               y=random_y,
                                               mode='markers',
                                               marker={
                                                   'size': 12,
                                                   'color': 'rgb(51,204,153)',
                                                   'symbol': 'pentagon',
                                                   'line': {'width': 2}
                                               }
                                               )],
                                         'layout': go.Layout(title='My 2 Scatterplot',
                                                             xaxis={
                                                                 'title': 'some X title'}
                                                             )}
                                 )
                       ])

app.run_server()
