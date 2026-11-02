import random
choices = ["rock"," paper" ,"secoirs"]
computer = random.choice(choices)
user = input("enter your choice" )
print(computer)

if user == computer :
    print("tie")

elif (user == "rock" and computer ==  "secoirs") or \
    (user == "paper" and computer ==  "rock") or \
    (user == "seciors" and computer ==  "paper") :

    print("user wins")

else:
    print("computer wins")

