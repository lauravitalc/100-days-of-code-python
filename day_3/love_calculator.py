name1 = "Laura"
name2 = "Gabriel"

combined_str = (name1 + name2).lower()

t = combined_str.count("t")
r = combined_str.count("r")
u = combined_str.count("u")
e = combined_str.count("e")

true = t + r + u + e

l = combined_str.count("l")
o = combined_str.count("o")
v = combined_str.count("v")
e = combined_str.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))


if love_score < 10 or love_score > 90:
    print(f"Your love score is: {love_score}. You go together like coke and mentos!")
elif love_score >= 40 and love_score <= 50:
     print(f"Your love score is: {love_score}. You are alright together.")
else:
    print(f"Your score is: {love_score}.")
