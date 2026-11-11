"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The artist's name and the number of songs planned.

# 2. Process: The program asks the user for two answers and stores them.

# 3. Out: A sentence displaying the artist's name and the number of songs planned.

# 4. My two fields, and what I would do with them:
# I chose the artist's name and the number of songs to prepare
# and organize a music project.


# Your code below
artist_name = input("What is the artist's name? ")
number_of_songs = input("How many songs are planned? ")

print(artist_name, "is preparing a music project with", number_of_songs, "songs.")

print(number_of_songs + 1)
# Test 1: When I entered an empty line, Python stored an empty string.
# The program displayed the sentence but returned a TypeError when adding 1.

# Test 2: When I entered a space, Python stored a string containing a space.
# The program displayed the sentence but returned a TypeError when adding 1.

# Test 3: When I entered text instead of a number, Python stored a string.
# The program displayed the sentence but returned a TypeError when adding 1.