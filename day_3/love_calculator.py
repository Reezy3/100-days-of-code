print("Welcome to the Love Calculator")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_name = (name1 + name2).lower()
t = combined_name.count("t")
r = combined_name.count("r")
u = combined_name.count("u")
e = combined_name.count("e")
first_number = t + r + u + e


l = combined_name.count("l")
o = combined_name.count("o")
v = combined_name.count("v")
e = combined_name.count("e")
last_number = l + o + v + e

score = int(str(first_number) + str(last_number))

if score < 10 or score > 90:
 print(f"Your score is {score}, you go together like coke and mentos.")
elif score >= 40 and score <= 50:
 print(f"Your score is {score}, you are alright together.")
else:
 print(f"Your score is {score} ")