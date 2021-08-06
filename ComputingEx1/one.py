"""
Jatan Pandya
Prof. Arman Pouraghily / ECE241
C1 / Project 1
31 Jul '21
"""

"""
Manage your data in Python classes and objects. For example, define two classes, Song
and SongLibrary. You will use one instance of the Song class for each song and one
instance of the SongLibrary class for your song library.
"""

# from avl import Node, AVLTree

# from partition import quickS

# import csv
# import random
# from partition import partition
# import time


import csv
import random
import time
import math

from sort_quick import quickS
from avl import AVLTree
from Node import Node
from Song import Song


class SongLibrary:
    def __init__(self):
        self.song_array = []
        self.library_size = 0
        self.library_isSorted = False
        self.BST = None
        self.bst_buildTime = 0
        self.bst_runtime = float()
        self.linear_runtime = float()

    def loadLibrary(self, file_name):
        """
        This method takes the input data file name, opens it, and loads the songs in the file into the library.
        Order of the songs is retained
        :param file_name: name of the csv file
        :type file_name: .csv file
        :return: list containing objects of songs
        :rtype: list
        """

        with open(file=file_name, mode="r", encoding="utf-8") as csv_file:
            reader = csv.reader(csv_file, skipinitialspace=True)
            for song_detail in reader:
                # print(song_detail)
                # print(type(song_detail))
                self.song_array.append(Song(song_detail))
                self.library_size += 1

        # j = 1
        # r = (self.song_array[:5])
        # for i in r:
        #     print(i.title)

    def quickSort(self):
        """
        Quick sort algorithm to sort the song database based on the song title
        Once sorted --> the status of the Boolean variable is changed
        :return:
        :rtype:
        """
        arr = self.song_array
        quickS(arr, 0, self.library_size - 1)
        self.library_isSorted = True

        # j = 1
        # r = (self.song_array[:5])
        # for i in r:
        #     print(i.title)

    def linearSearch(self, query, attribute):
        """
        linear search algorithm to search the songs based on either song title or artist.
        Returns the number of the songs found in the song array that satisfies.
        The search function has two parameters : query and attribute
        :param query: search by query / example : title of a song or the name of an artist
        :type query: str
        :param attribute: search by attr ('title' or 'artist')
        :type attribute: str
        :return: number of songs that satisfy
        :rtype: int
        """

        song_count = 0

        if attribute.lower() == "artist":
            for song in range(len(self.song_array)):
                if self.song_array[song].artist == query:
                    song_count += 1

        if attribute.lower() == "title":
            for song in range(len(self.song_array)):
                if self.song_array[song].title == query:
                    song_count += 1

        if song_count:
            return song_count
        # else:
        #     return "Not Found!"

    def BSTree(self):
        self.BST = AVLTree()
        start = time.time()
        for song in self.song_array:
            node = Node(song.title)
            self.BST.insert(node)
        end = time.time()
        self.bst_buildTime = end - start
        print(f"\nIt took {self.bst_buildTime} to build BST")

        if self.BST.root:
            return print(self.BST.root.getHeight())
        else:
            return 0

    def printBST(self):
        # print(self.BST)
        print(self.BST)

    def searchBST(self, query):
        curr_root = self.BST.root
        while curr_root is not None:

            try:
                if curr_root.key == query:
                    return curr_root.key

                if curr_root.key > query:
                    curr_root = curr_root.left
                else:
                    curr_root = curr_root.right

            except AttributeError:
                return None

    def random_songs(self):
        """
        Uses a random number generator (uniform distribution) to select 100 song titles arbitrarily.
        Saves them in a list.
        :return:
        :rtype:
        """

        songs_random = random.sample(self.song_array, k=100)
        songs_random = [song_obj.title for song_obj in songs_random]
        return songs_random

    def performSearches(self):
        """
        Performs all required searches in the sorted database for those 100
        songs. Record the total time spent on the linear searches.
        """
        random_songs = self.random_songs()
        print()
        print(random_songs[:5])

        linear_start = time.time()
        for song_title in random_songs:
            self.linearSearch(query=song_title, attribute="title")
        linear_end = time.time()
        self.linear_runtime = linear_end - linear_start
        print(
            f"\nLinear Search took a total of {self.linear_runtime} secs for 100 Random Songs"
        )

        bst_start = time.time()
        for song_title in random_songs:
            self.searchBST(query=song_title)
        bst_end = time.time()
        self.bst_runtime = bst_end - bst_start
        print(
            f"\nBinary Search took a total of {self.bst_runtime} secs for 100 Random Songs"
        )

    def calculations(self):
        print(self.bst_runtime)
        print(self.linear_runtime)
        print(self.bst_buildTime)

        # n * (linear_runtime / 100)  > bst_buildTime + bst_runtime
        # n > (bst_buildTime + bst_runtime) / (linear_runtime / 100)
        n = (self.bst_buildTime + self.bst_runtime) / self.linear_runtime
        print("n:", n)
        # print(math.floor(n))
        print(math.floor(n))


if __name__ == "__main__":
    file = "TenKsongs.csv"
    SongLib = SongLibrary()
    loaded_library = SongLib.loadLibrary(file)

    # with open(file, 'r') as c:
    #     r = csv.reader(c)
    #     k = 0
    #     for j in r:
    #         test = Song(trial_song=j)
    #         test.display()

    # print(SongLib.linearSearch('Bob Dylan', 'artist'))
    # print(SongLib.linearSearch('A Boy Named Sue', 'title'))
    # print(SongLib.linearSearch('Fake Song', 'title'))
    # SongLib.searchBST("""Hard Rain's Gonna Fall""")

    SongLib.quickSort()
    SongLib.BSTree()
    # SongLib.printBST()

    # SongLib.performSearches()
    # SongLib.calculations()

    # res = []
    # for i in range(100):
    #     SongLib.quickSort()
    #     SongLib.BSTree()
    #     # SongLib.printBST()
    #     SongLib.performSearches()
    #     res.append(SongLib.calculations())
    # print(res)
    # print(sum(res)/len(res))
    # 1.27, 1.5, 1.something
"""
1. average time? that is for each search, append in res? or total 100 searchers? that is avg_linear / 100
2. 
"""
