"""
Activity: Weather Outfit Picker

Instructions:
1. Ask the user to enter today's temperature.
2. If the temperature is below 20°C, suggest wearing a jacket.
3. Otherwise, suggest wearing a t-shirt.
4. Ask if it is raining.
5. If there are puddles, suggest wearing boots.
6. Otherwise, suggest wearing sneakers.
7. Display a summary of the outfit choices.
"""

# Ask for today's temperature
tempreture = float(input("Enter today's temperature in °C: "))


# Check if it is cold and decide the outfit 
tempreture_check = 20
if tempreture < tempreture_check:
    outfit = "jacket"
    print("wear a jacket") 

else:
    outfit = "t-shirt"
    print("wear a t-shirt")




# Check if it is raining and decide on the umbrella
is_raining = input("Is it raining? (yes/no): ").lower()
if is_raining == "yes":
    print("Carry an umbrella")


# Check for puddles and decide the shoes
has_puddles = input("Are there puddles on the ground? (yes/no): ").lower()
if has_puddles == "yes":
    shoes = "boots"
    print("Wear boots")

else:
    shoes = "any shoes"
    print("Wear shoes")



# Display the final summary
print("\n===== WEATHER OUTFIT SUMMARY =====")
print("Temperature :", tempreture, "°C")
print("Outfit      :", outfit)
print("Raining     :", is_raining)
print("Shoes       :", shoes)
print("=================================")