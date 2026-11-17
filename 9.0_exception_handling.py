
"""
Exercise 9.0 — Exception Handling

1. In:
   The user enters a number.

2. Process:
   The program divides 100 by the number entered.
   It checks whether the input is valid.
   The user has three attempts.

3. Out:
   The result of the division or an error message.

4. The two failures:
   - ZeroDivisionError: the user enters zero.
   - ValueError: the user enters text or an empty line.
   They should have different messages because the problems are different.

Why catch each failure separately?
   Catching exceptions separately allows the program to give
   a specific and helpful message for each type of error.

Attempts:
   The user has three attempts before the program stops.

Tests:
   - Normal number: the program displays the result.
   - Zero: the program displays a division by zero message.
   - "abc": the program displays an invalid number message.
   - Empty line: the program displays an invalid number message.
"""

# Maximum number of attempts
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    user_input = input("Enter a number to divide 100 by: ")

    try:
        number = float(user_input)
        result = 100 / number

        print("Result:", result)
        break

    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")

    except ValueError:
        print("Error: Please enter a valid number.")

    attempts += 1

else:
    print("You have used all your attempts. Goodbye!")