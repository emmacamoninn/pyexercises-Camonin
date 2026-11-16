
# SURVIVE THE QUARTER
# Student: Emma Camonin
# Group: C
#
# EXTRA FEATURE: The Algorithm
# On one random day, the reputation impact of the chosen decision is doubled.
# I chose this feature because it adds unpredictability to the game.
#
# INPUT:
# The program reads scenarios_C.csv using commas as separators.
# Each row contains an event, a day, three decisions, reputation impacts,
# budget impacts and three outcomes. Impacts are written as numbers with units.
#
# PROCESS:
# The program loads and shuffles the scenarios.
# Each day, the player chooses A, B or C.
# The program updates the budget and reputation and records the result.
#
# OUTPUT:
# The player sees their final budget, reputation, score and title.
# The program saves the result in results.csv.
#
# FAILURE CASES:
# 1. Invalid choice: the program asks the player to choose A, B or C again.
# 2. Missing scenario file: the program displays an error and stops safely.
# 3. Invalid impact value: the program uses 0 instead of crashing.
# 4. Empty player name: the program asks for a name again.

import csv
import random
import re
import os
from datetime import date


def parse_impact(value):
    """Convert an impact such as '+15 pts' or '-800 EUR' into a number."""
    match = re.search(r'-?\d+', value.replace(',', ''))
    if match:
        return int(match.group())
    return 0


def load_scenarios(filename):
    """Read the scenarios from the CSV file."""
    if not os.path.exists(filename):
        print("Error: scenarios_C.csv was not found.")
        return []

    try:
        with open(filename, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)
            scenarios = list(reader)
        return scenarios
    except (OSError, csv.Error):
        print("Error: The scenario file could not be read.")
        return []


def get_player_choice():
    """Ask the player to choose A, B or C."""
    while True:
        choice = input("Your choice (A, B or C): ").strip().upper()
        if choice in ["A", "B", "C"]:
            return choice
        print("Invalid choice. Please enter A, B or C.")


def build_option(scenario, choice):
    """Return the chosen decision as a tuple."""
    index = {"A": "1", "B": "2", "C": "3"}[choice]

    decision = scenario["Decision " + index]
    reputation_change = parse_impact(scenario["Reputation " + index])
    budget_change = parse_impact(scenario["Budget " + index])
    outcome = scenario["Outcome " + index]

    return (decision, budget_change, reputation_change, outcome)


def get_title(score):
    """Return a title based on the final score."""
    if score < 95:
        return "Eternal Intern"
    elif score < 120:
        return "Growth Hacker"
    elif score < 140:
        return "CMO Material"
    else:
        return "Viral Legend"


def save_result(name, budget, reputation, title):
    """Append the game result to results.csv."""
    filename = "results.csv"
    file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0

    try:
        with open(filename, "a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)

            if not file_exists:
                writer.writerow(["name", "budget", "reputation", "title", "date"])

            writer.writerow([name, budget, reputation, title, date.today()])
    except OSError:
        print("Error: The result could not be saved.")


def main():
    """Run the Survive the Quarter game."""
    print("===================================")
    print("       SURVIVE THE QUARTER")
    print("          CROISSANT ROCKET")
    print("===================================")

    name = input("Enter your name: ").strip()
    while not name:
        name = input("Please enter a valid name: ").strip()

    scenarios = load_scenarios("scenarios_C.csv")

    if len(scenarios) < 10:
        print("Error: At least 10 scenarios are required.")
        return

    random.shuffle(scenarios)
    selected_scenarios = scenarios[:10]

    budget = 10000
    reputation = 50
    history = []

    algorithm_day = random.randint(1, 10)

    print("\nWelcome,", name + "!")
    print("Your starting budget is 10,000 EUR.")
    print("Your starting reputation is 50/100.")
    print("The Algorithm will activate on one random day!")

    fired_reason = ""

    for day_number, scenario in enumerate(selected_scenarios, start=1):
        print("\n===================================")
        print("DAY", day_number, "/ 10")
        print("Budget:", budget, "EUR")
        print("Reputation:", reputation, "/ 100")
        print("-----------------------------------")
        print(scenario["Event"])

        print("\nA:", scenario["Decision 1"])
        print("B:", scenario["Decision 2"])
        print("C:", scenario["Decision 3"])

        choice = get_player_choice()

        # Build and unpack the selected option tuple.
        decision, budget_change, reputation_change, outcome = build_option(
            scenario, choice
        )

        if day_number == algorithm_day:
            print("\nTHE ALGORITHM IS ACTIVE! Reputation impact doubled!")
            reputation_change = reputation_change * 2

        old_reputation = reputation

        budget += budget_change
        reputation += reputation_change

        # Reputation cannot exceed 100.
        reputation = min(reputation, 100)

        actual_reputation_change = reputation - old_reputation

        history.append((day_number, decision, actual_reputation_change))

        print("\nYour decision:", decision)
        print(outcome)
        print("Budget change:", budget_change, "EUR")
        print("Reputation change:", actual_reputation_change, "points")

        if budget <= 0:
            fired_reason = "Your budget reached zero or below."
            break

        if reputation <= 0:
            fired_reason = "Your reputation reached zero or below."
            break

    print("\n===================================")
    print("             GAME OVER")
    print("===================================")

    print("Player:", name)
    print("Final budget:", budget, "EUR")
    print("Final reputation:", reputation, "/ 100")

    if fired_reason:
        title = "Fired"
        print("\nYOU HAVE BEEN FIRED!")
        print(fired_reason)
    else:
        score = reputation + budget // 200
        title = get_title(score)
        print("Final score:", score)
        print("Your title:", title)

    if history:
        best_move = max(history, key=lambda item: item[2])
        worst_move = min(history, key=lambda item: item[2])

        print("\nBest move:")
        print("Day", best_move[0], "-", best_move[1])
        print("Reputation change:", best_move[2])

        print("\nWorst move:")
        print("Day", worst_move[0], "-", worst_move[1])
        print("Reputation change:", worst_move[2])

    save_result(name, budget, reputation, title)
    print("\nYour result has been saved in results.csv.")
    print("Thanks for playing Survive the Quarter!")


if __name__ == "__main__":
    main()