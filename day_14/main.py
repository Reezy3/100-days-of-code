from art import logo, vs
from game_data import data
import random
import os

def format_data(account):
    """Format the account data into a printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]

    return(f" {account_name}, a {account_description}, from {account_country}")

def check_answer(guess, a_followers, b_followers):
    """Take user guess and follower counts and returns if they got it right."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

# Display art
print(logo)

score = 0
game_should_continue = True
account_b = random.choice(data)

# Make the game repeatable.
while game_should_continue:

    # Generate random account
    account_a = account_b
    account_b = random.choice(data)
    
    while account_a == account_b:
        account_b = random.choice(data) 

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # check if user is correct
    # # get follower count of each account.
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # Clear the screen
    os.system('cls')
    print(logo)
    # Give user feedback on their guess
    # Score keeping
    if is_correct:
        score += 1 
        print(f"Yayy! You got it right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry you got it wrong. Final score: {score} ")




# Make account at position B become the next account at position A if right

# Clear the screen # os.system('cls')


    
    

