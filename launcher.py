from web.index import Index
from get_metadata import GetMetadata


class Launcher:
    def run_program(self):
        #get_metadata = GetMetadata().show_info("2-06 Never Too Late.mp3")
        server = Index().run_server()