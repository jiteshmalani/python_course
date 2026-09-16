rows = int(input("enter the no. of rows: "))

for i in range(rows):
    for j in range(rows - i + 1):

        print(" ", end = "")

    for k in range(2*i+1):

        print("*",end = "")

    print()


for i in range(rows, -1 , -1):
    for j in range(rows - i + 1):

        print(" ", end = "")

    for k in range(2*i+1):

        print("*",end = "")

    print()


