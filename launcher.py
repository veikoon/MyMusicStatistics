from web.index import Index
from get_metadata import GetMetadata


class Launcher:
    def run_program(self):
        get_metadata = GetMetadata()
        songs = get_metadata.get_songs()
        print(songs)
        Index().run_server()
