#from web.index import Index
from get_metadata import GetMetadata
import argparse


class Launcher:

    def run_program(self):
        """
        Index().run_server()
        """

        # Argument parsing
        parser = argparse.ArgumentParser(description="Visualize song data.")
        parser.add_argument("-j", metavar="JSON File", help="source metadata from JSON file")
        args = parser.parse_args()
        source = "dataViz/Library/"
        if args.j:
            source = args.j
        get_metadata = GetMetadata()
        songs = get_metadata.get_songs(source)
        print(songs)
