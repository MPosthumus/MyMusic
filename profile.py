# Mathieu Posthumus
# 10-09-2020
# Final assignment for Programming
# Project: MyMusic

from datetime import datetime
from termcolor import cprint
import sys


# Everything what belongs to Profile
class Profile:
    def __init__(self):
        self.DATE_FORMAT = "%d-%m-%Y"
        self.name = ""
        self.dateOfBirth = datetime.now()
        self.age = ""

    # Asking for name and checking for validation
    def nameHandler(self):
        while True:
            name = input("What is you name?\n")
            if self.validateName(name):
                break

    # Validates the length of name
    def validateName(self, name):
        if len(name) < 2 or len(name) > 25:
            cprint(
                "The length of your name should be greater than 1 and shorter"
                " than 26 characters.\n", "yellow")
            return False
        else:
            self.name = name
            return True

    # Asking for date of birth and checking for validation
    def dateOfBirthHandler(self):
        # validAge = False
        while True:
            try:
                dateOfBirthInput = input(
                    f"What date were you born? (Example: "
                    f"{datetime.now().strftime(self.DATE_FORMAT)})\n")
                dateOfBirth = datetime.strptime(
                    dateOfBirthInput, self.DATE_FORMAT)
                if self.validateDateOfBirth(dateOfBirth):
                    break
            except ValueError:
                cprint("Wrong date format!", "red")
                # validAge = False

    # Validates if the user is old enough (8+)
    def validateDateOfBirth(self, dateOfBirth):
        today = datetime.now()
        age = today.year - dateOfBirth.year
        age - ((today.month, today.day) < (dateOfBirth.month, dateOfBirth.day))

        if age > 8:
            self.age = age
            self.dateOfBirth = dateOfBirth
            return True
        elif age < 0:
            cprint(
                "Very funny, with this date of birth you shouldn\'t even"
                "been born.\nGoodbye!", "red")
        else:
            cprint(
                "You\'re younger then 8.\nYou are not allowed to join.\n"
                "Hereby goodbye!", "red")
            sys.exit()

    # Show information about the user
    # def showMyInformation(self):
        
