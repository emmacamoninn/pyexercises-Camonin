"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In:
# Information about a social media post:
# platform, brand, format, target audience,
# publication date, and objective.

# 2. Process:
# The program asks the user to enter the information.
# It checks that the values are acceptable.
# It creates the CSV file with a header if it does not exist.
# It adds each new post as a new row without deleting previous entries.

# 3. Out, file name and columns:
# The output file is 7.0_marketing_posts.csv.
# The columns are platform, brand, format,
# target_audience, publication_date, and objective.

# 4. Why these columns, and what this file is for:
# I chose these columns to organize and track social media posts.
# With 200 rows, I could compare platforms, content formats,
# target audiences, publication dates, and marketing objectives.
# This file could help me analyze a brand's social media strategy.


# Your code below

import csv
import os
from datetime import datetime

print("Please fill in the following details:")

# Collect information from the user
platform = input("Platform: ").strip()
brand = input("Brand: ").strip()
post_format = input("Format: ").strip()
target_audience = input("Target audience: ").strip()
publication_date = input("Publication date (DD/MM/YYYY): ").strip()
objective = input("Marketing objective: ").strip()

# Check that all fields are filled in
if not all([platform, brand, post_format, target_audience, publication_date, objective]):
    print("Error: All fields are required.")

else:
    # Check that the publication date is valid
    try:
        datetime.strptime(publication_date, "%d/%m/%Y")

    except ValueError:
        print("Error: Please enter a valid date in DD/MM/YYYY format.")

    else:
        # Define the CSV file and its columns
        filename = "7.0_marketing_posts.csv"

        columns = [
            "platform",
            "brand",
            "format",
            "target_audience",
            "publication_date",
            "objective"
        ]

        # Check if the file already exists and is not empty
        file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0

        # Open the CSV file in append mode
        with open(filename, "a", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Write the header only if the file is new or empty
            if not file_exists:
                writer.writerow(columns)

            # Add the new social media post
            writer.writerow([
                platform,
                brand,
                post_format,
                target_audience,
                publication_date,
                objective
            ])

        print("Data saved successfully!")
