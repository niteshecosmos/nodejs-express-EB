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
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to Treasure Island")
print("Your misson to find the treasure")
choice1 = input('You\'re at a cross road. Where do you want go ?Type "Left" or "right" \n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake.Type "wait" to wait for the bike. Type "swim" to across. \n').lower()
    if choice2 == "swim":
        choice3 = input('You are arrive at the island unharmed. There is a house with 3 doors.One red, one yellow and one blue.Which colour do you choose? \n').lower()
        if choice3 =="red":
            print("Burned by fire Game Over.")
        elif choice3 =="yellow":
            print("You found the treaure! You Win.")
        elif choice3 == "Blue":
            print("Eaten by beasts.Game Over.")
        else:
            print("You are chose a door that dosen't exist.Game Over.")       
    else:
        print("Attacked by trout.Game Over")
else:    
    print("Fall into a hole. Game Over")

   
 