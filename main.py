import time

# Ask for users budget.
budget = input("What is your budget?")
while not budget.isnumeric():
    print("Sorry we really need to know your budget to help you.")
    budget = input("What is your budget?")
budget = int(budget)

   