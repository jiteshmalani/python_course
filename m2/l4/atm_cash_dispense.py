"""
notes = [100, 50, 20, 10, 5, 1]

OUTPUT:

=== ATM Cash Dispenser ===

Enter customer name: Ajay
Enter withdrawal amount: 100

Dispensing 100 units:

1 x 100 note(s)
Transaction complete!


Serve another customer? (yes/no): yes
Enter customer name: Rahul
Enter withdrawal amount: 125

Dispensing 125 units:

1 x 100 note(s)
1 x 20 note(s)
1 x 5 note(s)
Transaction complete!


Serve another customer? (yes/no): yes
Enter customer name: Chethan
Enter withdrawal amount: 107

Dispensing 107 units:

1 x 100 note(s)
1 x 5 note(s)
2 x 1 note(s)
Transaction complete!


Serve another customer? (yes/no): no

Customers Served : 3
Total Amount Dispensed : 332
ATM Closed
"""


notes = [100, 50, 20, 10, 5, 1]
customers = 0
total_amount = 0

while True:
    name = input("enter your name: ")
    amount = int(input("enter the amount: "))
    remaining = amount
    index = 0 

    while index < len(notes):
        note = notes[index]  # 100
        count = remaining // note  # 220 // 100 = 2
        if count > 0:
            print(f"{count} x {note} note(s)")
            remaining = remaining % note  # 220 % 100 = 20

        index = index + 1

    print("Transaction complete!\n")
    customers = customers + 1
    total_amount = total_amount + amount

    choice = input("\nServe another customer? (yes/no): ").lower()

    if choice == "no":
        break
print(f"\nCustomers Served : {customers}")
print(f"Total amount dispensed {total_amount}" )
print("ATM Closed")