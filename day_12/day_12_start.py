################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")


# Local scope 
# Exixst within functions

# def drink_potion():
#     '''Increases player strength'''
#     potion_strenght = 2
#     print(potion_strenght) 

# drink_potion()
# print(potion_strenght)

# GLbal scope
player_health = 10

