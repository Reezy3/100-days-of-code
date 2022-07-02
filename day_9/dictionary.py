programming_dictionary = {
    "Bug" : "An error in a program that prevents the program from running as expected.",
    "Function" : "A piece of code that you can easily call over and over again.",
    "Loop" : "The action of doing something over and over again."
}

print(programming_dictionary["Bug"])

# Adding a new entry
programming_dictionary["Boy"] = "A male child"
print(programming_dictionary)

# Empty dictionary
empty_dictionary = {}

# # Wipe an existing dictionary
# programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through a dictionary
for x in programming_dictionary:
    print(x)
    print(programming_dictionary[x])