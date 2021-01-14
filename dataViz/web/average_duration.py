import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px

from web.utils import nav


class AverageGenreDuration:
    """
    The AverageGenreDuration module creates a vertical bar graph which shows the most popular music genre of every year.

    """

    def __get_average_song_duration(self, songs: dict) -> pd:
        """Calculate the average song duration per genre.

        Parameters
        ----------
        songs:  dict
                The dictionary containing songs with their metadata.

        Returns
        -------
        pd
            The average genre duration dictionary converted to pandas.

        """
        genre_average_duration = dict()

        # Define default music genres to be displayed.
        genres = {"Rock": 0, "Other": 0, "Alternative": 0, "Metal": 0, "R&B": 0, "Classic": 0, "Hip-Hop": 0, "Pop": 0}

        # To retrieve the average song duration per genre, we use the operation :
        # <total genre duration> / <number of songs>.
        genre_count = genres.copy()
        genre_duration = genres.copy()

        # Count the number of songs per genre and calculate the total duration.
        for song in songs:
            if "duration" in songs[song] and "genre" in songs[song]:
                if songs[song]["genre"] in genres.keys():
                    genre_count[songs[song]["genre"]] += 1
                    genre_duration[songs[song]["genre"]] += songs[song]["duration"]
                else:
                    genre_count["Other"] += 1
                    genre_duration["Other"] += songs[song]["duration"]

        # Calculate the average song duration per genre.
        for genre in genres.keys():
            if genre_count[genre] != 0:
                genre_average_duration[genre] = float(genre_duration[genre]) / float(genre_count[genre])

        # Convert the dictionary to pandas.
        GAD = pd.concat({k: pd.Series(v) for k, v in genre_average_duration.items()}).reset_index()
        GAD.columns = ["Genre", "extra", "Average duration (seconds)"]

        return GAD

    def get_layout(self, songs):
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
        GAD = self.__get_average_song_duration(songs)

        # Display genres in an ascending order.
        duration_sort = GAD.sort_values(by="Average duration (seconds)", ascending=True)

        # Create vertical bar graph.
        fig = px.bar(
            duration_sort,
            x="Genre",
            y="Average duration (seconds)",
            color="Genre",
        )

        # Creates the dashboard.
        graph = dcc.Graph(
            id="av-dur-graph",
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
