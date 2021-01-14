import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

from web.utils import nav


class PopularGenres:
    """
    The PopularGenre module creates an animated bar graph which shows the most popular music genre of every year.

    """

    def __get_popular_genres(self, songs: dict) -> pd:
        """Creates a new popular genres dictionary and converts it to pandas.

        Parameters
        ----------
        songs:  dict
                The dictionary containing songs with their metadata.

        Returns
        -------
        pd
            The popular genre dictionary converted to pandas.

        """
        sub_dict = dict()

        # Define the default music genres to be displayed on the graph.
        genres = ["Rock", "Other", "Alternative", "Metal", "R&B", "Classic", "Hip-Hop", "Pop"]

        # For each valid release date, add it to the dictionary if it isn't already there.
        for song in songs:
            if "release_date" in songs[song] and "genre" in songs[song]:
                if songs[song]["release_date"] not in sub_dict:
                    sub_dict[songs[song]["release_date"]] = dict()

        for year in sub_dict:
            # Initialize each music genre count to 0.
            for genre in genres:
                sub_dict[year][genre] = 0
            # Increment the corresponding music genre count.
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

        # Convert the dictionary to pandas.
        popular_genres = pd.concat({k: pd.Series(v) for k, v in sub_dict.items()}).reset_index()
        popular_genres.columns = ['year', 'genre', 'count']

        return popular_genres

    def get_layout(self, songs: dict) -> html.Div:
        """Creates dashboard layout.

        Parameters
        ----------
        songs:  dict
                The dictionary containing songs with their metadata.

        Returns
        -------
        html.Div
            A HTML division containing the dashboard.
        """

        popular_genres = self.__get_popular_genres(songs)

        # Display years in an ascending order.
        year_sort = popular_genres.sort_values(by="year", ascending=True)

        # Create vertical bar graph.
        fig = px.bar(
            year_sort,
            x="genre",
            y="count",
            color="genre",
            range_y=[0, 20],
            animation_frame="year",
        )

        graph = dcc.Graph(
            id='pop-genre-graph',
            figure=fig
        )

        # Group the whole layout in a single HTML division.
        layout_GAD = html.Div(
            children=[
                nav,
                graph,
            ]
        )

        return layout_GAD
