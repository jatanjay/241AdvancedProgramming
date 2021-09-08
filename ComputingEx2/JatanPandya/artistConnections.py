"""
file : artistConnections.py
Author : Jatan Pandya
ECE 241 : Project - Computing Ex 2
"""

from graph import Graph, Queue
from SongLibrary import SongLibrary


class ArtistConnections:
    def __init__(self):
        self.g = Graph()  # the graph is stored in this

    def loadGraph(self, file_name):
        """
        loadGraph method takes the input data file name and reads the artist information.
        :param file_name:csv file name of the csv file
        :type file_name: str
        """
        g = Graph()
        songLib = SongLibrary()  # from project 1
        songLib.loadLibrary(file_name)  # loads the songs
        songLibrary = songLib.arr  # all song objects
        """
        Structure of songLibrary : list of song objects
        """
        # s = []
        for song in songLibrary:
            current_artist = song.artist
            current_song = song.title
            current_coArtists_list = song.collaborators
            # s.append(current_artist)
            for coArtist in current_coArtists_list:  # i.e. Mariah Carey's coArtist [xxxxx,xxxx,xxxx,xxxx,xxx]
                if current_artist != coArtist:
                    """
                    A check measure, few artists are listed as their own collaborators:
                    Eg : Charlie Peacock,Otis Taylor,House Of Lords,Max Melvin,Pinchers & Ganglords
                    """
                    # s.append(coArtist)

                    """
                    add edges from Mariah Carey --> coArtist
                    and since collaboration works both ways -->
                    """
                    self.g.add_edge(current_artist, coArtist, cost=1)
                    self.g.add_edge(coArtist, current_artist, cost=1)
                # update curr_song, will be used in later functions
            self.g.get_vertex(current_artist).update_songs(current_song)

        # print({song.artist: s for song, s in self.g.vert_dict['Santana'].coArtists.items()})
        # res = []
        # for song in set(s):
        #     for weight in self.g.vert_dict[song].coArtists.values():
        #         res.append(weight)
        #
        # print(len(res))
        # print(sum(res))

    def searchArtists(self, artist_name):
        """
        :param artist_name: name of artist
        :type artist_name: str
        :return: number of songs for artist_name, all coArtists
        :rtype: tuple
        """
        song_len = len(self.g.vert_dict[artist_name].songs)
        res = set([coArtist.artist for coArtist in self.g.get_vertex(artist_name).coArtists])
        coArtists = [CoArtist for CoArtist in res if CoArtist != artist_name]
        return song_len, sorted(coArtists)

    def findNewFriends(self, artist_name):
        """
        :param artist_name:----'----'----
        :type artist_name: ----'----'----
        :return: 2 hop artists (friend of friend)
        :rtype: list
        """
        givenArtistsCoArtists = self.searchArtists(artist_name)[1]  # Mariah Carey's orignal coArtists from earlier f()
        two_hops = []

        for coArtist in givenArtistsCoArtists:
            """
            create a temporary list of Mariah Carey's Collaborator
            """
            fly = self.searchArtists(coArtist)[1]
            for subCoArtist in fly:
                # MC's friend of friends
                two_hops.append(subCoArtist)

        for my_coArtists in givenArtistsCoArtists:
            """
            Its possible that some 1 hops might be in 2 hop 
            """
            if my_coArtists in two_hops:
                two_hops.remove(my_coArtists)
        two_hops = sorted(set(two_hops))
        two_hops.remove(artist_name)
        return two_hops

    def recommendNewCollaborator(self, artist_name):
        """
        :param artist_name: -----
        :type artist_name:-----
        :return: Artist name and it's "importance" i.e. song count from the weights in 2 hops
        :rtype: tuple
        """
        two_hop_artist = self.findNewFriends(artist_name)
        coArtists_for_Given_Artists = self.searchArtists(artist_name)[1]
        songs_written = {}
        """
        Following project guide lines example and terminology -->
        (mariah - y - aa + aa - x - bb = x+y)
        """
        for coArtist in coArtists_for_Given_Artists:
            curr = coArtist
            # got to do this cause g.vert_dict has vertex objects are keys, can't access aritst names
            fly = {k.artist: v for k, v in self.g.vert_dict[curr].coArtists.items()}
            for twoHopArtist in two_hop_artist:
                # BB artist
                if twoHopArtist in fly:
                    # if BB artist in One Hop's coArtist list
                    key = fly[twoHopArtist]
                    # get number of songs written, make a dict
                    if twoHopArtist in songs_written:
                        songs_written[twoHopArtist] += key
                    else:
                        songs_written[twoHopArtist] = key
        return sorted(songs_written.items(), reverse=True, key=lambda x: x[1])[0]  # artist w most counts = fit for co

    def shortestPath(self, artist_name):
        """
        :param artist_name: ----
        :type artist_name: -----
        :return: path length from artist_name to other artists
        :rtype: dict
        """
        graph = self.g
        start_vertex = artist_name
        distances = {}
        visited_list = []
        discovered_set = set()
        frontierQueue = Queue()

        frontierQueue.enqueue(start_vertex)  # first entry in Queue
        discovered_set.add(start_vertex)  # of course, starting with given artist
        distances[start_vertex] = 0

        while frontierQueue.getSize() != 0:  # since we dequeue'd, we run into exception of popping from []
            current_vertex = frontierQueue.dequeue()
            visited_list.append(current_vertex)
            for adjVertex in graph.vert_dict[current_vertex].coArtists.keys():  # all coArtists for curr_vertex/Artist
                if adjVertex.artist not in discovered_set:
                    frontierQueue.enqueue(adjVertex.artist)  # new current_vertex (next artist)
                    discovered_set.add(adjVertex.artist)
                    distances[adjVertex.artist] = distances[current_vertex] + 1  # update distance
        return distances


if __name__ == '__main__':
    file = "TenKsongs_proj2.csv"
    artistGraph = ArtistConnections()
    artistGraph.loadGraph(file)
    artist_to_search = "Mariah Carey"
    print(f'\nSearching for {artist_to_search} . . .\n{artistGraph.searchArtists(artist_to_search)}')
    print(f'\nNew friends for {artist_to_search} . . .\n{artistGraph.findNewFriends(artist_to_search)}')
    print(f'\nCollab Recommendation for {artist_to_search} . . .'
          f'\n{artistGraph.recommendNewCollaborator(artist_to_search)}')
    print(f'\nShortest Path for {artist_to_search} . . .\n{artistGraph.shortestPath(artist_to_search)}')
