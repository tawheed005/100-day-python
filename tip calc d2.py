print("welcome to tip calculator!")
bill=int(input("how much was the total bill ?:"))
tipping_amount=int(input("how much do you want to tip?\n 10%_15%_20%:"))
total_people=int(input("For how many people?: "))
tip_decimal=tipping_amount / 100 + 1
total_bill=bill*tip_decimal
For_each=total_bill/total_people
print("every person should pay:",round(For_each,2))
