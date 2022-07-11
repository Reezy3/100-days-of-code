# Import logo and print it 
from art import logo
print(logo)

# Ask for username and print a personalized welcome
user_name = input("Please enter a username: ").capitalize()
print(f"Welcome {user_name}, To Number Guessing game.")

# Print out the range of numbers to be guessed from and pick a random number
print("I'm thinking about a number from 1 to 100")

import random
chosen_number = random.randint(1, 101)
print(f"Psst the answer is {chosen_number}")

# Take an input of the difficulty they want

lives = 0

difficulty = input("What difficulty will you prefer? 'easy', 'medium', 'hard': ").lower()
if difficulty == "easy":
    lives = 10

elif difficulty == "medium":
    lives = 7

elif difficulty == "hard":
    lives = 5
    
else:
    print(f"{user_name}, you selected an invalid option")
    
print(f"{user_name}, you have {lives} attempts ")

guess = input("Guess a number")
def compare_values(number_1, number_2):
    if number_1 > number_2:
        return {user_name}, "your guess is higher than the chosen number"
    elif number_1 < number_2:
        return {user_name}, "your guess is lower than the chosen number"
    
game_over = True
while not game_over:
    if guess == chosen_number:
        print(f"{user_name}, you guessed correct! YOU WIN")
        game_over = True
    else:
        if lives == 0:
            game_over = True
        else:
            compare_values(guess, chosen_number)
            lives -= 1