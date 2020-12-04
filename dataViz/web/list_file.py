#
# Imports
#

import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
from dash.dependencies import Input, Output, State
from web.navbar import nav
from web.app import app


class ListFile:

    def get_layout(self, songs):
        collumns = songs.get("exemple").keys()

        tab = list()
        for key in songs.keys():
            tab.append(songs[key])

        table = dash_table.DataTable(
            data=tab,
            sort_action='native',
            id='table',
            columns=[{"name": i, "id": i} for i in collumns],
            fixed_rows={'headers': True},
            style_table={
                'maxHeight': '50ex',
                'width': '100%',
                'minWidth': '100%',
                "height": "80vh", "maxHeight": "80vh"
            },
            style_header={'backgroundColor': 'rgb(0, 123, 255)'},
            style_cell={
                            'textAlign': 'center',
                            'overflow': 'hidden',
                            'textOverflow': 'ellipsis',
                            'maxWidth': 0,
                        },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(248, 248, 248)'
                }
            ],
        )

        #collapse = html.Div(
        #    [
        #        dbc.Button(
        #            "Open collapse",
        #            id="collapse-button",
        #            className="mb-3",
        #            color="primary",
        #        ),
        #        dbc.Collapse(
        #            table,
        #            id="collapse",
        #        ),
        #    ]
        #)
        layout_list = html.Div([
                nav,
                table,
        ], id="list_file")

        #@app.callback(
        #    Output("collapse", "is_open"),
        #    [Input("collapse-button", "n_clicks")],
        #    [State("collapse", "is_open")],
        #)
        #def toggle_collapse(n, is_open):
        #    if n:
        #        return not is_open
        #    return is_open

        return layout_list