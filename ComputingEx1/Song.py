"""
Jatan Pandya
Prof. Arman Pouraghily / ECE241
C1 / Project 1 - File Song.py
31 Jul '21
"""


class Song:
    """
    one instance of the Song class is created for each song from the input csv file
    """

    def __init__(self, trial_song):
        """
        :param trial_song: A list of song details (extracted from the CSV)
        :type trial_song: LIST
        """
        '''
        Different attributes -->
        
        Example : ["0,Qing Yi Shi,Leon Lai,203.38893,5237536"]
        serial = 0 
        title = Qing Yi Shi
        artist = Leon Lai
        song_duration = 203.38893
        track_id = 5237536
        '''
        self.title = trial_song[1].strip()
        self.artist = trial_song[2].strip()
        self.song_duration = trial_song[3]
        self.track_ID = trial_song[4]

    # self.serial = trial_song[0]

    def display(self):
        print(
            f"Song Name : {self.title}\nArtist : {self.artist}\nTime Durations : {self.song_duration}\nSong Id "
            f": "
            f"{self.track_ID}")
