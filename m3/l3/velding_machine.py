"""
OUTPUT:
Snack Price: 25
Enter the amount paid: 32
Change Returned: 7
Thank you!
"""

# Snack Vending Machine

# Function to calculate change
def calculate_change(paid, price):

    change = paid - price

    return change 


# Main program
price = 25
paid = int(input("enter the amount you paid: "))

result = calculate_change(paid,price)
print(result)
                          

