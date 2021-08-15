"""
file : ArtistConnections.py
Author : Jatan Pandya
ECE 241 : Project - Computing Ex 2
"""

import csv

from Graph import Graph
from Vertex import Vertex


class ArtistConnections:
    def __init__(self):
        self.g = Graph()

    def loadGraph(self, file_name):
        """
        loadGraph method takes the input data file name and reads the artist information.
        :param file_name:
        :type file_name:
        """
        all_artists = []
        with open(file=file_name, mode="r", encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file)
            for song_detail in reader:
                song_artist = song_detail[2]
                song_title = song_detail[1]
                coArtist_list = song_detail[5].split(";")
                all_artists.append(song_artist)

                if song_artist not in self.g.vert_dict:
                    self.g.add_vertex(song_artist)
                    current_artist_vertex = Vertex(song_artist)

                for coArtist in coArtist_list:
                    self.g.add_edge(song_artist, coArtist, 1)
                    current_artist_vertex.add_neighbor(coArtist, 1)

        # print(self.g.get_vertex('Leon Lai'))
        # for a in all_artists:
        #     m, h = self.findNewFriends(a)
        #     if m != h:
        #         print(m, h, a)

    def searchArtists(self, artist):

        song_len = len(self.g.vert_dict[artist].songs)
        collabArtists = [coArtist.artist for coArtist in self.g.get_vertex(artist).coArtists]
        collabArtists = [CoArtist for CoArtist in collabArtists if CoArtist != artist]

        return song_len, sorted(set(collabArtists))

    def findNewFriends(self, artist_name):

        givenArtists_collab = self.searchArtists(artist_name)[1]
        two_hops = []

        for coArtist in givenArtists_collab:
            fly = self.searchArtists(coArtist)[1]
            for subCoArtist in fly:
                two_hops.append(subCoArtist)

        for my_coArtists in givenArtists_collab:
            if my_coArtists in two_hops:
                two_hops.remove(my_coArtists)
        two_hops = sorted(set(two_hops))
        two_hops = [artist for artist in two_hops if artist != artist_name]

        return two_hops

    def recommendNewCollaborator(self, artist_name):
        two_hop_artist = self.findNewFriends(artist_name)
        coArtists_for_Given_Artists = self.searchArtists(artist_name)[1]
        res = []


if __name__ == '__main__':
    file = "TenKsongs_proj2.csv"
    artistGraph = ArtistConnections()
    artistGraph.loadGraph(file)
    # print(artistGraph.searchArtists("Santana"))
    # print(artistGraph.findNewFriends("Santana"))
    # print(artistGraph.recommendNewCollaborator("Green Day"))
    # print(artistGraph.shortest_path("Mariah Carey"))
