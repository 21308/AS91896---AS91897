print("This is a price comparison tool that will convert the price and weight to calculate the unit price. We will first ask for your budget range,\
 then we will ask you for your desired items and then do the calculations to find the unit price.\n")

# Ask for users budget.
budget = input("What is your budget?")
while not budget.isnumeric():
    print("Sorry we really need to know your budget to help you.")
    budget = input("What is your budget?")
budget = int(budget)

print("Your total budget is: $", budget)

# Ask user for their inputs
print("Could you please list the product name so that we can help you?\n")
# Ask for the product
product_name = input ("Product Name:\n")
# Ask for the weight of the product.
print("Could you please list the weight so that we can help you?\n")
weight = input ("Weight(kg)\n")
# Ask for the cost of the product.
print("Could you please list the cost of the item so that we can help you?\n")
cost = input ("Cost:\n")







   