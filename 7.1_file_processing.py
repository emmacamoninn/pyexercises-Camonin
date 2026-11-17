
"""
Exercise 7.1 — Loading a file, cleaning it, saving the result

What is wrong with names.txt:
# 1. There are empty lines.
# 2. Some names have spaces at the beginning of the line.
# 3. Some names are written entirely in lowercase.
# 4. Some names use inconsistent uppercase and lowercase letters.
# 5. Some names have the first name and last name with different capitalization.

Answers:

1. In:
   The program reads names from names.txt.

2. Process, problem by problem:
   - Empty lines are removed.
   - Extra spaces at the beginning and end are removed using strip().
   - Names are converted to a consistent capitalization using title().
   - Names are sorted alphabetically by last name.
   - For compound last names, all words after the first name
     are considered part of the last name.

3. Out:
   A new file called cleaned_names.txt containing the cleaned
   and sorted names. The original file is not modified.

4. How I decide which word is the last name:
   The first word is the first name. All remaining words
   are considered the last name.
"""

# Read the original file
with open("names.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Clean the names
names = []

for line in lines:
    name = line.strip()

    if name:
        name = name.title()
        names.append(name)

# Sort names by last name
names.sort(key=lambda name: " ".join(name.split()[1:]).casefold())

# Write the result into a new file
with open("cleaned_names.txt", "w", encoding="utf-8") as file:
    for name in names:
        file.write(name + "\n")

print("Names have been cleaned and sorted!")
print("The result is saved in cleaned_names.txt")