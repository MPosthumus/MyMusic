# Mathieu Posthumus
# 16-09-2020
# Final assignment for Programming
# Project: MyMusic

from datetime import time
from termcolor import cprint
import os


# Clear the console
def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


# Will repeat the input till it is filled
def noEmptyInputHandler(question):
    value = ""
    while True:
        value = input(question)
        if len(value) > 0:
            break
        else:
            cprint("Input cannot be empty", "red")

    return value


# Parse time to readable time
def timeParser(value):
    totalTimeInSeconds = 0
    for index in range(0, len(value)):
        position = len(value)-index-1
        totalTimeInSeconds += int(value[position])*60**index

    seconds = totalTimeInSeconds % 60
    minutes = (totalTimeInSeconds // 60) % 60
    hours = (totalTimeInSeconds // 3600) % 60

    return {
        "formatted": f"{hours}:{minutes}:{seconds}",
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds
    }


# Validated if the input is an integer
def tryParseInt(value):
    try:
        return int(value)
    except ValueError:
        return False
