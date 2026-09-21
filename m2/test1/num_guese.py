hidden_number = 6

attemts = 5

print("you will have 5 attemts to crack the hidden number")

users_guese = int(input("enter your guese between 1 and 10: "))


while users_guese != 6:
    
    

    if users_guese > 6:
        print("LOWER")

    elif users_guese < 6:
        print("HIGER")

    attemts = attemts - 1

    if attemts == 0:
    
        print("GAME OVER")
        


    if users_guese == 6:
        print("YOU WON ")

        break
    users_guese = int(input("enter your guese between 1 and 10: "))

    







    
    




