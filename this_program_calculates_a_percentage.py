"""This program calculates a percentage. A retail business is planning to have a storewide sale where the prices
of all items will be 20 percent off. We habe been asked to write a program to calculate the sale price of a item
after the discount is sutracted. Here is the algorithm:
    1. Get the oriinal price of the item.
    2. Calculate 20 percent of the original price. This is the amount of the discount.
    3. Subtract the discount from the original price. This is the sale price.
    4. Display the sale price"""

# This program gets an item's original price and calculates its sale price, with a 20% discount

# Get the item's original price
original_price = float(input("Enter the item's original price: "))

# Calculate the amount of the discount
discount = original_price * 0.2

# Calculate the sale price
sale_price = original_price - discount

# Display the sale price
print('The sale price is', sale_price)
    

