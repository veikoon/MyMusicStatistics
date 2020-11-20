#
# Imports
#

import dash_core_components as dcc
import dash_html_components as html

from dataViz.web.home import layout_home
from dataViz.web.list_file import layout_list
from dataViz.web.year import layout_year
from dash.dependencies import Input, Output
from dataViz.web.app import app

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
            if pathname == '/':
                return layout_home
            elif pathname == '/list':
                return layout_list
            elif pathname == '/year':
                return layout_year
            else:
                return '404'

        app.run_server(debug=True)