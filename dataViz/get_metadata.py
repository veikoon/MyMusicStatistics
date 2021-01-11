import codecs
import json
import os
import re
from json import JSONDecodeError

import eyed3
from pprint import pprint


class Metadata:
    """
    The Metadata module retrieves song data from a JSON file or extracts them from mp3 files in a provided directory.

    """

    def __get_json_songs(self, file_name: str) -> dict:
        """Retrieve songs dictionary from a JSON file.

        Parameters
        ----------
        file_name:  str
                    The name of the JSON file containing all song information.

        Returns
        -------
        dict
            A dictionary containing songs with their respective metadata.

        Raises
        ------
        RuntimeError
            If JSON file can't be found or if it contains errors.

        """
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
    """
    def __generateExample(self):
        return {
                    "title": "example",
                    "artist": "John Smith",
                    "album": "Anonymous",
                    "release_date": 2000,
                    "genre": "Classic",
                    "publisher": "ESIEE",
                    "composer": "ESIEE",
                    "duration": 200.00,
                    "bit_rate": 320
                }
    """
    def __get_file_songs(self, source):
        """Retrieve songs dictionary from mp3 files.

        Parameters
        ----------
        source: str
                The name of the directory containing all mp3 files.

        Returns
        -------
        dict
            A dictionary containing songs with their respective metadata.

        Raises
        ------
        RuntimeError
            If JSON file can't be found or if it contains errors.

        """
        songs = dict()
        for filename in os.listdir(source):
            if filename.endswith(".mp3"):
                song = eyed3.load(source + filename)

                if song is not None and song.tag is not None and song.tag.title is not None:
                    # Define all possible dictionary keys.
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
                        # Remove key if the value is empty.
                        if value is None:
                            temp_song.pop(key)

                        # Format the "genre" key value and convert it to a string.
                        elif key == "genre":
                            temp_song["genre"] = str(song.tag.genre).lstrip(".()0123456789")

                        # Convert the "bit_rate" key value to an integer.
                        elif key == "bit_rate":
                            temp_song["bit_rate"] = int(str(list(map(int, re.findall("\d+", temp_song["bit_rate"]))))
                                                        .strip("[]"))

                        # Make sure the year is an integer.
                        elif key == "release_date":
                            temp_song["release_date"] = int(str(temp_song["release_date"]))

                        # Set "album" key to "single" if needed.
                        elif key == "album" and temp_song["album"] == "[non-album tracks]":
                            temp_song["album"] = "Single"
                    songs[song.tag.title] = temp_song
        return songs

    def get_songs(self, source):
        """Retrieve songs dictionary.

        Parameters
        ----------
        source: str
                The name of the directory containing all mp3 files.

        Returns
        -------
        dict
            A dictionary containing songs with their respective metadata.

        """
        if source.endswith(".json"):
            return self.__get_json_songs(source)
        else:
            return self.__get_file_songs(source)
