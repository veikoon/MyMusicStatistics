#
# Imports
#

import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from web.navbar import nav


class PopularGenres:

    def get_layout(self, songs):
        sub_dict = dict()
        genres = list()
        for song in songs:
            if "release_date" in songs[song] and "genre" in songs[song]:
                if songs[song]["release_date"] not in sub_dict:
                    sub_dict[songs[song]["release_date"]] = dict()
                if songs[song]["genre"] not in genres:
                    genres.append(songs[song]["genre"])

        for year in sub_dict:
            for genre in genres:
                sub_dict[year][genre] = 0
            for song in songs:
                if "release_date" in songs[song] and "genre" in songs[song]:
                    if year == songs[song]["release_date"]:
                        sub_dict[year][songs[song]["genre"]] += 1


        popular_genres = pd.concat({k: pd.Series(v) for k, v in sub_dict.items()}).reset_index()
        popular_genres.columns = ['year', 'genre','count']
        year_sort = popular_genres.sort_values(by="year", ascending=True)

        fig = px.bar(
            year_sort,
            x="genre",
            y="count",
            animation_frame="year",
        )

        graphique = dcc.Graph(
            id='example-graph',
            figure=fig
        )

        layout_year = html.Div(
            children=[
                nav,
                graphique,
            ]
        )

        return layout_year
