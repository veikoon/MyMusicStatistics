#
# Imports
#

import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px

from web.navbar import nav

class Year:

    def getLayout():
        songs = {'Starlight':{'release_date':'2005'}, 'Never Too Late':{'release_date':'2008'}, 'Tear in My Heart':{'release_date':'2002'},}
        year = []
        index = [1,2,3]
        for element in songs:
            year.append(songs[element]['release_date'])

        fig = px.scatter(x=index, y=year)

        layout_year = html.Div(
            children=[
                nav,
                dcc.Graph(figure=fig),
            ]
        )

        return layout_year

