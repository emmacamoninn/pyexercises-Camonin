"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# A list of marketing channel names.

# 2. Process, function by function:
# First, count_channels() counts the total number of channels.
# Then, count_long_names() counts the names longer than 7 characters.
# Next, calculate_percentage() calculates the percentage.
# Finally, percentage_of_long_names() uses the three functions
# to calculate the percentage of long channel names.

# 3. Out:
# The percentage of marketing channels with names longer than 7 characters.

# 4. The question my fourth function answers:
# What percentage of my marketing channels have names longer than
# 7 characters? Splitting the work into three small functions
# makes each calculation easier to test and check.


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
def count_channels(channels):
    return len(channels)
def count_long_names(channels):
    count = 0

    for channel in channels:
        if len(channel) > 7:
            count = count + 1

    return count
def calculate_percentage(part, total):
    if total == 0:
        return 0

    return (part / total) * 100
def percentage_of_long_names(channels):
    total = count_channels(channels)
    long_names = count_long_names(channels)

    return calculate_percentage(long_names, total)
# Test 1: count_channels()
# Input: The complete list of 8 marketing channels.
# Expected output: 8
print("Test 1:", count_channels(marketing_channels))

# Test 2: count_long_names()
# Input: The complete list of 8 marketing channels.
# Expected output: 3
print("Test 2:", count_long_names(marketing_channels))

# Test 3: calculate_percentage()
# Input: 3 and 8.
# Expected output: 37.5
print("Test 3:", calculate_percentage(3, 8))
# Final test: percentage_of_long_names()
# Input: The complete list of 8 marketing channels.
# Expected output: 37.5%
result = percentage_of_long_names(marketing_channels)
print("Percentage of long channel names:", result, "%")