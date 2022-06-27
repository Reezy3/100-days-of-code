import random
print("===============WELCOME TO ROCK PAPER SCISSORS GAME!!!!!!!!!!!!!!!!!!=============")
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
game = [rock, paper, scissors]
user_name = input("Please enter your name: \n")

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))

if user_choice >= 3 or user_choice < 0:
 print(f"{user_name}, you typed an invalid number , You lose!!!")
else:
 user_input = game[user_choice]
 computer_input = random.choice(game)

 if user_input == game[0] and computer_input == game[2]:
  print(f"You picked: \n{user_input}")
  print(f"Computer picked: \n{computer_input}")
  print(f"Congrats {user_name}, Rock smashes scissors YOU WIN!!!")

 elif user_input == game[1] and computer_input == game[0]:
  print(f"You picked: \n {user_input} ")
  print(f"Computer picked: \n {computer_input}")
  print(f"Congrats {user_name}, paper covers rock YOU WIN!!!")
  
 elif user_input == game[2] and computer_input == game[1]:
  print(f"You picked: \n {user_input} ")
  print(f"Computer picked: \n {computer_input} ")
  print(f"Congrats {user_name}, Scissors cuts paper YOU WIN!!!")

 elif user_input == computer_input:
   print(f"You picked: \n {user_input} ")
   print(f"Computer picked: \n {computer_input} ")
   print(f"Sorry {user_name}, IT'S A DRAW")
   
 if computer_input == game[0] and user_input == game[2]:
  print(f"You picked: \n{user_input}")
  print(f"Computer picked: \n{computer_input}")
  print(f"Sorry {user_name}, Rock smashes scissors YOU LOSE!!!")

 elif computer_input == game[1] and user_input == game[0]:
  print(f"You picked: \n {user_input} ")
  print(f"Computer picked: \n {computer_input}")
  print(f"Sorry {user_name}, paper covers rock YOU LOSE!!!")
  
 elif computer_input == game[2] and user_input == game[1]:
  print(f"You picked: \n {user_input} ")
  print(f"Computer picked: \n {computer_input} ")
  print(f"Sorry {user_name}, Scissors cuts paper YOU LOSE!!!")