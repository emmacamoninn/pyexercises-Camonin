"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: Information about a social media post, including its platform,
# brand, format, target audience, publication date, and objective.

# 2. Process: The program stores the information in a dictionary,
# reads one field, updates one field, removes one field,
# and displays all the remaining fields with their values.

# 3. Out: The original information, the updated information,
# and all the remaining fields. The program also handles
# a field that does not exist.

# 4. My object, my five fields, and why those:
# My object is a social media post. I chose the platform, brand,
# format, target audience, publication date, and objective
# because these details are useful when planning
# and managing social media content.


# Your code below

social_media_post = {
    "platform": "Instagram",
    "brand": "Dior",
    "format": "Reel",
    "target_audience": "Young adults",
    "publication_date": "December 10",
    "objective": "Increase brand awareness"
}

# Read one field
print("Platform:", social_media_post["platform"])

# Change one field
social_media_post["objective"] = "Promote a new collection"
print("Updated objective:", social_media_post["objective"])

# Remove one field
del social_media_post["format"]

# Display all remaining fields
for field, value in social_media_post.items():
    print(field, ":", value)

# Check a field that does not exist
print("Hashtags:", social_media_post.get("hashtags", "Not available"))

# Check: Using social_media_post["hashtags"] would raise a KeyError
# because this field does not exist.
# The get() method avoids this error and displays "Not available".
