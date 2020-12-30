#
# Imports
#

import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from web.navbar import nav


class AverageGenreDuration:

    def get_layout(self, songs):
        genre_average_duration = dict()
        genres = {"Rock": 0, "Other": 0, "Alternative": 0, "Metal": 0, "R&B": 0, "Classic": 0, "Hip-Hop": 0, "Pop": 0}
        genre_count = genres.copy()
        genre_duration = genres.copy()

        for song in songs:
            if "duration" in songs[song] and "genre" in songs[song]:
                if songs[song]["genre"] in genres.keys():
                    genre_count[songs[song]["genre"]] += 1
                    genre_duration[songs[song]["genre"]] += songs[song]["duration"]
                else:
                    genre_count["Other"] += 1
                    genre_duration["Other"] += songs[song]["duration"]

        for genre in genres.keys():
            genre_average_duration[genre] = float(genre_duration[genre]) / float(genre_count[genre])

        GAD = pd.concat({k: pd.Series(v) for k, v in genre_average_duration.items()}).reset_index()
        GAD.columns = ["Genre", "extra", "Average duration (seconds)"]
        duration_sort = GAD.sort_values(by="Average duration (seconds)", ascending=True)

        fig = px.bar(
            duration_sort,
            x="Genre",
            y="Average duration (seconds)",
            color="Genre",
        )

        graph = dcc.Graph(
            id="av-dur-graph",
            figure=fig
        )

        layout_GAD = html.Div(
            children=[
                nav,
                graph,
            ]
        )

        return layout_GAD
