
"""
Exercise 8.1 — Bitwise operators

1. What goes in?
   Three permissions: VIEW, EDIT and PUBLISH.

2. What happens to it?
   - Two permissions are combined using OR (|).
   - A third permission is checked using AND (&).
   - A permission is added using OR (|).
   - A permission is removed using AND with NOT (& ~).

3. What comes out?
   The permissions represented as binary values at each step.

4. What are your permissions about?
   My permissions are about managing a marketing campaign:
   - VIEW: the person can view the campaign.
   - EDIT: the person can edit the campaign.
   - PUBLISH: the person can publish the campaign.
"""

# Define the permissions using bits
VIEW = 1       # 001
EDIT = 2       # 010
PUBLISH = 4    # 100

# Combine two permissions
permissions = VIEW | EDIT

print("Initial permissions:")
print("Binary:", format(permissions, "03b"))

# Check if PUBLISH permission is present
has_publish = (permissions & PUBLISH) != 0

print("\nIs PUBLISH allowed?")
print(has_publish)

# Add PUBLISH permission
permissions = permissions | PUBLISH

print("\nAfter adding PUBLISH:")
print("Binary:", format(permissions, "03b"))

# Remove EDIT permission
permissions = permissions & ~EDIT

print("\nAfter removing EDIT:")
print("Binary:", format(permissions, "03b"))