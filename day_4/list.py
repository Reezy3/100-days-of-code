import random
print("Welcome to WHO IS PAYING THE BILL?")
name_string = input("Please input everybody's name seperated by a coma. \n ")
names = name_string.split(",")

no_of_people = len(names)

bill_payer = random.randint(0, no_of_people - 1)


print(f"{names [bill_payer]} is going to buy the meal today!")