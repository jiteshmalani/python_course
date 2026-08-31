print("pick your vehicle 1. bike  2. car")

choice = int(input("enter your choice: "))

if choice == 1 :
    print("you have choosed a bike")

    print("choose your bike type 1. mountain  2. sports: ")

    bike_type = int( input("enter the bike type:  "))

    if bike_type == 1:
        print("you picked mountain bike")

    else :
        print("you picked sports bike")



else:
    print("you have choosed a car")

    print("choose your bike type 1. sedan  2. suv: ")

    car_type = int( input("enter the car type:  "))

    if car_type == 1:
        print("you picked sedan car")

    else :
        print("you picked suv car")


print("thank you")

