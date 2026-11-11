"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of eight marketing channels.

# 2. Process: The program stores the channels in a list.
# It displays the whole list, one selected channel,
# the sorted list, and counts the number of channels.

# 3. Out: The whole list, one selected channel,
# the sorted list, and the total number of channels.

# 4. My list is about marketing channels.
# I computed the number of channels because it shows
# how many different channels are used in a marketing strategy.


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

# Display the whole list
print("Whole list:", marketing_channels)

# Display one selected channel
print("One channel:", marketing_channels[2])

# Sort the list alphabetically
sorted_channels = sorted(marketing_channels)
print("Sorted list:", sorted_channels)

# Count the number of channels
print("Number of channels:", len(marketing_channels))