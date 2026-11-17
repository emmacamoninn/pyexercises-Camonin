
"""
Exercise 8.0 — Operators

1. What goes in?
   Two strings: "Emma" and "emma".

2. What happens to it?
   Python compares the two strings using comparison operators.
   It also combines the comparison results using logical operators.

3. What comes out?
   A readable table showing each expression and its result.

4. Which two values did you pick, and which comparison result surprised you?
   I picked "Emma" and "emma".
   I was surprised that "Emma" is smaller than "emma"
   because Python distinguishes uppercase and lowercase letters.
"""

# Choose two values
value1 = "Emma"
value2 = "emma"

# Perform all comparisons
comparisons = {
    "value1 == value2": value1 == value2,
    "value1 != value2": value1 != value2,
    "value1 < value2": value1 < value2,
    "value1 <= value2": value1 <= value2,
    "value1 > value2": value1 > value2,
    "value1 >= value2": value1 >= value2
}

# Logical combinations
logical_results = {
    "Equality AND inequality": comparisons["value1 == value2"] and comparisons["value1 != value2"],
    "Equality OR inequality": comparisons["value1 == value2"] or comparisons["value1 != value2"],
    "NOT equality": not comparisons["value1 == value2"],
    "Less than AND not equal": comparisons["value1 < value2"] and comparisons["value1 != value2"],
    "Greater than OR equal": comparisons["value1 > value2"] or comparisons["value1 == value2"]
}

# Display the results as a readable table
print("=" * 55)
print("COMPARISON OPERATORS")
print("=" * 55)
print(f"{'Expression':<35} {'Result':<10}")
print("-" * 55)

for expression, result in comparisons.items():
    print(f"{expression:<35} {result}")

print("\n" + "=" * 55)
print("LOGICAL OPERATORS")
print("=" * 55)
print(f"{'Expression':<35} {'Result':<10}")
print("-" * 55)

for expression, result in logical_results.items():
    print(f"{expression:<35} {result}")

print("=" * 55)