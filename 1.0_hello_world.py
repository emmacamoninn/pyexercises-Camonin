"""Exercise 1.0 — Hello World

WHAT THE PROGRAM MUST DO
    Display a message of your choice, five times, with each line numbered.

ANSWER THESE FIRST, in comments at the top of your file, before any code
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What message did you choose, and why that one?

WHAT THE AI CANNOT KNOW
    The message is yours. Choose something you would actually want a program to say,
    not "Hello, World!". Your comment has to justify it.

CHECK IT YOURSELF
    Count the lines your program produced. Five, not four and not six.
    Then change the number to 3 and run it again. If you had to rewrite more than one
    character, your program is not built the way it should be.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# The program takes a message and a number of repetitions as input.

# 2. Process:
# The program repeats the chosen message five times and adds a number to each line.

# 3. Out:
# The program displays the message five times, with each line numbered from 1 to 5.

# 4. My message, and why:
# My message is "Camonin" because it is my last name.
# I chose it because it is personal and represents me.


# Your code below
for i in range(1, 6):
    print(f"{i}. Camonin")