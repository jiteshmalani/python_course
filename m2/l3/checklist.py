"""
OUTPUT:
You have 4 chores to finish today!

Did you finish Make your bed? (yes/no): yes
Great job!
Chores remaining: 3

Did you finish Feed the pet? (yes/no): no
Finish it first!
Chores remaining: 3

Did you finish Feed the pet? (yes/no): no
Finish it first!
Chores remaining: 3

Did you finish Feed the pet? (yes/no): yes
Great job!
Chores remaining: 2

Did you finish Take out the trash? (yes/no): yes
Great job!
Chores remaining: 1

Did you finish Wash the dishes? (yes/no): yes
Great job!
Chores remaining: 0

All chores are complete!
"""


# List of chores to complete
chores = ["Make your bed", "Feed the pet", "Take out the trash", "Wash the dishes"]


chores_remaining = len(chores) # 4
index = 0

print("You have",chores_remaining, "chores to finish today!\n")

while chores_remaining > 0:
    ans = input(f"did you finish {chores[index]} (yes / no): ")


    if ans == "yes":
        index = index + 1
        chores_remaining = chores_remaining - 1
        print("Great job!")

    else:
        print("Finish it first!")

    print("You have",chores_remaining, "chores to finish today!\n")

print("all chores are completed")