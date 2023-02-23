# Subscript
print("Hello"[0])

#Integer
integer = 324_345_292 #Escrito assim pra facilitar leitura e para o python ler números grandes

#Float
float = 3.14159

#Boolean
booleanTrue  = True
booleanFalse = False

# ----------------------------------------------------------------
teste = "testing python"
print(type(teste))

print(type(str(float)))

# ----------------------------------------------------------------

# Answers - Coding Rooms - Exercise 1
two_digit_number = input("Type a two digit number")

first_digit = two_digit_number[0]
second_digit = two_digit_number[1]

result = int(first_digit) + int(second_digit)
print(result)

# ----------------------------------------------------------------

# Mathematical Operations
# Division always returns a float number
# 2 ** 3 (two to the power of 3)


# -----------------------------------------------------------------

# Answers - Coding Rooms - Exercise 2 - BMI Calculator

height = input("Type a height in m: ")
weight = input("Type a weight in kg: ")

bmi = int(weight) / float(height) ** 2
bmi_as_int = int(bmi)
print(bmi_as_int)

# ------------------------------------------------------------------

# Round functions

print(round(8 / 3, 2))
print(8 // 3) # floor division

# +=, -=, /=, *=

score = 0
height = 1.8
isWinning = True

#f-string
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# ------------------------------------------------------------------
# Answers - Coding Rooms - Exercise 3 - Your life in Weeks

age = input("What is your current age?")

age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")