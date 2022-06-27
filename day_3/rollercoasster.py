print("Welcome to Rollercoaster!")
height = int(input("What is your height in cm? \n"))
bill = 0

# Conditional statement
if height >= 120:
 print("You can ride the rollercoaster!")
 age = int(input("What is your age?"))
 if age < 12:
  bill = 5
  print("Child tickets are $5")
 elif age <= 18:
  bill = 7
  print("Teenagers tickets are $7")
 elif age >= 45 and age <= 55:
  print("Everything is going to be okay. Have a free ride on us!")
 else:
  bill = 12
  print("Adult tickets are $12")
  
  
 wants_photo = input("Do you want a photo taken? Y or N ?")
 wants_photo_1 = wants_photo.upper()
 if wants_photo_1 == "Y":
  bill += 3
 print(f"Yor final bill is ${bill}")  
else:
 print("Sorry you have to get taller before you can ride.")
 
# miltiple if statements