day = input("Enter the day of the week: ")

weather = input("Enter the weather (sunny, rainy, cloudy): ")

homework = input("Have you completed your homework? (yes/no): ")

if day == "sunday" or day == "saturday":
    print("It's the weekend! Enjoy your day off.")

elif day == "friday" :
    print( "it is the last day of the week" )

else:
    print("It's a weekday. Get ready for school!")


if weather =="sunny" and homework == "yes":
    print("Great! You can go outside and enjoy the sunny weather after school.")

if not ( homework == "yes" ):
    print("Make sure to complete your homework before going outside.")
