import eyed3

PATH = './Library/'

def show_info():
    audio = eyed3.load(PATH + "02 B.Y.O.B..mp3")
    print(audio.tag.artist)
    print(audio.tag.album)
    print(audio.tag.title)

show_info()