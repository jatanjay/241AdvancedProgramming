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

import csv
import random
import time

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
        self.bst_buildTime = float()
        self.bst_runtime = float()
        self.linear_runtime = float()
        self.size_k = 100

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
            reader = csv.reader(csv_file)
            for song_detail in reader:
                self.song_array.append(Song(song_detail))
                self.library_size += 1

        array = self.song_array[:5]
        print("\nFirst Five Songs in the CSV: ")
        print("------------------------------------------")
        for s in array:
            print(s.title)

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

        res = self.song_array[:5]
        print("\nFirst five songs of the Sorted Array: ")
        print("------------------------------------------")
        for song in res:
            print(song.title)

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
            return f"Song {attribute} : {query} --> Total Count :: {song_count}"
        else:
            return f"Song {attribute} : {query} --> Not Found!"

        # if song_count:
        #     return song_count"
        # else:
        #     return None

    def BSTree(self):
        self.BST = AVLTree()
        start = time.time()
        for song in self.song_array:
            node = Node(song.title)
            self.BST.insert(node)
        end = time.time()
        self.bst_buildTime = end - start
        print(f"It took {self.bst_buildTime} seconds to build the BST")
        print(f"The height of the BST is:", self.BST.root.getHeight())

    def printBST(self):
        print(self.BST)

    def searchBST(self, query):
        curr_root = self.BST.root
        while curr_root is not None:
            if curr_root.key == query:
                return True
            if curr_root.key > query:
                curr_root = curr_root.left
            else:
                curr_root = curr_root.right
        return False

    def random_songs(self):
        """
        Uses a random number generator (uniform distribution) to select 100 song titles arbitrarily.
        Saves them in a list.
        :return:
        :rtype:
        """

        songs_random = random.sample(self.song_array, k=self.size_k)
        songs_random = [song_obj.title for song_obj in songs_random]
        return songs_random

    def performSearches(self):
        """
        Performs all required searches in the sorted database for those 100
        songs. Record the total time spent on the linear searches.
        """

        '''
        ALL EYEZ ON ME :::::::::: SEE YOU GOTTA SORT !!!!
        '''
        random_songs = self.random_songs()
        print(f"5 random songs : {random_songs[:5]}")
        print(f"{sorted(random_songs[:5])}")

        linear_start = time.time()
        for song_title in random_songs:
            self.linearSearch(query=song_title, attribute="title")
        linear_end = time.time()
        self.linear_runtime = linear_end - linear_start
        print(
            f"Linear Search took a total of {self.linear_runtime} secs for {self.size_k} Random Song titles"
        )

        bst_start = time.time()
        for song_title in random_songs:
            self.searchBST(query=song_title)
        bst_end = time.time()
        self.bst_runtime = bst_end - bst_start
        print(
            f"Binary Search took a total of {self.bst_runtime} secs for {self.size_k} Random Song titles"
        )

        return self.linear_runtime, self.bst_buildTime

    def calculations(self):
        # bst_time = self.performSearches()
        # print("\nAt a glance:")
        # print("------------------------------------------")
        # print("To BST search : ", self.bst_runtime)
        # print("To Linear Search: ", self.linear_runtime)
        # print("To Build BST:", self.bst_buildTime)

        # # n > ( MakingBSTtime + BST(n))  / LinearSearchTime(n) / 100
        #
        # rhs = (self.bst_buildTime + res[0]) / res[1] / 100
        #
        # print(rhs)
        print(self.bst_buildTime)
        rhs = (self.bst_buildTime + self.bst_runtime) / (self.linear_runtime / self.size_k)
        return rhs


if __name__ == "__main__":

    file = "TenKsongs.csv"
    print("\nContents of the CSV file:")
    print("------------------------------------------")
    with open(file, 'r') as c:
        r = csv.reader(c)
        for j in r:
            test = Song(trial_song=j)
        test.display()

    SongLib = SongLibrary()
    loaded_library = SongLib.loadLibrary(file)

    # print("\nLinear Search Test:")
    # print("------------------------------------------")
    # print(SongLib.linearSearch('Bob Dylan', 'artist'))
    # print(SongLib.linearSearch('A Boy Named Sue', 'title'))
    # print(SongLib.linearSearch('Fake Song', 'title'))
    # print(SongLib.linearSearch('Jatan Pandya', 'artist'))

    SongLib.quickSort()

    # print("\nBST:")
    # print("------------------------------------------")
    SongLib.BSTree()
    # print("\nPrinted BST")
    # SongLib.printBST()
    # print(SongLib.searchBST("A hard Rain's gonna fall"))
    # print(SongLib.searchBST("New Pony"))

    print("\nSearches:")
    print("------------------------------------------")
    SongLib.performSearches()

    # res = []
    # for i in range(100):
    SongLib.calculations()
    # print(res)
    # print(sum(res)/len(res))
