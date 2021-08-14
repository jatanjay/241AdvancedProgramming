"""
File : Vertex.py
author : jatan pandya
ece 241 : C/Project 2
references :bogotobogo.com/python_graph_data_structures.php and ZYBooks, Chapter : Python Graphs
"""


class Vertex:
    """
    class Vertex, which represents each vertex in the graph:
    """

    def __init__(self, artist):
        self.artist = artist
        self.songs = []
        self.coArtists = {}

    def __str__(self):
        return str(self.artist) + ' is connected to : ' + str([x for x in self.coArtists])

    def add_neighbor(self, neighbor, weight=0):
        self.coArtists[neighbor.artist] = weight

    def get_connections(self):
        return self.coArtists.keys()

    def get_weight(self, neighbor):
        return self.coArtists[neighbor.artist]

    def getArtistName(self):
        return self.artist

    def update_songs(self, song_title):
        return self.songs.append(song_title)
