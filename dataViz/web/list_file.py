#
# Imports
#

import dash_html_components as html
import dash_bootstrap_components as dbc
import dash_table
from web.navbar import nav


class ListFile:

    def get_layout(self, songs):
        columns = ["title", "artist", "album", "release_date", "genre", "publisher", "composer", "duration", "bit_rate"]
        tab = list()
        for key in songs.keys():
            tab.append(songs[key])

        table = dash_table.DataTable(
            data=tab,
            sort_action='native',
            id='table',
            columns=[{"name": i, "id": i} for i in columns],
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

        layout_list = html.Div([
                nav,
                table,
        ], id="list_file")

        return layout_list