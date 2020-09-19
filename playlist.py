# Mathieu Posthumus
# 18-09-2020
# Final assignment for Programming
# Project: MyMusic

from termcolor import cprint


class Playlist:
    songs = []

    def createSong(self):
        cprint("Fill in information to add a song to your playlsit.", "green")
        title = input("Title: ")
        artist = input("Artist: ")
        album = input("Album: ")
        genre = input("Genre: ")
        duration = input("Duration: ")
        
        self.songs.append({
            "id": len(self.songs)+1,
            "title": title,
            "artist": artist,
            "album": album,
            "genre": genre,
            "duration": duration
        })
    
    def showList(self, sortBy = "title"):
        for song in self.songs:
            cprint(f"{song.id}. {song.title} - {song.artist} - {song.album} - {song.duration}")