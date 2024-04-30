# Ask for users budget.
budget = input("What is your budget?")
while not budget.isnumeric():
    print("Sorry we really need to know your budget to help you.")
    budget = input("What is your budget?")
budget = int(budget)

print("Your total budget is: $", budget)

# Ask user for their inputs
print("Can you please list the product name, weight in kg and the cost you wish to get price compared?\n")
# Ask for the product
product_name = input ("Product Name:\n")
# Ask for the weight of the product.
weight = input ("Weight(kg)\n")
# Ask for the cost of the product.
cost = input ("Cost:\n")







   