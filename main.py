# Ask for users budget.
budget = input("What is your budget?")
while not budget.isnumeric():
    print("Sorry we really need to know your budget to help you.")
    budget = input("What is your budget?")
budget = int(budget)

print("Your total budget is: $", budget)

# Ask user for the product name, weight in kg and the cost.
print("Can you please list the product name, weight in kg and the cost you wish to get price compared?\n")
reply = input ("List them here:")



   