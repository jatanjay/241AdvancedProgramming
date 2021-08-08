"""
Jatan Pandya
Prof. Arman Pouraghily / ECE241
C1 / Project 1
File : SongLibrary.py
31 Jul '21
"""

"""
Manage your data in Python classes and objects. For example, define two classes, Song
and SongLibrary. You will use one instance of the Song class for each song and one
instance of the SongLibrary class for your song library.
"""

"""
-- Imports --
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
        self.song_array = []  # an array for all the Song objects,
        self.library_size = 0  # an integer that indicates how many songs the library holds
        self.library_isSorted = False  # a Boolean variable to show whether the library is sorted or not
        self.BST = None  # SongLibrary's Binary Search Tree (BST), used when generating a BST
        self.bst_buildTime = float()  # stores time taken to build the BST
        self.bst_runtime = float()  # stores time taken by BST to run
        self.linear_runtime = float()  # stores time taken by Linear search to run
        self.size_k = 100  # can be tweaked if one desires to increase sample size of random songs

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
                self.song_array.append(Song(song_detail))
                self.library_size += 1

        array = self.song_array[:5]
        print("\nFirst Five Songs in the CSV: ")
        print("------------------------------------------------------------------------------------"
              "------------------------------------------------------------------------------------")
        for song in array:
            print(song.title)

    def quickSort(self):
        """
        Quick sort algorithm to sort the song database based on the song title
        Once sorted --> the status of the Boolean variable is changed
        :return:
        :rtype:
        """
        arr = self.song_array  # the arr we just loaded into the data structure
        quickS(arr, 0, self.library_size - 1)  # calling quickS that will in turn call partition() from sort_quick.py
        self.library_isSorted = True  # all fine and dandy, change the boolean variable now

        """
        Just a check, first few songs in this new sorted array. The fact that we are creating this new array by slicing 
        from self.song_array, it tells sorted songs are stored in the same song array, as required.
        """
        array = self.song_array[1:6]
        print("\nFirst five songs of the Sorted Array: ")
        print("------------------------------------------------------------------------------------"
              "------------------------------------------------------------------------------------")
        for song in array:
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

        """
        Below is a more refined, fancy representation. easy to understand / good for testing. But adds sentences.
        If using the tests in main(), comment this one out
        """
        # if song_count:
        #     return f"For song {attribute} '{query}', Total Count is {song_count}"
        # else:
        #     return f"Not results found for song {attribute} '{query}'"

        """
        A more simple, to the point, no sentences. I'll go with this just in case.
        """
        if song_count:
            return song_count
        else:
            return False

    def BSTree(self):
        self.BST = AVLTree()  # code for AVL in avl.py
        # the BST will be created and stored in the variable (we created earlier in __ini__())
        start = time.time()
        for song in self.song_array:
            node = Node(song.title)
            self.BST.insert(node)  # node insertion
        end = time.time()
        self.bst_buildTime = end - start
        print(f"It took {self.bst_buildTime} seconds to build the BST")
        print(f"The height of the BST is -->", self.BST.root.getHeight())

    def printBST(self):
        """
        This is one way to see (literally) if our freshly made BST turned out the way we intended
        Here, I make a new small BST of just first 25 songs.
        Printing 9709 songs looks bad. Un-comment anyway to see.
        see graph_print.py for more -->
        """
        trial_bst = AVLTree()
        for song in self.song_array[:8]:
            node = Node(song.title)
            trial_bst.insert(node)
        print(trial_bst)

        # print(self.BST) # will print the whole BST

    def searchBST(self, query):
        """
        Since we are explicitly told to search directly for song title, an 'attribute' is not needed, as query will
        always be the song title
        :param query: Name of the song (song title) to be searched
        :type query: str
        :return: True if song exists, false otherwise
        :rtype: Boolean
        """
        curr_root = self.BST.root
        while curr_root is not None:
            if curr_root.key == query:
                return True  # will return True at once song exists
            elif curr_root.key > query:
                curr_root = curr_root.left
            else:
                curr_root = curr_root.right
        return False

    def random_songs(self):
        """
        Uses a random number generator (uniform distribution) to select 100 song titles arbitrarily.
        Saves them in a list.
        :return: songs_random -- a list of 100 random song titles
        :rtype: list
        """
        songs_random = random.sample(self.song_array, k=self.size_k)
        songs_random = [song_obj.title for song_obj in songs_random]
        return songs_random

    def performSearches(self):
        """
        Performs all required searches in the sorted database for those 100
        songs. Record the total time spent on the linear searches.
        """

        random_songs = self.random_songs()  # generate a list of self.size_k songs
        print(f"\n{self.size_k} Random Songs:")
        print("------------------------------------------------------------------------------------"
              "------------------------------------------------------------------------------------")
        print(f"First five songs from the array of {self.size_k} random songs that will be searched for: ")
        print(f"{random_songs[:5]}")  # a little peek

        print("\nSearches:")
        print("------------------------------------------------------------------------------------"
              "------------------------------------------------------------------------------------")
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

    def calculations(self):
        # bst_time = self.performSearches()
        # print("\nAt a glance:")
        print("------------------------------------------------------------------------------------"
              "------------------------------------------------------------------------------------")
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
    print("\nContents of the CSV file (example):")
    print("------------------------------------------------------------------------------------"
          "------------------------------------------------------------------------------------")
    with open(file, 'r') as c:
        r = csv.reader(c)
        for j in r:
            test = Song(trial_song=j)
        test.display()

    SongLib = SongLibrary()
    loaded_library = SongLib.loadLibrary(file)

    print("\nLinear Search Test:")
    print("------------------------------------------------------------------------------------"
          "------------------------------------------------------------------------------------")
    print(SongLib.linearSearch('Bob Dylan', 'artist'))
    print(SongLib.linearSearch('A Boy Named Sue', 'title'))
    print(SongLib.linearSearch('Fake Song', 'title'))
    print(SongLib.linearSearch('Jatan Pandya', 'artist'))

    SongLib.quickSort()

    print("\nBST:")
    print("------------------------------------------------------------------------------------"
          "------------------------------------------------------------------------------------")
    SongLib.BSTree()
    print("\nFirst few songs of the BST, visualized: ")
    print("------------------------------------------------------------------------------------"
          "------------------------------------------------------------------------------------")
    SongLib.printBST()

    print("\nBST Search Test:")
    print("------------------------------------------------------------------------------------"
          "------------------------------------------------------------------------------------")
    print(SongLib.searchBST("There She Goes Again"))
    print(SongLib.searchBST("A hard Rain's gonna fall"))
    print(SongLib.searchBST("New Pony"))

    SongLib.performSearches()
