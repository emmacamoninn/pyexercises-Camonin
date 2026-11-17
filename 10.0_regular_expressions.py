
"""
Exercise 10.0 — Regular Expressions

1. Input:
   The user enters a username, an email address and a phone number.

2. Process:
   The program checks each value using regular expressions.
   It validates all three fields before saving anything.

3. Output:
   If all three values are valid, they are saved in a text file.
   Otherwise, error messages are displayed and nothing is saved.

4. The three fields and their rules:

   Username:
   Accepts 3 to 12 characters.
   Must start with a letter.
   Can contain letters, numbers and underscores.

   Email:
   Must contain text before and after @.
   Must contain a dot followed by at least two letters.

   Phone:
   Must contain exactly 10 digits.
   Must start with 0.

Regular expression explanations:

Username:
^ means start of the text.
[A-Za-z] means one letter.
[A-Za-z0-9_] means a letter, number or underscore.
{2,11} means between 2 and 11 repetitions.
$ means end of the text.

Email:
^ and $ check the complete text.
[A-Za-z0-9._+-]+ accepts letters, numbers and some symbols.
@ checks for the at sign.
[A-Za-z0-9.-]+ accepts the domain name.
\\. checks for a dot.
[A-Za-z]{2,} requires at least two letters at the end.

Phone:
^0 means the number must start with 0.
[0-9]{9} means exactly nine more digits.
$ means end of the text.
"""

import re

username_pattern = r"^[A-Za-z][A-Za-z0-9_]{2,11}$"
email_pattern = r"^[A-Za-z0-9._+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"
phone_pattern = r"^0[0-9]{9}$"

username = input("Enter your username: ")
email = input("Enter your email: ")
phone = input("Enter your French phone number: ")

username_valid = re.fullmatch(username_pattern, username)
email_valid = re.fullmatch(email_pattern, email)
phone_valid = re.fullmatch(phone_pattern, phone)

if username_valid and email_valid and phone_valid:
    with open("validated_info.txt", "w") as file:
        file.write(f"Username: {username}\n")
        file.write(f"Email: {email}\n")
        file.write(f"Phone: {phone}\n")

    print("All information is valid. Data saved successfully!")
else:
    print("Some information is invalid.")

    if not username_valid:
        print("Invalid username.")

    if not email_valid:
        print("Invalid email.")

    if not phone_valid:
        print("Invalid phone number.")

    print("No information was saved.")