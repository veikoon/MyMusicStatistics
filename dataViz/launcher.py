import argparse

from get_metadata import Metadata
from web.index import Index


class Launcher:

    def run_program(self):

        # Argument parsing
        parser = argparse.ArgumentParser(description="Visualize song data.")
        parser.add_argument("-j", metavar="JSON File", help="source metadata from JSON file")
        args = parser.parse_args()
        source = "dataViz/assets/"
        if args.j:
            source = args.j
        metadata = Metadata()
        songs = metadata.get_songs(source)
        Index().run_server(songs)
