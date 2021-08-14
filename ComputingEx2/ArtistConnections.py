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

        # return self.num_vertices
        # print(self.vertex_dict['Leon Lai'].coArtists)
        # print(self.vertex_dict['Michèle Crider'])

    def searchArtists(self, artist):
        return len(self.vertex_dict[artist].songs), sorted(
            [coArtist for coArtist in self.vertex_dict[artist].coArtists])

    def findNewFriends(self, artist_name):
        for_Given_Artist = self.searchArtists(artist=artist_name)[1]  # Mariah Carey's coArtists

        subCoArtists = []  # all coArtists of Mariah Carey's coArtists
        for coArtist in for_Given_Artist:
            # print(coArtist)
            for sub_co_artist in self.vertex_dict[coArtist].coArtists:
                # print(coArtist)
                subCoArtists.append(sub_co_artist)

        # artist that has not written (isn't a coArtist) with Mariah Carey +
        # but has written (IS a coArtist) with Mariah Carey's coArtists' coArtist
        # Of course, Mariah Carey isn't her own friend :(

        two_hop_neighbor = [Artist for Artist in self.vertex_dict.keys() if
                            Artist not in for_Given_Artist and Artist != artist_name and Artist in subCoArtists]

        return sorted(set(two_hop_neighbor))

    def recommendNewCollaborator(self, artist_name):
        for_Given_Artist = self.findNewFriends(artist_name=artist_name)  # AA's BB list
        coArtists_for_Given_Artists = self.searchArtists(artist=artist_name)[1]  # Mariah Carey's AA List
        res = []

        for songAA in coArtists_for_Given_Artists:
            if songAA in self.vertex_dict[artist_name].coArtists:
                marriah_carrey_to_aa = self.vertex_dict[artist_name].coArtists[songAA]
                for songBB in for_Given_Artist:
                    if songBB in self.vertex_dict[songAA].coArtists:
                        song_AAs_BB = self.vertex_dict[songAA].coArtists[songBB]
                        res.append([song_AAs_BB + marriah_carrey_to_aa, songBB])

        # for two_hop_artist in for_Given_Artist:
        #     for coArtist in coArtists_for_Given_Artists:
        #         if two_hop_artist in self.vertex_dict[coArtist].coArtists:
        #             res.append([self.vertex_dict[coArtist].coArtists[two_hop_artist], two_hop_artist])
        return sorted(res, reverse=True)[0]

    def shortestPath(self, artist_name):
        path = {}
        # BFS

        pass


if __name__ == '__main__':
    file = "TenKsongs_proj2.csv"
    artistGraph = ArtistConnections()
    artistGraph.loadGraph(file)
    # print(artistGraph.searchArtists("Green Day"))
    # print(artistGraph.findNewFriends("Santana"))
    print(artistGraph.recommendNewCollaborator("Santana"))
    # print(f"\nNumber of total Unique artists : {len(self.vertex_dict)}")
    # print(f"\nTotal number of total artists : {len(g.get_vertices())}")
    # print(f"Total number of edges : {len(self.vertex_dict.items())}")
    # print(f"Total of weighted edges : {len(self.vertex_dict.items())}")
