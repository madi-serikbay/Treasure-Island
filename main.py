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


#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 
choice1 = input('Choose: "Left" or "Right"?').lower()
if choice1 == "Left" or choice1 == "left" or choice1 == "LEFT":
  print(choice1)
  choice2 = input('Choose: "Swim" or "Wait"?').lower()
  if choice2 == "Wait" or choice2 == "wait" or choice2 == "WAIT":
    print(choice2)
    choice3 = input('Choose door color: "Red", "Blue", "Yellow"?').lower()
    if choice3 == "Yellow" or choice3 == "yellow" or choice3 == "YELLOW":
      print("You Win!")
    elif choice3 == "Red" or choice3 == "red" or choice3 == "RED":
      print("Burned by fire. Game Over.")
    elif choice3 == "Blue" or choice3 == "blue" or choice3 == "BLUE":
      print("Eaten by beasts. Game Over")
    else:
      print("Game Over")
  else:
    print("Attacked by trout. Game Over.")
else:
  print("Fall into a hole. Game Over.")