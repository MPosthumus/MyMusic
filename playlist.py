# Mathieu Posthumus
# 18-09-2020
# Final assignment for Programming
# Project: MyMusic

from functions import noEmptyInputHandler, timeParser, tryParseInt
from termcolor import cprint
import json


class Playlist:
    isFilledWithSeed = False
    songs = []
    favoriteSongs = []

    def addSong(self, title, artist, album, genre, duration):
        self.songs.append({
            "id": len(self.songs)+1,
            "title": title,
            "artist": artist,
            "album": album,
            "genre": genre,
            "duration": duration
        })

        self.readSong(self.songs[-1])
        cprint("Song is added!", "green")

    def addToFavorite(self):
        availableSongs = []
        availableSongIds = []
        for song in self.songs:
            if song not in self.favoriteSongs:
                availableSongs.append(song)
                availableSongIds.append(song["id"])

        if len(availableSongs) < 1:
            cprint("There are no songs to be added...", "red")
        else:
            self.showAllSongs(False)
            while True:
                songId = tryParseInt(input("\nSong to add: "))
                if not songId or songId not in availableSongIds:
                    cprint("No song found with this id...", "red")
                else:
                    for song in availableSongs:
                        if song["id"] == songId:
                            self.favoriteSongs.append(song)
                    cprint("Song added to \"My Favorite Songs\"!", "green")
                    break

    def createSong(self):
        cprint("Fill in information to add a song to your playlsit.", "green")
        title = noEmptyInputHandler("Title: ")
        artist = noEmptyInputHandler("Artist: ")
        album = noEmptyInputHandler("Album: ")
        genre = noEmptyInputHandler("Genre: ")
        duration = self.isValidDurationInput("(example: 1:14:35) Duration: ")

        self.addSong(title, artist, album, genre, duration['formatted'])

    def getKnownGenres(self):
        genres = []
        for song in self.songs:
            if song['genre'] not in genres:
                genres.append(song['genre'])

        genres.sort()
        return genres

    def isValidDurationInput(self, question):
        duration = ""
        while True:
            duration = input(question).split(":")
            isValid = True
            if len(duration) > 3:
                cprint(
                    "You are allowed to fill in <hours>:<minutes>:<seconds>",
                    "red")
                isValid = False
                continue

            for segment in duration:
                if not segment.isnumeric():
                    isValid = False
                    continue

            if isValid:
                break
            else:
                cprint("Invalid input, try again", "red")

        return timeParser(duration)

    def readSong(self, song):
        cprint(
            f"\n{song['id']}. {song['title']} - {song['artist']} - "
            f"{song['album']} - {song['duration']}")

    def seedListOfSongs(self):
        with open("./seed.json") as seed_file:
            seed = json.load(seed_file)
            for song in seed['songs']:
                self.addSong(
                    song['title'], song['artist'], song['album'],
                    song['genre'], song['duration'])
        self.isFilledWithSeed = True

    def showFavoriteSongs(self):
        if len(self.favoriteSongs) < 1:
            cprint("No favorite songs found...", "red")
        else:
            for song in self.favoriteSongs:
                self.readSong(song)

    def showAllSongs(self, all=True):
        songs = self.songs
        if not all:
            songs = []
            for song in self.songs:
                if song not in self.favoriteSongs:
                    songs.append(song)

        if len(songs) < 1:
            cprint("No songs found...", "red")
        else:
            for song in songs:
                self.readSong(song)

    def songsByGenre(self):
        if len(self.songs) < 1:
            cprint("No songs found...", "red")
        else:
            cprint(f"Known genres: {self.getKnownGenres()}", "yellow")
            while True:
                genre = input("Genre: ")
                if genre not in self.getKnownGenres():
                    cprint("Unknown genre", "red")
                else:
                    break

            for song in self.songs:
                if song['genre'] == genre:
                    self.readSong(song)
