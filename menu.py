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
        print("[2] My Favorite Songs")
        print("[3] All Songs")
        print("[4] Songs by Genre")
        print("[5] Add Song")
        print("[6] Add Song to \"My Favorite Songs\"")
        if self.playlist.isFilledWithSeed == False:
            print("[7] Load  Songs")
        print("[9] Exit MyMusic\n")

        self.optionHandler()

    def optionHandler(self):
        chosenMenuOption = tryParseInt(input(f"Option: "))
        
        clearConsole()

        if chosenMenuOption == 9:
            cprint("Thanks for using MyMusic. See you back soon!", "green")
            sys.exit()
        elif chosenMenuOption == 1:
            self.profile.showMyInformation()
        elif chosenMenuOption == 2:
            self.playlist.showFavoriteSongs()
        elif chosenMenuOption == 3:
            self.playlist.showList()
        elif chosenMenuOption == 4:
            self.playlist.songsByGenre()
        elif chosenMenuOption == 5:
            self.playlist.createSong()
        elif chosenMenuOption == 6:
            self.playlist.addToFavorite()
        elif chosenMenuOption == 7 and self.playlist.isFilledWithSeed == False:
            self.playlist.seedListOfSongs()
        else:
            self.showOptions()

        input("\nPress [Enter] to go back to the menu!")
        self.showOptions()

    def showByGenre(self):
        print('Genre Songs')