import os
import art
print(art.logo)
print("================Welcome to the Blind Auction.=======================")

bids = {}

bidding_finished = False

def find_highest_bidder(bidding_record):
    winner = ""
    highest_bid = 0
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding_finished:
    name = input("What is your name?: ")
    price = int(input("What is your bid?: $"))
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no'").lower()
    if should_continue == "no":
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == "yes":
        os.system('cls')
        
        


# auction = {}
# def add_auction():
#     user_name = input("Please enter your username: \n").capitalize()
#     print(f"{user_name},Welcome to secret Auction Program")
#     bid = input("What is your bid price?")
#     auction[user_name] = bid

# add_auction()
# next_person = input("Is there any other bidder? 'Yes' or 'No' ").lower()
# wrong_input = False
# while wrong_input == False:
#     if next_person == "yes":
#         os.system('cls')
#         add_auction()

#     elif next_person == "no":
#         for x in auction:
#             largest_bid = 0
#             if largest_bid < auction[x]:
#                 largest_bid = auction[x]
#         print(f"{[x]} bid {largest_bid}")
            
#     else:
#         print("Sorry you made a wrong input. Try again")
#         wrong_input = True
#HINT: You can call clear() to clear the output in the console.

# os.system('cls')  # on windows