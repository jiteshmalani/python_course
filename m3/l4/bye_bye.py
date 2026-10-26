valid = False
while not valid:

    try: 
        a = int(input("enter a number: "))
        valid = True
        print("bye bye")
    except ValueError:
        print("please enter a number")


    
