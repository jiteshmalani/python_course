import random
num = random.randint(0,9)
gues = int(input("enter a guse"))
if gues == num:
    print("you are right")
else:
    
    print("wrong answer")
print(num)