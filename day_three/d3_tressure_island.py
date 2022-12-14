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
print("\n\tWelcome to Treasure Island.")
print("\tYour mission is to find the treasure.") 
#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
#Write your code below this line 👇
if(input("\tWhich way you wanna go? Type 'Left' or 'Right' : \t").lower() == 'right'):
    print(f"\n\tWow! You reached the Temple 🛕.")
    if(input("\tWhich way you wanna go? Type 'Left' or 'Right' : \t").lower() == 'right'):
        print(f"\n\tYou reached the river 🌊.")
        if(input("\tDo you wanna swim or wait for the boat to pick you up? Type 'Swim' 🏊‍♀️ or 'Wait' 🚣 : \t").lower() == 'swim'):
            print(f"\tAppreciate your courage 👏 and you reached destination. But one final thing. Here you have three boxes and you have to pick one.")
            if(input("\tType 'Green' or 'Red' or 'Blue' : \t").lower() == 'green'):
                print(f"\t🎉 Yay..!!! 🎊 You are a brave 💪 and good hearted 💝 person and here is your reward inside the box 🎁 🏆!")
            elif(input("\tType 'Green' or 'Red' or 'Blue' : \t").lower() == 'blue'):
                print(f"\tOops! Wrong one and start from the scratch again. Game over...!!! 👾")
            else:
                print(f"\tOh my God! that's horrible. the box is full of venomour creatures 🐍 🦂 🪱. Game over...!!! 👾")
        else:
            print(f"\tPay for it - Here comes venomous snakes 🐍🐍. Game over...!!! 👾")
    else:
        print(f"\tYou took a wrong turn 👺 and start from the scratch now. Game over...!!! 👾")
else:
    print(f"\tThat's a 'Death Whole' 🥶☠️ and you reached the Heaven..! Game over...!!! 👾")