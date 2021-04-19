import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from main import app
import dash_bootstrap_components as dbc

from FirstFloor import content1
from upload import data_upload

# styling the sidebar
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
                dbc.NavLink("Floor 1", href="/floor-1", active="exact"),
                dbc.NavLink("Floor 2", href="/floor-2", active="exact"),
                dbc.NavLink("upload data", href="/upload", active="exact"),
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
            html.H1('Home graph',
                    style={'textAlign': 'center'}),
        ]
    elif pathname == "/floor-1":
        return [
            content1
        ]
    elif pathname == "/floor-2":
        return [
            html.H1('consumption and cost of electricity in second floor',
                    style={'textAlign': 'center'}),

        ]
    elif pathname == "/upload":
        return [
            data_upload
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
    app.run_server(debug=True)
