import eyed3
import os
import re


class GetMetadata:

    def __init__(self):
        #self.__PATH = './Library/'
        self.__PATH = '../../../../Musique/'

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
                if key == "genre":
                    if value is None:
                        temp_song.pop(key)
                    else:
                        temp_song["genre"] = str(song.tag.genre).lstrip("()0123456789")
                if key == "bit_rate":
                    if value is None:
                        temp_song.pop(key)
                    else:
                        temp_song["bit_rate"] = int(str(list(map(int, re.findall("\d+", temp_song["bit_rate"])))).strip("[]"))
                if key == "release_date":
                    if value is None:
                        temp_song.pop(key)
                    else:
                        temp_song["release_date"] = int(str(temp_song["release_date"]))
                if temp_song["album"] == "[non-album tracks]":
                    if value is None:
                        temp_song.pop(key)
                    else:
                        temp_song["album"] = "Single"
            songs[song.tag.title] = temp_song

        return songs
