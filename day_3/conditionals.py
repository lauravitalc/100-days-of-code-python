print("Welcome to the rollercoaster!")
height = int(input("What is yout height in cm?"))
age = int(input("What is your age?"))
          
if height >= 120:
    print("You can ride the rollercoaster.")
    if age < 12:
        print("The price is $5")
    elif age <= 18:
        print("The price is $7")
    else:
        print("The price is $12")
else:
    print("Sorry. You can't ride the rollercoaster.")

# --------------------------------------------------------

number = int(input("Which number do you wan to check?"))

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")

# --------------------------------------------------------