# Introduce what this code is..
print("This is a price comparison tool that will convert the price and weight to calculate the unit price. We will first ask for your budget range,\
 then we will ask you for your desired items and then do the calculations to find the unit price.\n")
thisdict={}
product_dict={}


# Ask for users budget.
budget = input("What is your budget?")
while not budget.isnumeric():
    print("Sorry we really need to know your budget to help you.")
    budget = input("What is your budget?")
budget = int(budget)



print("Your total budget is: $", budget)

# Ask user for their inputs
print("Could you please list the product name so that we can help you?"
      " Or type xxx to quit")
while True:
    # Ask for the product
    product_name = input ("Product Name:\n")
    if product_name == 'xxx':
        break
    # Ask for the weight of the product.
    print("Could you please list the weight so that we can help you?\n")
    weight = float(input ("Weight(kg)\n"))
    # Ask for the cost of the product.
    print("Could you please list the cost of the item so that we can help you?\n")
    cost = int(input ("Cost($):\n"))
    new_product = {product_name:cost}
    product_dict.update(new_product)
    cost_per_kg=cost/weight


# Storing users input in a dictionary
    new_product = {product_name:cost_per_kg}
    thisdict.update(new_product)
# Sorted Dictionary
sorted_dict=dict(sorted(thisdict.items(), key=lambda item: item[1]))


# Recommending user the most suitable item from their inputs
i=0
while True:
    cheapest_product = list(sorted_dict.keys())[i]
    cheapest_cost = product_dict[cheapest_product]
    
    if cheapest_cost <= budget:
        print(f"The most cost efficient product within your budget is {cheapest_product} for ${cheapest_cost}.")
        break
    i+=1
