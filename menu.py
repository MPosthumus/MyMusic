# Mathieu Posthumus
# 16-09-2020
# Final assignment for Programming
# Project: MyMusic

from functions import clearConsole, tryParseInt
from termcolor import cprint
import sys


# Everything what belongs to Menu
class Menu:
    # Sets profile and starts the showMenu function
    def __init__(self, profile, playlist):
        self.playlist = playlist
        self.profile = profile
        self.showOptions()

    def showOptions(self):
        clearConsole()

        cprint(f"Hi {self.profile.name}, make an option!", "green")
        print("[1] My Information")
        print("[2] My Songs")
        print("[3] All Songs")
        print("[4] Songs by Genre")
        print("[5] Add Song")
        print("[5] Load  Song")
        print("[9] Exit MyMusic\n")

        self.optionHandler()

    def optionHandler(self):
        chosenMenuOption = tryParseInt(input(f"Option: "))
        
        clearConsole()

        if chosenMenuOption == 9:
            cprint("Thanks for using MyMusic. See you back soon!", "green")
            sys.exit()
        elif chosenMenuOption == 1:
            self.showMyInformation()
        elif chosenMenuOption == 2:
            self.showMySongs()
        elif chosenMenuOption == 3:
            self.showAllSongs()
        elif chosenMenuOption == 4:
            self.showByGenre()
        elif chosenMenuOption == 5:
            self.playlist.createSong()
        else:
            self.showOptions()

        input("\nPress [Enter] to go back to the menu!")
        self.showOptions()

    def showMyInformation(self):
        print(self.profile)

    def showMySongs(self):
        print('My Songs')

    def showAllSongs(self):
        print(self.playlist.songs)

    def showByGenre(self):
        print('Genre Songs')