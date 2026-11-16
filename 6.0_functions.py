"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of marketing channel names.

# 2. Process: The function calculates the total number
# of characters in all channel names and divides it
# by the number of channels.

# 3. Out: The average number of characters in the
# marketing channel names.

# 4. My function name, and why return rather than print:
# My function is called calculate_average_name_length
# because its name clearly explains what it does.
# I use return instead of print because return allows
# me to reuse the result in other parts of the program.
# If the list is empty, the function returns 0 to avoid
# a division by zero error.


# Your code below
marketing_channels = [
    "Instagram",
    "TikTok",
    "LinkedIn",
    "YouTube",
    "Email",
    "Website",
    "Influencers",
    "Events"
]


def calculate_average_name_length(channels):
    if len(channels) == 0:
        return 0

    total_characters = 0

    for channel in channels:
        total_characters = total_characters + len(channel)

    return total_characters / len(channels)
# First call: all marketing channels
result_1 = calculate_average_name_length(marketing_channels)
print("Average length of all channels:", result_1)

# Second call: two marketing channels
result_2 = calculate_average_name_length(["Instagram", "TikTok"])
print("Average length of selected channels:", result_2)

# Third call: an empty list
result_3 = calculate_average_name_length([])
print("Average length of an empty list:", result_3)
