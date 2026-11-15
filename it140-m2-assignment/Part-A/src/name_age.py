"""The program will ask the user for their name and age, and it will calculate the birth year.

Input:
    Name: type integer, source user input
    Age: type integer, source user input

Process:
    Calculate birth year

Output:
    The program will greet the user using the name they input, then display the year they were born. It will be output in the console, while the input will be entered in the terminal

Typical usage example:
    What is your name? Pat
    How old are you? 31

    Hello Pat! You were born in 1995.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name: str = input('What is your name? ')
    age: int = int(input('How old are you? '))

    # Calculate user's approximate birth year.
    birth_year: int = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f'Hello {name}! You were born in {birth_year}.')


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===