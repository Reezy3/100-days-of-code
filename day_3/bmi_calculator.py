print("Welcome to BMI calculator")
height = float(input("Enter your height in m: \n"))
weight = float(input("Enter your weight in kg: \n"))
bmi = round(weight / (height ** 2))
if bmi < 18.5:
 print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 25:
 print(f"Your BMI is {bmi}, you have a Normal weight.")
elif bmi < 30:
 print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
 print(f"You BMI is {bmi}, you are Obese.")
else:
 print(f"Your BMI is {bmi}, you are clinically obese.")