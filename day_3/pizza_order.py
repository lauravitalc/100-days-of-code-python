print("What size pizza do you want? S, M or L?" )
pizza = 'M';
print("Do you want pepperoni? Y or N?")
pepperoni = 'Y';
print("Do you want cheddar? Y or N?")
cheddar = 'Y';

bill = 0;

if pizza == "S":
    bill += 15
elif pizza == "M":
    bill += 20
elif pizza == "L":
    bill += 25

if pepperoni == "Y":
    if pizza == "S":
        bill +=2
    else:
        bill += 3

if cheddar == "Y":
    bill += 1

print(f"Your final bill is {bill}")