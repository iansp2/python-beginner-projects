"""Returns expense per person based on total expense and people participating.
This module receives the total amount, the number of people, and stores the expense on the people responsible for it in a dictionary.
"""
from typing import Dict, List, Union

def print_separator(char: str = '-', length: int = 15) -> None:
    print(char * length)

def init_expenses_dict(guests: List[str]) -> Dict[str, float]:
    return {guest: 0.0 for guest in guests}

def get_user_input(question: str, expected_type: type) -> Union[int, str, float]:
    while True:
        try:
            return expected_type(input(question))
        except ValueError as e:
            print(f"Invalid input. Please enter a valid {expected_type.__name__}.")

def print_guest_names(guests: List[str]) -> None:
    print("Let's add a new expense.\nWho was involved in this expense? For example, if guests 1 and 3 were involved, you can type 1,3 in the terminal.")
    print_separator()
    for i, guest in enumerate(guests, start=1):
        print(f"{i}. {guest}")
    print_separator()

def get_involved_guests(input_str: str, guests: List[str]) -> List[str]:
    try:
        indices = [int(i) - 1 for i in input_str.split(',')]
        return [guests[idx] for idx in indices if 0 <= idx < len(guests)]
    except (ValueError, IndexError):
        raise ValueError("Invalid guest numbers. Please enter valid indices.")

def assign_expense(people_involved: List[str], amount: float, expenses: Dict[str, float]) -> None:
    split_amount = amount / len(people_involved)
    for person in people_involved:
        expenses[person] += split_amount

def print_final_expenses(expenses: Dict[str, float]) -> None:
    print("Here is the final tally:")
    print_separator()
    for i, (person, amount) in enumerate(expenses.items(), start=1):
        print(f"{i}. {person}: ${amount:.2f}")
        print_separator()

def main() -> None:
    number_of_people = get_user_input("How many people are in your group?\n", int)
    if number_of_people <= 1:
        print("It seems like you don't have enough people to use this app. Please try again when you have more friends.")
        return

    guests = [get_user_input(f"Name of guest {i + 1}: ", str) for i in range(number_of_people)]
    expenses = init_expenses_dict(guests)

    while True:
        print_guest_names(guests)
        
        people_involved_input = get_user_input("Enter the numbers corresponding to the guests involved: ", str)
        try:
            people_involved = get_involved_guests(people_involved_input, guests)
        except ValueError as e:
            print(e)
            continue

        amount = get_user_input("How much was this transaction?\n", float)
        assign_expense(people_involved, amount, expenses)

        more_expenses = get_user_input("Are there more expenses? (Y/N)\n", str).strip().upper()
        if more_expenses != "Y":
            break

    print_final_expenses(expenses)

if __name__ == "__main__":
    main()