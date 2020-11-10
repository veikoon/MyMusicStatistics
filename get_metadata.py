import eyed3

class GetMetadata:

    def __init__(self):
        self.__PATH = './Library/'

    def show_info(self, mp3_path):
        audio = eyed3.load(self.__PATH + mp3_path)
        print(audio.tag.artist)
        print(audio.tag.album)
        print(audio.tag.title)
        print(audio.tag.release_date)
        if(audio.tag.genre != None):
            print(str(audio.tag.genre)[3:])
        print(audio.info.time_secs)
