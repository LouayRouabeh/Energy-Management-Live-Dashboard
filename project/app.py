import dash
import dash_bootstrap_components as dbc
from flask import Flask

server = Flask(__name__)
app = dash.Dash(__name__, server=server, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True,
                prevent_initial_callbacks=True)


app.server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False