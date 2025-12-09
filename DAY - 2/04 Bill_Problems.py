#if the bill was 150.00, split between 5 people, with 12% tip
#Each person should pay(150.0 / 5) * 1.12


print("Welcome to the tip calculator")
bill = float(input( "what was the total bill: $"))
tip = int (input( "what was the percentage tip would you like to give? 10, 12, or 15? : "))
people = int(input( "how many people split the bill : "))

# tip_percentage = tip_percentage / 100
# total_bill = (bill * (tip_percentage / 100)) / 5

bill_with_tip = bill * (1 + tip / 100)
bill_per_person = bill_with_tip / people

total_bill = round(bill_per_person, 2)


print(f"Each should pay: {total_bill}")