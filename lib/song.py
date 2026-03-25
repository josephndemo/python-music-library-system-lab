class Song:
    # Class Attributes
    count = 0
    genres = set()
    artists = set()
    genre_count = {}
    artists_count = {}

    def __init__(self, name, artist, genre):
        self.name = name
        self.artist = artist
        self.genre = genre

        # Call class methods with values
        Song.add_song_to_count()
        Song.add_to_genres(self.genre)
        Song.add_to_artists(self.artist)
        Song.add_to_genre_count(self.genre)
        Song.add_to_artists_count(self.artist)

    # Class Methods
    @classmethod
    def add_song_to_count(cls):
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        cls.genres.add(genre)

    @classmethod
    def add_to_artists(cls, artist):
        cls.artists.add(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        if artist in cls.artists_count:
            cls.artists_count[artist] += 1
        else:
            cls.artists_count[artist] = 1

song1 = Song("No Woman No Cry", "Bob Marley", "Reggae")
song2 = Song("Welcome to Jamrock", "Damian Marley", "Reggae")
song3 = Song("Temperature", "Sean Paul", "Reggae")
song4 = Song("Halo", "Beyonce", "Pop")
song5 = Song("Empire State of Mind", "Jay-Z", "Rap")
song6 = Song("Crazy in Love", "Beyonce", "Pop")

print(Song.count)
print(Song.genres)
print(Song.artists)
print(Song.genre_count)
print(Song.artists_count)