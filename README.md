# MyMusic
Python eindopdracht(School)

====Install====
Before running this project, you should install: `pip install termcolor`

MyMusic is sort of a MP3 player, where you can;
 - add new songs
    - title - artist - album - genre - duration
 - see the list of songs
 - get songs by genre
 - add songs to your favorite list
 - load songs - dummy context

[main.py]
In my main.py comes everything together.

[profile.py]
In profile.py I ask the name and date of birth and will handle this, so it will 
not stop the program on bad input. Except when the user fills in an date of birth 
that will say if it's younger than 8 years old.

[menu.py]
In menu.py it should handle so, that the menu will always come back when someone 
is done with his action. Except when [9] Exit is called. This should stop the 
program.

[playlist.py]
In playlist.py I will handle everything what is ment for the songs.
In here will be stored all the songs in one list

[functions.py]
In functions.py I define my function that can be used overall the project.
