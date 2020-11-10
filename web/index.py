#
# Imports
#

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

from web.home import layout_home
from web.list_file import layout_list
from dash.dependencies import Input, Output
from web.app import app

class Index:

    def run_server(self):
        app.layout = html.Div([
            dcc.Location(id='url', refresh=False),
            html.Div(id='page-content')
        ])

        @app.callback(
            Output('page-content', 'children'),
            [Input('url', 'pathname')],
        )
        def display_page(pathname):
            if pathname == '/home':
                return layout_home
            elif pathname == '/list':
                return layout_list
            else:
                return '404'

        app.run_server(debug=True)