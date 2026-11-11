"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A confirmation answer from the user about launching
# a marketing campaign.

# 2. Process: The program repeatedly asks the user for an answer
# until the campaign is confirmed or the maximum number
# of attempts is reached.
# It removes extra spaces and converts the answer to lowercase.

# 3. Out: A message showing whether the campaign was confirmed
# and the number of attempts made.

# 4. My stop condition, my attempt limit, my summary:
# The loop stops when the user answers "yes" or after 5 attempts.
# The program accepts answers with capital letters and extra spaces.
# The summary displays whether the campaign was confirmed
# and how many attempts were made.


# Your code below
attempts = 0
max_attempts = 5
confirmed = False

while attempts < max_attempts and not confirmed:
    answer = input("Is the marketing campaign confirmed? ")
    answer = answer.strip().lower()

    attempts = attempts + 1

    if answer == "yes":
        confirmed = True

if confirmed:
    print("Campaign confirmed after", attempts, "attempt(s).")
else:
    print("Campaign was not confirmed after", attempts, "attempts.")
