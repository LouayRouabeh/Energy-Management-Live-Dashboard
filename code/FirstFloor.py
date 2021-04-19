import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import dash_core_components as dcc

first = pd.read_excel("consumption.xlsx", "FirstFloor")

content1 = html.Div([dcc.Graph(id='barplot',
                               figure={'data': [
                                   go.Bar(x=first["Month"],
                                          y=first["consumption(670)"],

                                          marker={

                                       'color': 'rgb(200,204,53)',

                                   }
                                   )],
                                   'layout': go.Layout(title='consumption of counter 670 per month',
                                                       xaxis={
                                                           'title': '2019'}
                                                       )}
                               ),
                     dcc.Graph(id='barplot2',
                               figure={'data': [
                                   go.Bar(x=first["Month"],
                                          y=first["consumption(669)"],

                                          marker={

                                       'color': 'rgb(51,204,153)',

                                   }
                                   )],
                                   'layout': go.Layout(title='consumption of counter 669 per month',
                                                       xaxis={
                                                           'title': 'year 2019'}
                                                       )}
                               ),
                     dcc.Graph(id='barplot3',
                               figure={'data': [
                                   go.Bar(x=first["Month"],
                                          y=first["consumption(659)"],

                                          marker={

                                       'color': '#40E0D0',

                                   }
                                   )],
                                   'layout': go.Layout(title='consumption of counter 659 per month',
                                                       xaxis={
                                                           'title': '2019'}
                                                       )}
                               ),
                     dcc.Graph(id='barplot4',
                               figure={'data': [
                                   go.Bar(x=first["Month"],
                                          y=first["consumption(658)"],

                                          marker={

                                       'color': '#FFEBCD',

                                   }
                                   )],
                                   'layout': go.Layout(title='consumption of counter 658 per month',
                                                       xaxis={
                                                           'title': '2019'}
                                                       )}
                               )

                     ])
