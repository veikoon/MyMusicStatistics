#
# Imports
#

import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from web.navbar import nav

class Year:

    def getLayout(self):

        graphique = dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1900, 1950, 2008], 'y': [45, 21, 13], 'type': 'bar', 'name': 'SF'},
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

