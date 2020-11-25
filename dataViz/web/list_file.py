#
# Imports
#

import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
from dash.dependencies import Input, Output, State

from web.navbar import nav
from web.app import app
from get_metadata import GetMetadata

class ListFile:

    def get_layout(self, songs):
        keys = []
        for keys,values in songs.items():
            keys = values.keys()

        tab = list()
        for key in songs.keys():
            tab.append(songs[key])

        table = dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in keys],
            style_cell={'textAlign': 'center'},
            data=tab,
        )

        collapse = html.Div(
            [
                dbc.Button(
                    "Open collapse",
                    id="collapse-button",
                    className="mb-3",
                    color="primary",
                ),
                dbc.Collapse(
                    table,
                    id="collapse",
                ),
            ]
        )

        layout_list = html.Div(
            children=[
                nav,
                collapse,
            ]
        )

        @app.callback(
            Output("collapse", "is_open"),
            [Input("collapse-button", "n_clicks")],
            [State("collapse", "is_open")],
        )
        def toggle_collapse(n, is_open):
            if n:
                return not is_open
            return is_open

        return layout_list