try: 

       
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    div = a/b
    print(div)
    
except ValueError:
    print("please enter a number")

except ZeroDivisionError:
    print("0 cannot be divided in maths")

else:
    print("no exception" )

finally:
    print("it will run anyways")


