import os

if(os.name == 'nt'):
    os.system('cls')
else:
    os.system('clear')

print(f"\n\tWelcome to Treasure Island. Your mission is to find the treasure 👍 👍 👍")
if(input("\n\tWhich way you wanna go? Type 'Left' or 'Right' : \t").lower() == 'right'):
    print(f"\n\tWow! You reached the Temple 🛕 .")
    if(input("\n\tWhich way you wanna go? Type 'Left' or 'Right' : \t").lower() == 'right'):
        print(f"\n\tYou reached the river 🌊 .")
        if(input("\n\tDo you wanna swim or wait for the boat to pick you up? Type 'Swim' 🏊‍♀️ or 'Wait' 🚣 : \t").lower() == 'swim'):
            print(f"\n\tAppreciate your courage 👏 and you reached destination. But one final thing. Here you have three boxes and you have to pick one.")
            if(input("\n\tType 'Green' or 'Red' or 'Blue' : \t").lower() == 'green'):
                os.system('cls')
                print(f"\n\t 🎉 Yay..!!! 🎊 You are a brave 💪 and good hearted 💝 person and here is your reward inside the box 🎁  🏆!\n\n")
            elif(input("\n\tType 'Green' or 'Red' or 'Blue' : \t").lower() == 'blue'):
                print(f"\n\tOops! Wrong one and start from the scratch again. Game over...!!! 👾")
            else:
                print(f"\n\tOh my God! that's horrible. the box is full of venomour creatures 🐍  🦂  🪱. Game over...!!! 👾")
        else:
            print(f"\n\tPay for it - Here comes venomous snakes 🐍 🐍. Game over...!!! 👾")
    else:
        print(f"\n\tYou took a wrong turn 👺 and start from the scratch now. Game over...!!! 👾")
else:
    print(f"\n\tThat's a 'Death Whole' 🥶 ☠️ and you reached the Heaven..! Game over...!!! 👾")