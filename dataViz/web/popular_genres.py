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
        genres = ["Rock", "Other", "Alternative", "Metal", "R&B", "Classic", "Hip-Hop", "Pop"]
        for song in songs:
            if "release_date" in songs[song] and "genre" in songs[song]:
                if songs[song]["release_date"] not in sub_dict:
                    sub_dict[songs[song]["release_date"]] = dict()

        for year in sub_dict:
            for genre in genres:
                sub_dict[year][genre] = 0
            for song in songs:
                if "release_date" in songs[song] and "genre" in songs[song]:
                    if year == songs[song]["release_date"]:
                        increment_other = True
                        for genre in genres:
                            if genre in songs[song]["genre"]:
                                sub_dict[year][genre] += 1
                                increment_other = False
                                break
                        if increment_other:
                            sub_dict[year]["Other"] += 1

        popular_genres = pd.concat({k: pd.Series(v) for k, v in sub_dict.items()}).reset_index()
        popular_genres.columns = ['year', 'genre', 'count']
        year_sort = popular_genres.sort_values(by="year", ascending=True)

        fig = px.bar(
            year_sort,
            x="genre",
            y="count",
            color="genre",
            range_y=[0,50],
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
