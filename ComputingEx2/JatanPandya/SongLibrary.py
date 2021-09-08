"""
file : songlibrary.py
stuff from c1, helps load songs
"""


class SongLibrary:
    def __init__(self):
        self.arr = []

    def loadLibrary(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as fOut:
            line_read = fOut.readlines()
            for line in line_read:
                self.arr.append(Song(line))
        fOut.close()


class Song:
    def __init__(self, song_detail):
        chunk = song_detail.split(',')
        self.title = chunk[1]
        self.artist = chunk[2]
        self.collaborators = chunk[5][:len(chunk[5]) - 1].split(';')
