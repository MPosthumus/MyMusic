# Mathieu Posthumus
# 10-09-2020
# Final assignment for Programming
# Project: MyMusic

# Module imports
from datetime import datetime
from functions import clearConsole
from menu import Menu
from playlist import Playlist
from profile import Profile
from termcolor import cprint
import sys


clearConsole()

# Welcoming messages
cprint("MyMusic - Manage your favorite songs!\n", "blue")
print("Welcome, lets start with some information about you!")

# Initialize the Profile class
profile = Profile()

# Call the name/dateOfBirthHandler
profile.nameHandler()
profile.dateOfBirthHandler()

# Initialize the playlist
playlist = Playlist()

# Initialize the Menu class
menu = Menu(profile, playlist)
