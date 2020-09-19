# Mathieu Posthumus
# 16-09-2020
# Final assignment for Programming
# Project: MyMusic

import os

# Clear the console
def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')

# Validated if the input is an integer
def tryParseInt(value):
    try:
        return int(value)
    except ValueError:
        return False, value

test = input()

tryParseInt(test)

# print