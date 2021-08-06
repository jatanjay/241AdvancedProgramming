"""
Jatan Pandya
Prof. Arman Pouraghily / ECE241
C1 / Project 1 - File Song.py
31 Jul '21
"""


class Song:
    """
    Class song ::
    """

    def __init__(self, trial_song):
        self.title = trial_song[1].strip()
        self.artist = trial_song[2].strip()
        self.song_duration = trial_song[3]
        self.track_ID = trial_song[4]

    # self.serial = trial_song[0]

    def display(self):
        """
        :return:
        :rtype:
        """
        print(
            f" \n Song Name : {self.title}\n Artist : {self.artist}\n Time Durations : {self.song_duration}\n Song Id "
            f": "
            f"{self.track_ID}")
