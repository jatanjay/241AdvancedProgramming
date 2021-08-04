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

from partition import partition


# import csv
# import random
# from partition import partition
# import time


class Song:
    def __init__(self, trial_song):
        self.title = trial_song[1].strip()
        self.artist = trial_song[2].strip()
        self.song_duration = trial_song[3]
        self.track_ID = trial_song[4]

    # self.serial = trial_song[0]

    def display(self):
        print(
            f" \n Song Name : {self.title}\n Artist : {self.artist}\n Time Durations : {self.song_duration}\n Song Id "
            f": "
            f"{self.track_ID}")


class SongLibrary:
    def __init__(self):
        self.song_array = []
        self.library_size = 0
        self.library_isSorted = False

    def loadLibrary(self, file_name):
        """
        This method takes the input data file name, opens it, and loads the songs in the file into the library.
        Order of the songs is retained
        :param file_name: name of the csv file
        :type file_name: .csv file
        :return: list containing objects of songs
        :rtype: list
        """

        with open(file=file_name, mode='r', encoding='utf-8') as csv_file:
            reader = csv.reader(csv_file, skipinitialspace=True)
            for song_detail in reader:
                # print(song_detail)
                # print(type(song_detail))
                self.song_array.append(Song(song_detail))
                self.library_size += 1

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
        else:
            print(f"\nNot found!")

    def quickS(self, array, start_index, end_index):
        partition(array, start_index, end_index)

        if end_index <= start_index:
            return

        high = partition(array, start_index, end_index)
        self.quickS(array, start_index, high)
        self.quickS(array, high + 1, end_index)

    def quickSort(self):
        """
        Quick sort algorithm to sort the song database based on the song title
        Once sorted --> the status of the Boolean variable is changed
        :return:
        :rtype:
        """
        arr = self.song_array
        self.quickS(arr, 0, len(arr) - 1)
        self.library_isSorted = True

    def random_songs(self):
        """
        Uses a random number generator (uniform distribution) to select 100 song titles arbitrarily.
        Saves them in a list.
        :return:
        :rtype:
        """
        # j = 1
        # r = (self.song_array[:10])
        # for i in r:
        #     print(i.title)

        songs_random = random.sample(self.song_array, k=100)
        songs_random = [song_obj.title for song_obj in songs_random]
        # print(songs_random[:5])
        return songs_random

    def performLinearSearch(self):
        """
        Performs a linear search in the sorted database for those 100
        songs. Record the total time spent on the linear searches.
        """
        time_start = time.time()
        for song_title in self.random_songs():
            self.linearSearch(query=song_title, attribute='title')
        time_end = time.time()
        print(f"\nLinear Search took a total of {time_end - time_start} secs for 100 Random Songs")


if __name__ == '__main__':
    file = 'TenKsongs.csv'
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

    SongLib.quickSort()
    SongLib.performLinearSearch()
