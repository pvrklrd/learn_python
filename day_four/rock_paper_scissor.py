import random as r
import os
# 0 - Rock             # 1 - Paper              # 2 - Scissors

def clear_the_console_screen():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

clear_the_console_screen()

u_choice = int(input(f"\n\t'0' for Rock  🪨  \n\t'1' for Paper  🧻  \n\t'2' for Scissor  ✂️  \n\n\t\tEnter your choice : "))
c_choice = r.randint(0,2)

if(u_choice == 0):
    if(c_choice == 0):
        print(f"\n\tBoth chose  🪨   and the match tied\n")
    elif(c_choice == 1):
        print(f"\n\tYou chose  🪨   and the computer chose  🧻  . Compueter wins!\n")
    else:
        print(f"\n\tYou chose  🪨   and the computer chose  ✂️  . You win!\n")
elif(u_choice == 1):
    if(c_choice == 0):
        print(f"\n\tYou chose  🧻   and the computer chose  🪨  . You win!\n")
    elif(c_choice == 1):
        print(f"\n\tBoth chose  🧻   and the match tied\n")
    else:
        print(f"\n\tYou chose  🧻   and the computer chose  ✂️  . Computer wins!\n")
else:
    if(c_choice == 0):
        print(f"\n\tYou chose  ✂️   and the computer chose  🪨  . Computer wins!\n")
    elif(c_choice == 1):
        print(f"\n\tYou chose  ✂️   and the computer chose  🧻  . You win!\n")
    else:
        print(f"\n\tBoth chose  ✂️   and the match tied\n")