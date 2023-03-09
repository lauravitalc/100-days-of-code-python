
# on every year that is evenly divisible by 4 
# EXPECT every year that is evenly divisible by 100 
# UNLESS the year is also evenly divisible by 400

year = 2003

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year")

# Very slow solution!