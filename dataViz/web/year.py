#
# Imports
#

import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from web.navbar import nav

class Year:

    def get_layout(self, songs):

        sub_dict = dict()
        for song in songs:
            if "release_date" in songs[song]:
                if songs[song]["release_date"] not in sub_dict:
                    sub_dict[songs[song]["release_date"]] = 0
                for year in sub_dict:
                    if year == songs[song]["release_date"]:
                        sub_dict[year] += 1

        graphique = dcc.Graph(
            id='example-graph',
            figure={
                'data': [
                    {'x': list(sub_dict.keys()), 'y': list(sub_dict.values()), 'type': 'bar', 'name': 'SF'},
                ],
                'layout': {
                    'title': 'Dash Data Visualization'
                }
            }
        )
        layout_year = html.Div(
            children=[
                nav,
                graphique,
            ]
        )

        return layout_year

