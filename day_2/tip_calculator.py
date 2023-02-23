# (150.00 / 5) * 1.12
# bill: 150, persons: 5, tip: 12%
# round the result to 2 decimal places = 33.60
print("Welcome to the tip calculator.")
bill = float(input("Total bill: $"))
tip = int(input("How much tip would like to give? 10, 12 or 15: "))
people = int(input("How many people to slipt the bill?"))

tip_as_percent = tip / 100
total_tip = bill * tip_as_percent
total_bill = bill + total_tip

bill_per_person = total_bill / people
# final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)

print(f"Each person should pay ${final_amount}")