import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc

from dash.dependencies import Input, Output


from regression import regression
from GroundFloor import content0

from floor1 import firstFloor
from app import app

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

# padding for the page content
CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

sidebar = html.Div(
    [
        html.H2("Medtech", className="display-4"),
        html.Hr(),
        html.P(
            "Electricity consumption and cost", className="lead"
        ),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Floor1", href="/floor1", active="exact"),
                dbc.NavLink("Floor2", href="/floor2", active="exact"),
                dbc.NavLink("Floor3", href="/floor3", active="exact"),
                dbc.NavLink("Regression", href="/regression", active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)

content = html.Div(id="page-content", children=[], style=CONTENT_STYLE)

app.layout = html.Div([
    dcc.Location(id="url"),
    sidebar,
    content
])


@app.callback(
    Output("page-content", "children"),
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return [
            content0
        ]
    elif pathname == "/floor1":
        return [
            firstFloor
        ]
    elif pathname == "/floor2":
        return [
            html.H1("test")
        ]
    elif pathname == "/floor3":
        return [
            html.H1("test")
        ]
    elif pathname == "/regression":
        return [
            regression
        ]

    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )


if __name__ == '__main__':
    app.run_server(debug=True, port=3000)
