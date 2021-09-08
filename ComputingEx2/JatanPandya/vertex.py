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
        return str(self.artist) + ' is connected to : ' + str([x.artist for x in self.coArtists])

    def add_neighbor(self, neighbor, cost=0):
        if neighbor in self.coArtists:
            # if Nick Ingman in Leon Lai's CoArtist, +1 to their collabCount
            self.coArtists[neighbor] += 1
        else:
            # sweet, start with their collabCount
            self.coArtists[neighbor] = 1

    def get_connections(self):
        return self.coArtists.keys()

    def get_weight(self, neighbor):
        return self.coArtists[neighbor]

    def getArtistName(self):
        return self.artist

    def getName(self):
        return self.artist

    def update_songs(self, song_title):
        """
        appends curr song to self.songs
        :param song_title: curr_song
        :type song_title: str
        """
        return self.songs.append(song_title)
