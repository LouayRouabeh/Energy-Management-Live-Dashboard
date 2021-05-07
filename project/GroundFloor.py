import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from dash.dependencies import Output, Input
from app import app
from dash_extensions import Download
from dash_extensions.snippets import send_data_frame

ground = pd.read_excel("consumption.xlsx", "Sheet1")

content0 = html.Div([html.Button("Download", id="btn"), Download(id="download"), dcc.Graph(
    figure=dict(
        data=[
            dict(
                x=ground['Month'],
                y=ground['consumption'],
                name='2019',
                marker=dict(
                    color='rgb(55, 83, 109)'
                )
            ),

        ],
        layout=dict(
            title='consumption ',
            showlegend=True,
            legend=dict(
                x=0,
                y=1.0
            ),
            margin=dict(l=40, r=0, t=40, b=30)
        )
    ),
    style={'height': 300},
    id='my-graph'
)])


@app.callback(Output("download", "data"), [Input("btn", "n_clicks")])
def func(n_clicks):
    return send_data_frame(ground.to_csv, "groundFloor.csv", index=False)
