#
# Imports
#

import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

from dash.dependencies import Input, Output, State
from web.app import app
from web.navbar import nav

class Home:
    
    def get_layout(self, songs):

        columns = ["title", "artist", "album", "release_date", "genre", "publisher", "composer", "duration", "bit_rate"]
        complete = 0
        years = []
        genre = {}
        for song in songs:
            if all(i in songs[song].keys() for i in columns):
                complete += 1
            if songs[song].get("genre") not in genre:
                genre[songs[song].get("genre")] = 1  
            else:
                genre[songs[song].get("genre")] += 1
            if "release_date" in songs[song]:
                if songs[song].get("release_date") not in years:
                    years.append(songs[song].get("release_date"))

        if len(genre) >= 10:
            for element in list(genre.keys()):
                if genre[element] <= 10:
                    genre.pop(element)
        if None in genre:
            genre["Unknown"] = genre.pop(None)



        quick_stat = html.Div(
            children=[
                dbc.Alert("Music number : " + str(len(songs)) , color="primary"),
                dbc.Alert("Music number with complete data : " + str(complete) , color="success"),
                dbc.Alert("Music number with incomplete data : " + str(len(songs) - complete) , color="danger"),
                dbc.Alert("Musics date from : " + str(min(years)) + " to " + str(max(years)), color="dark"),
                dbc.Alert("Musics are from " + str(len(years)) + " different years", color="dark"),
                dbc.Alert("Musics are from " + str(len(genre)) + " different genres", color="dark"),
            ]
        )

        pie = dcc.Graph(
            id="piechart",
            figure={
                "data": [
                    {
                        "labels": list(genre.keys()),
                        "values": list(genre.values()),
                        "type": "pie",
                        "marker": {"line": {"color": "white", "width": 1}},
                        "hoverinfo": "values",
                        "textinfo": "label",
                    }
                ],
                "layout": {
                    "title": "Number of Genre",
                    "showlegend": True,
                    "autosize": True,
                },
            },
        )

        collapse = html.Div(
            [
                dbc.Button(
                    "Basic statistics",
                    id="collapse-button",
                    className="mb-3",
                    color="primary",
                ),
                dbc.Collapse(
                    quick_stat,
                    id="collapse",
                ),
            ], style={'marginTop': 50, 'textAlign': 'center',}
        )

        layout_home = html.Div(
            children=[
                nav,
                collapse,
                pie,
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

        return layout_home
