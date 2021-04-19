import dash_core_components as dcc
import pandas as pd

ground = pd.read_excel("consumption.xlsx", "Sheet1")

content0 = dcc.Graph(
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
)
