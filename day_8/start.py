# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
    print("Welcome to day 8 of learning")
    print("I'm Arinze and I will keep improving")
    print("I hope to get really good at programming")   
    
greet()

# Function that allows input
# def greet_with_name(name):
#     print(f"Welcome {name} to day 8 of learning")
#     print(f"How do you do {name}?")
    
# greet_with_name("Ben")
  
  
# Functions with more than one input
def greet_with(name, location):
    print(f"Hello {name} ")
    print(f"What is it like in {location}?")

greet_with("Arinze", "Nigeria")   


# Functions with keyword arguments
user_name = input("Please enter your name: ")
user_location = input("Please enter your location: ")
def vote_change(voter_name = user_name , voter_location = user_location):
    print(f"Hello {voter_name} please vote for change")
    print(f"Vote at {voter_location} for a better tomorrow ")
    
    
vote_change()