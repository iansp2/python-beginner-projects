""" Calculates net income and recommends spending breakdown
This finance calculator will get your gross income as an input, and output your net income plus recommended recommended spending per category.
"""

from typing import Dict

def spending_recommendation(net_income: float) -> None:
    categories: Dict[str, float] = {
        "rent": 0.25,
        "entertainment": 0.1,
        "food": 0.15,
        "utilities": 0.1,
        "savings": 0.2,
        "transportation": 0.1,
        "miscellaneous": 0.1
    }

    for category, percentage in categories.items():
        spending: float = net_income * percentage
        print(f"{category}: ${spending:,.2f}")
    print("-----------------------------------------")

def finance_calculator(gross_income: int, tax_rate: float = 0.25) -> None:
    if gross_income <= 0:
        print("Oh no, you're broke. Get a job and come back later!")
        return
    
    net_income: float = gross_income * (1 - tax_rate)

    print(f"Your net income is ${net_income:,.2f}, considering a tax rate of {tax_rate*100:,.0f}%")
    print("-----------------------------------------")
    print("I recommend your spending allocation to look like this:\n")
    spending_recommendation(net_income)

def main() -> None:
    while True:
        try:
            gross_income: int = int(input("Let's take a look at your finances. What is your current income? Please round it to the nearest dollar.\n"))
            break  # Exit the loop if input is valid
        except ValueError:
            print("Please enter a valid integer.")

    finance_calculator(gross_income)

if __name__ == "__main__":
    main()