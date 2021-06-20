import base64
import datetime
import io
import plotly.graph_objs as go
import dash
from app import app
from dash.dependencies import Input, Output, State
import dash_core_components as dcc
import dash_html_components as html
import dash_table

import pandas as pd

from sqlalchemy import create_engine

# INSERT INTO "data1.db" (data, month, meter) VALUES (6666,'11-UU',844)

colors = {"graphBackground": "#F5F5F5", "background": "#ffffff", "text": "#000000"}

engine = create_engine('sqlite:///data.db', echo=False)




upload = html.Div([
    dcc.Upload(
        id="upload-data",
        children=html.Div(["Drag and Drop or ", html.A("Select Files")]),
        style={
            "width": "100%",
            "height": "60px",
            "lineHeight": "60px",
            "borderWidth": "1px",
            "borderStyle": "dashed",
            "borderRadius": "5px",
            "textAlign": "center",
            "margin": "10px",
        },
        # Allow multiple files to be uploaded
        multiple=True,
    ),
    dash_table.DataTable(id='output-data-upload', editable=True, export_format='xlsx',
                         export_headers='display',
                         merge_duplicate_headers=True),
    dcc.Graph(id="Mygraph"),
    html.Div(id="output-data-upload1"),
    dcc.Input(
        id='sql-query',
        value='SELECT * FROM "data1.db"',
        style={'width': '100%'},
        type='text'
    ),
    html.Button('Run Query', id='run-query'),

    html.Hr(),

    html.Div([
        html.Div(id='table-container', className="four columns"),

        html.Div([
            html.Div([
                html.Div([
                    html.Label('Select X'),
                    dcc.Dropdown(
                        id='dropdown-x',
                        clearable=False,
                    )
                ], className="six columns"),
                html.Div([
                    html.Label('Select Y'),
                    dcc.Dropdown(
                        id='dropdown-y',
                        clearable=False,
                    )
                ], className="six columns")
            ], className="row"),
            html.Div(dcc.Graph(id='graph'), className="ten columns")
        ], className="eight columns")
    ], className="row"),

    # hidden store element
    html.Div(id='table-store', style={'display': 'none'})
])


@app.callback(Output('Mygraph', 'figure'), [
    Input('upload-data', 'contents'),
    Input('upload-data', 'filename')
])
def update_graph(contents, filename):
    x = []
    y = []
    if contents:
        contents = contents[0]
        filename = filename[0]
        df = parse_data(contents, filename)
        df = df.set_index(df.columns[0])
        df.to_sql('data.db', con=engine, if_exists='replace')
        x = df['Month']
        y = df['Data']
    fig = go.Figure(
        data=[
            go.Scatter(
                x=x,
                y=y,
                mode='lines+markers')
        ],
        layout=go.Layout(
            plot_bgcolor=colors["graphBackground"],
            paper_bgcolor=colors["graphBackground"]
        ))
    return fig


def parse_data(contents, filename):
    content_type, content_string = contents.split(",")

    decoded = base64.b64decode(content_string)
    try:
        if "csv" in filename:
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8")))
        elif "xls" in filename:
            df = pd.read_excel(io.BytesIO(decoded))
        elif "txt" or "tsv" in filename:
            df = pd.read_csv(io.StringIO(decoded.decode("utf-8")), delimiter=r"\s+")
    except Exception as e:
        print(e)
        return html.Div(["There was an error processing this file."])

    return df


@app.callback(
    Output("output-data-upload", "children"),
    [Input("upload-data", "contents"), Input("upload-data", "filename")],
)
def update_table(contents, filename):
    table = html.Div()

    if contents:
        contents = contents[0]
        filename = filename[0]
        df = parse_data(contents, filename)

        table = html.Div(
            [
                html.H5(filename),
                dash_table.DataTable(
                    data=df.to_dict("rows"),
                    columns=[{"name": i, "id": i} for i in df.columns],
                ),
                html.Hr(),
                html.Div("Raw Content"),
                html.Pre(
                    contents[0:200] + "...",
                    style={"whiteSpace": "pre-wrap", "wordBreak": "break-all"},
                ),
            ]
        )

    return table


@app.callback(
    dash.dependencies.Output('table-store', 'children'),
    [dash.dependencies.Input('run-query', 'n_clicks')],
    state=[dash.dependencies.State('sql-query', 'value')])
def sql(number_of_times_button_has_been_clicked, sql_query):
    dff = pd.read_sql_query(
        sql_query,
        engine
    )
    return dff.to_json()




@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input('table-store', 'children'),
     dash.dependencies.Input('dropdown-x', 'value'),
     dash.dependencies.Input('dropdown-y', 'value')])
def dff_to_table(dff_json, dropdown_x, dropdown_y):
    dff = pd.read_json(dff_json)
    return {
        'data': [{
            'x': dff[dropdown_x],
            'y': dff[dropdown_y],
            'type': 'bar'
        }],
        'layout': {
            'margin': {
                'l': 20,
                'r': 10,
                'b': 60,
                't': 10
            }
        }
    }


@app.callback(
    dash.dependencies.Output('dropdown-x', 'options'),
    [dash.dependencies.Input('table-store', 'children')])
def create_options_x(dff_json):
    dff = pd.read_json(dff_json)
    return [{'label': i, 'value': i} for i in dff.columns]


@app.callback(
    dash.dependencies.Output('dropdown-y', 'options'),
    [dash.dependencies.Input('table-store', 'children')])
def create_options_y(dff_json):
    dff = pd.read_json(dff_json)
    return [{'label': i, 'value': i} for i in dff.columns]


app.css.append_css({"external_url": "https://codepen.io/chriddyp/pen/bWLwgP.css"})

if __name__ == '__main__':
    app.run_server(debug=True)
