print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

round_1 = (input("You are running from the mafia who you stole money from you are at crossroads what direction will you take right or left? \n")).lower()


if round_1 == "left":
 print("Welcome to stage 2!!!")
 round_2 = (input("You get home and your side piece comes over and wants to swim before your girl gets home but you have no swimwear to join her, what do you do wait or swim? \n")).lower()
 if round_2 == "wait":
  print("She decides to not swim and have a drink with you")
  round_3 = (input("She tells you to pick a colour that she has a suprise for you, what do you pick? red, blue or yellow\n")).lower()
  if round_3 == "yellow":
   print("She drops her clothes and takes your hand upstairs, YOU WIN!!!")
  elif round_3 == "blue":
   print("She slaps your face and tells you she knows about your other girls, YOU LOSE!!")
  else:
   print("She sprays sleeping gas and robs you YOU LOSE!!!") 
 else:
  print("You get frostbite and die!!! YOU LOSE SUCKER!!!")
  
  
else:
 print("You get ran over by a car! YOU LOSE..")