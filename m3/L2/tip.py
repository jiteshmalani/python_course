def tip(bill_amount , tip_percent):
    tip = bill_amount * tip_percent/100
    return tip
    

bill_amount = int(input("enter your bill amount: "))

tip_percent = int(input("enter the percent of tip: "))

result = tip(bill_amount , tip_percent)

print(result)