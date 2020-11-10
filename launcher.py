from server import Server
from get_metadata import GetMetadata


class Launcher:
    def run_program(self):
        get_metadata = GetMetadata()
        get_metadata.show_info("02 B.Y.O.B..mp3")
        server = Server()
        server.run_server()