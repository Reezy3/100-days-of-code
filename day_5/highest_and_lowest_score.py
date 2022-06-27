# 🚨 Don't change the code below 👇
print("Welcome to Maximum and Minimum score CHECKER!!!!!!!!")
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
highest_score = 0
for scores in student_scores:
 if highest_score < scores:
  highest_score = scores
print(f"The highest score in the class is: {highest_score}")

lowest_score = student_scores[0]
for students in student_scores:
  if lowest_score > students:
    lowest_score = students
print(f"The lowest score in the class is: {lowest_score}")