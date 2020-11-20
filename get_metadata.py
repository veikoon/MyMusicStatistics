import eyed3
import os
import re


class GetMetadata:

    def __init__(self):
        self.__PATH = './Library/'

    def get_songs(self):
        songs = dict()
        for filename in os.listdir(self.__PATH):
            if not filename.endswith(".mp3"):
                pass
            song = eyed3.load(self.__PATH + filename)
            songs[song.tag.title] = {"title": song.tag.title,
                                     "artist": song.tag.artist,
                                     "album": song.tag.album,
                                     "release_date": song.tag.release_date,
                                     "genre": song.tag.genre,
                                     "publisher": song.tag.publisher,
                                     "composer": song.tag.composer,
                                     "duration": round(float(str(song.info.time_secs)), 2),
                                     "bit_rate": song.info.bit_rate_str}
            temp_song = songs[song.tag.title].copy()
            for key, value in songs[song.tag.title].items():
                if value is None:
                    temp_song.pop(key)
                elif key == "genre":
                    temp_song["genre"] = str(song.tag.genre).lstrip("()0123456789")
                elif key == "bit_rate":
                    temp_song["bit_rate"] = int(str(list(map(int, re.findall("\d+", temp_song["bit_rate"])))).strip("[]"))
                elif key == "release_date":
                    temp_song["release_date"] = int(str(temp_song["release_date"]))
                elif temp_song["album"] == "[non-album tracks]":
                    temp_song["album"] = "Single"
            songs[song.tag.title] = temp_song

        return songs
