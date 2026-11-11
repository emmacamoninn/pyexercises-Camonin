"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The marketing channels list created in exercise 4.0.

# 2. Process: The program creates four different versions
# of the list by changing their order.
# Some methods create a new list, while others modify a list directly.

# 3. Out: Four different arrangements of the marketing channels,
# followed by the original list to check that it is unchanged.

# 4. My four orders and their effects:
# - Alphabetical order: sorted() creates a new list.
# - Reverse alphabetical order: sorted() with reverse=True creates a new list.
# - Reverse order: reverse() modifies the list on which it is used.
# - Sorted order: sort() modifies the list on which it is used.
# I will use copies to protect my original list.


# Your code below
marketing_channels = [
    "Instagram", "TikTok", "LinkedIn", "YouTube",
    "Email", "Website", "Influencers", "Events"
]

# Display the original list
print("Original list:", marketing_channels)

# Sort alphabetically
alphabetical_channels = sorted(marketing_channels)
print("Alphabetical order:", alphabetical_channels)

# Sort in reverse alphabetical order
reverse_alphabetical = sorted(marketing_channels, reverse=True)
print("Reverse alphabetical order:", reverse_alphabetical)

# Reverse the order using a copy
reversed_channels = marketing_channels.copy()
reversed_channels.reverse()
print("Reverse order:", reversed_channels)

# Sort alphabetically using a copy
sorted_channels = marketing_channels.copy()
sorted_channels.sort()
print("Sorted order:", sorted_channels)

# Check that the original list is unchanged
print("Original list at the end:", marketing_channels)
