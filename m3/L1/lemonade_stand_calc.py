"""
OUTPUT:

Welcome to the Lemonade Stand!
Price per cup is 10

Enter number of cups sold: 4

===== RECEIPT =====
Price Per Cup : 10.0
Cups Sold     : 4
Total Cost    : 40.0
Thank you for visiting!
===================
"""

def greet():
    print("Welcome to the lemonade stand")

def calc_total(price , cups):
    total_cost = price * cups
    return total_cost

greet()

price = 10

cups = int(input("enter the number of cups you need: "))

total = calc_total(price , cups)

print("===== RECEIPT =====")

print("price per cup : ", price)

print("cups sold : ", cups)

print("total cost : ", total)

print("thank you for visiting")

print("===================")




