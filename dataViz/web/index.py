#
# Imports
#

import dash_core_components as dcc
import dash_html_components as html

from web.home import Home
from web.list_file import ListFile
from web.year import Year
from web.popular_genres import PopularGenres
from dash.dependencies import Input, Output
from web.app import app

class Index:

    def run_server(self, songs):

        liste = ListFile()
        home = Home()
        year = Year()
        popular_genres = PopularGenres()

        layout_list = liste.get_layout(songs)
        layout_home = home.get_layout()
        layout_year = year.get_layout(songs)
        layout_popular_genres = popular_genres.get_layout(songs)

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
            elif pathname == '/popular_genres':
                return layout_popular_genres
            else:
                return '404'

        app.run_server(debug=True)