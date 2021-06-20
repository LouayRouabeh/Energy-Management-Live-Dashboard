import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

from sqlalchemy import create_engine

engine = create_engine('sqlite:///data.db', echo=False)


# Create a simple database
def create_sample_database():
    data = {
        'CHN': {'COUNTRY': 'China', 'POP': 1_398.72, 'AREA': 9_596.96,
                'GDP': 12_234.78, 'CONT': 'Asia'},
        'IND': {'COUNTRY': 'India', 'POP': 1_351.16, 'AREA': 3_287.26,
                'GDP': 2_575.67, 'CONT': 'Asia', 'IND_DAY': '1947-08-15'},
        'USA': {'COUNTRY': 'US', 'POP': 329.74, 'AREA': 9_833.52,
                'GDP': 19_485.39, 'CONT': 'N.America',
                'IND_DAY': '1776-07-04'},
        'IDN': {'COUNTRY': 'Indonesia', 'POP': 268.07, 'AREA': 1_910.93,
                'GDP': 1_015.54, 'CONT': 'Asia', 'IND_DAY': '1945-08-17'},
        'BRA': {'COUNTRY': 'Brazil', 'POP': 210.32, 'AREA': 8_515.77,
                'GDP': 2_055.51, 'CONT': 'S.America', 'IND_DAY': '1822-09-07'},
        'PAK': {'COUNTRY': 'Pakistan', 'POP': 205.71, 'AREA': 881.91,
                'GDP': 302.14, 'CONT': 'Asia', 'IND_DAY': '1947-08-14'},
        'NGA': {'COUNTRY': 'Nigeria', 'POP': 200.96, 'AREA': 923.77,
                'GDP': 375.77, 'CONT': 'Africa', 'IND_DAY': '1960-10-01'},
        'BGD': {'COUNTRY': 'Bangladesh', 'POP': 167.09, 'AREA': 147.57,
                'GDP': 245.63, 'CONT': 'Asia', 'IND_DAY': '1971-03-26'},
        'RUS': {'COUNTRY': 'Russia', 'POP': 146.79, 'AREA': 17_098.25,
                'GDP': 1_530.75, 'IND_DAY': '1992-06-12'},
        'MEX': {'COUNTRY': 'Mexico', 'POP': 126.58, 'AREA': 1_964.38,
                'GDP': 1_158.23, 'CONT': 'N.America', 'IND_DAY': '1810-09-16'},
        'JPN': {'COUNTRY': 'Japan', 'POP': 126.22, 'AREA': 377.97,
                'GDP': 4_872.42, 'CONT': 'Asia'},
        'DEU': {'COUNTRY': 'Germany', 'POP': 83.02, 'AREA': 357.11,
                'GDP': 3_693.20, 'CONT': 'Europe'},
        'FRA': {'COUNTRY': 'France', 'POP': 67.02, 'AREA': 640.68,
                'GDP': 2_582.49, 'CONT': 'Europe', 'IND_DAY': '1789-07-14'},
        'GBR': {'COUNTRY': 'UK', 'POP': 66.44, 'AREA': 242.50,
                'GDP': 2_631.23, 'CONT': 'Europe'},
        'ITA': {'COUNTRY': 'Italy', 'POP': 60.36, 'AREA': 301.34,
                'GDP': 1_943.84, 'CONT': 'Europe'},
        'ARG': {'COUNTRY': 'Argentina', 'POP': 44.94, 'AREA': 2_780.40,
                'GDP': 637.49, 'CONT': 'S.America', 'IND_DAY': '1816-07-09'},
        'DZA': {'COUNTRY': 'Algeria', 'POP': 43.38, 'AREA': 2_381.74,
                'GDP': 167.56, 'CONT': 'Africa', 'IND_DAY': '1962-07-05'},
        'CAN': {'COUNTRY': 'Canada', 'POP': 37.59, 'AREA': 9_984.67,
                'GDP': 1_647.12, 'CONT': 'N.America', 'IND_DAY': '1867-07-01'},
        'AUS': {'COUNTRY': 'Australia', 'POP': 25.47, 'AREA': 7_692.02,
                'GDP': 1_408.68, 'CONT': 'Oceania'},
        'KAZ': {'COUNTRY': 'Kazakhstan', 'POP': 18.53, 'AREA': 2_724.90,
                'GDP': 159.41, 'CONT': 'Asia', 'IND_DAY': '1991-12-16'}
    }

    columns = ('COUNTRY', 'POP', 'AREA', 'GDP', 'CONT', 'IND_DAY')

    df = pd.DataFrame(data=data).T

    dtypes = {'POP': 'float64', 'AREA': 'float64', 'GDP': 'float64', 'IND_DAY': 'datetime64'}
    df = pd.DataFrame(data=data).T.astype(dtype=dtypes)
    df.dtypes

    df.to_sql('data.db', con=engine, if_exists='replace')


create_sample_database()


# Dash
def generate_table(dataframe, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in dataframe.columns])] +

        # Body
        [html.Tr([
            html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
        ]) for i in range(min(len(dataframe), max_rows))]
    )


app = dash.Dash()
app.layout = html.Div([
    dcc.Input(
        id='sql-query',
        value='SELECT * FROM data.db',
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
    dash.dependencies.Output('table-container', 'children'),
    [dash.dependencies.Input('table-store', 'children')])
def dff_to_table(dff_json):
    dff = pd.read_json(dff_json)
    return generate_table(dff)


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
