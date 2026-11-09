a = 0

b = 0


try:

    a = float(input("enter a number: "))
    b = float(input("enter a number: "))

except ValueError:
    print("please entr a number")

def add(a , b):
    result = a + b
    return result

def sub(a , b):
    result = a - b
    return result

def mul(a , b):
    result = a * b 
    return result

def div(a , b):
    result = a / b 
    return result

result = mul(a , b )
print(result)



