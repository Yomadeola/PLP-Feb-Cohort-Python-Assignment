# Create a function named calculate_discount(price, discount_percent) 
# that calculates the final price after applying a discount. 
# The function should take the original price (price) and the discount percentage (discount_percent) as parameters. 
# If the discount is 20% or higher, apply the discount; otherwise, return the original price.


def calculate_discount(price, discount_percent):
    if discount_percent >= 0.20:
        discount = discount_percent * price 
        price = price - discount
        return f"Discount applied. Final price: {price}"
    else:
        return f"No discount applied. Price remains: {price}"

  
final_price = calculate_discount(300000, 0.10)
print(final_price)



# Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage.
# Print the final price after applying the discount, or if no discount was applied, print the original price.


user_price = float(input("Enter a price:  "))
user_discount = float(input("Enter the discount percentage (e.g., 20 for 20%): ")) / 100


final_price2 = calculate_discount (user_price, user_discount)


# Calculate and print result
final_price2 = calculate_discount(user_price, user_discount)
print(final_price2)