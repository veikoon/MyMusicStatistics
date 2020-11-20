import eyed3
import os

class GetMetadata:

    def __init__(self):
        self.__PATH = './Library/'

    def get_songs(self):
        songs = dict()
        for filename in os.listdir(self.__PATH):
            if not filename.endswith(".mp3"):
                pass
            song = eyed3.load(self.__PATH + filename)
            songs[song.tag.title] = {"artist": song.tag.artist,
                                     "album": song.tag.album,
                                     "release_date": str(song.tag.release_date),
                                     "genre": song.tag.genre,
                                     "publisher": song.tag.publisher,
                                     "composer": song.tag.composer}
            temp_song = songs[song.tag.title].copy()
            for key, value in songs[song.tag.title].items():
                if value is None:
                    temp_song.pop(key)
                elif key == "genre":
                    temp_song["genre"] = str(song.tag.genre).lstrip("()0123456789")
                elif temp_song["album"] == "[non-album tracks]":
                    temp_song["album"] = "Single"
            songs[song.tag.title] = temp_song

        return songs
