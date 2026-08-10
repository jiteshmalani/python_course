# --- Assignment Operator (=) ---
# Store the harvest in kg from each of the 5 fields
field1 = 120
field2 = 85
field3 = 150
field4 = 95
field5 = 110

# --- Arithmetic Operators (+, -, *, /) ---
# Calculate total and average harvest
total=field1 + field2 + field3 + field4 + field5
print("Total harvest in kg:", total)
average = total / 5
print("Average harvest in kg:", average)

# Price per kg is 15 rupees — calculate total earnings
price_per_kg = 15
earnings= total * price_per_kg
print("Total earnings in rupees:", earnings)





# --- Floor Division (//) and Modulus (%) ---

# Pack the harvest into bags of 25 kg each
bags=total//25
print("Number of bags needed:", bags)



# --- Comparison Operators (>, <, ==, >=) ---
# Compare this year's harvest with last year
last_year = 500
is_less = total < last_year
print("Is this year's harvest less than last year's?", is_less)
bonus_field = 30
total+= bonus_field
print(total)



# --- Assignment Operators (+=, -=) ---
# A bonus field adds 30 kg to the total