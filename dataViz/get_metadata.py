import eyed3
import os
import re
import json
from json import JSONDecodeError
import codecs


class GetMetadata:

    def __get_json_songs(self, file_name):
        try:
            file = codecs.open(file_name, "r", "utf8")
        except IOError:
            raise RuntimeError("Could not find source file : \"{}\".".format(file_name))
        else:
            try:
                songs = json.load(file, encoding="latin-1")
                file.close()
                return songs
            except JSONDecodeError:
                raise RuntimeError("JSON file contains errors.")

    def __generateExemple(self):
        return {
                    "title":"exemple",
                    "artist":"John Smith",
                    "album":"Anonyme",  
                    "release_date":2000,
                    "genre":"Classic",
                    "publisher":"Esiee",
                    "composer":"Esiee",
                    "duration":200.00,
                    "bit_rate":320
                }

    def __get_file_songs(self, source):
        songs = dict()
        songs["exemple"] = self.__generateExemple()
        for filename in os.listdir(source):
            print(filename)
            if filename.endswith(".mp3"):
                song = eyed3.load(source + filename)
                if song is not None and song.tag is not None and song.tag.title is not None:
                    songs[song.tag.title] = {
                                "title": song.tag.title,
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
                            try:
                                temp_song["release_date"] = int(str(temp_song["release_date"]))
                            except:
                                temp_song.pop(key)
                        elif key == "album" and temp_song["album"] == "[non-album tracks]":
                            temp_song["album"] = "Single"
                    songs[song.tag.title] = temp_song
        return songs

    def get_songs(self, source):
        if source.endswith(".json"):
            return self.__get_json_songs(source)
        else :
            return self.__get_file_songs(source)
