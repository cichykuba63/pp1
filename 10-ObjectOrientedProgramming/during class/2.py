class Music:
    
    def __init__(self, artist, track_title, album, year):
        self.performer = artist
        self.song = track_title
        self.album = album
        self.year = year

    def __str__(self):
        return f"Performer:     {self.performer}\nSong:          {self.song}\nAlbum:         {self.album}\nYear:          {self.year}"

song1 = Music("Ed Sheeran", "Hearts Don't Break Around Here", "Divide", 2017)
song2 = Music("Linkin Park", "In the End", "Linkin Park", 2010)
song3 = Music("Maroon 5", "Sugar", "Sugar", 2013)

print(song1)
print()
print(song2)
print()
print(song3)