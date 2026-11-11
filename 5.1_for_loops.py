"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The list of eight marketing channels from exercise 4.0.

# 2. Process: The program goes through each marketing channel,
# finds its position in the list, and counts the number
# of characters in its name.

# 3. Out: One line for each marketing channel showing its
# position, name, and number of characters.

# 4. What I compute for each item, and why it is worth showing:
# I calculate the number of characters in each channel name
# because it allows me to compare the length of the names
# and see which marketing channels have the shortest
# or longest names.


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

for position, channel in enumerate(marketing_channels, start=1):
    print(position, "-", channel, "has", len(channel), "characters")
