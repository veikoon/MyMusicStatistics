import eyed3

PATH = './Library/'

def show_info(mp3_path):
    audio = eyed3.load(PATH + mp3_path)
    print(audio.tag.artist)
    print(audio.tag.album)
    print(audio.tag.title)
    print(audio.tag.release_date)
    if(audio.tag.genre != None):
        print(str(audio.tag.genre)[3:])
    print(audio.info.time_secs)

show_info("2-06 Never Too Late.mp3")
show_info("02 B.Y.O.B..mp3")