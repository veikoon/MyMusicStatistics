import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from web.app import app
from web.average_duration import AverageGenreDuration
from web.home import Home
from web.list_file import ListFile
from web.popular_genres import PopularGenres
from web.year import Year


class Index:
    """The Index module acts as a web hub where it is decided when and where to display dashboards.

    """

    def run_server(self, songs: dict) -> None:
        """Runs server and configures URL redirections.

        Parameters
        ----------
        songs:      dict
                    The dictionary containing songs with their metadata.

        """
        # Retrieve dashboard layouts.
        file_list = ListFile()
        home = Home()
        year = Year()
        popular_genres = PopularGenres()
        GAD = AverageGenreDuration()

        layout_list = file_list.get_layout(songs)
        layout_home = home.get_layout()
        layout_year = year.get_layout(songs)
        layout_popular_genres = popular_genres.get_layout(songs)
        layout_GAD = GAD.get_layout(songs)

        app.layout = html.Div([
            dcc.Location(id='url', refresh=False),
            html.Div(id='page-content')
        ])

        @app.callback(
            Output('page-content', 'children'),
            [Input('url', 'pathname')],
        )
        def display_page(pathname) -> html.Div:
            """Configure URL redirection.

            Parameters
            ----------
            pathname:   str
                        Path to be added to the URL.

            Returns
            -------
            html.Div
                A HTML division containing the dashboard.

            """
            if pathname == '/':
                return layout_home
            elif pathname == '/list':
                return layout_list
            elif pathname == '/year':
                return layout_year
            elif pathname == '/popular_genres':
                return layout_popular_genres
            elif pathname == '/average_genre_duration':
                return layout_GAD
            else:
                return '404'

        app.run_server()
