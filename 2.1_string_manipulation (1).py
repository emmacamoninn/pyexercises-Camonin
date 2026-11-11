"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A sentence about a music project entered by the user.

# 2. Process: The program applies four different string methods to transform the sentence.

# 3. Out: Four different versions of the original sentence.

# 4. My four transformations, and when each is useful:
# - strip(): removes unnecessary spaces at the beginning and end of a sentence.
# - upper(): changes all letters to uppercase, useful for titles.
# - lower(): changes all letters to lowercase, useful for keeping text consistent.
# - replace(): replaces specific characters, useful for changing words or formatting text.


# Your code below

sentence = input("Enter a sentence about music: ")

print("strip():", sentence.strip())
print("upper():", sentence.upper())
print("lower():", sentence.lower())
print("replace():", sentence.replace("music", "songs"))


# Check:
# strip(): The result was what I expected because it removed spaces at the beginning and end.
# upper(): The result was what I expected because it changed all letters to uppercase.
# lower(): The result was what I expected because it changed all letters to lowercase.
# replace(): The result was what I expected because it replaced the word music with songs.
