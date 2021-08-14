"""
file : ArtistConnections.py
Author : Jatan Pandya
ECE 241 : Project - Computing Ex 2
"""

import csv

from Graph import Graph


# from Song_SongLib import Song,SongLibrary
# from Vertex import Vertex
# from Graph import Graph

class ArtistConnections:
    def __init__(self):
        self.vertex_dict = {}

    def loadGraph(self, file_name):
        """
        loadGraph method takes the input data file name and reads the artist information.
        :param file_name:
        :type file_name:
        """
        g = Graph()
        t_art = []
        count = 0
        with open(file=file_name, mode="r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file)
            for song_detail in reader:
                count += 1
                song_artist = song_detail[2]
                song_title = song_detail[1]
                coArtist_list = song_detail[5].split(";")
                t_art.append(song_artist)
                if song_artist not in self.vertex_dict:
                    self.vertex_dict[song_artist] = g.add_vertex(song_artist)

                if song_artist in self.vertex_dict:
                    self.vertex_dict[song_artist].update_songs(song_title)
                    for coArtist in coArtist_list:
                        if coArtist in self.vertex_dict[song_artist].coArtists.keys():
                            g.add_edge(song_artist, coArtist, self.vertex_dict[song_artist].coArtists[coArtist] + 1)
                        if coArtist not in self.vertex_dict[song_artist].coArtists.keys():
                            g.add_edge(song_artist, coArtist, 1)

        # print(f"\nNumber of total Unique artists : {len(self.vertex_dict)}")
        # print(f"\nTotal number of total artists : {len(g.get_vertices())}")
        #
        # print(self.vertex_dict['Leon Lai'].coArtists)
        # print(self.vertex_dict)
        # print(self.vertex_dict['Leon Lai'])
        # print(self.vertex_dict['Leon Lai'].coArtists)

        r = []
        for a in t_art:
            for val in self.vertex_dict[a].coArtists.values():
                # r.append(len(self.vertex_dict[a].coArtists))
                r.append(val)

        print(len(r))
        print(sum(r))


# print(f"Total number of edges : {len(self.vertex_dict.items())}")
# print(f"Total of weighted edges : {len(self.vertex_dict.items())}")


def searchArtists(self, artist):
    return len(self.vertex_dict[artist].songs), sorted(
        [coArtist for coArtist in self.vertex_dict[artist].coArtists])


if __name__ == '__main__':
    file = "TenKsongs_proj2_test.csv"
    artistGraph = ArtistConnections()
    artistGraph.loadGraph(file)
    # print(artistGraph.searchArtists("Mariah Carey"))
