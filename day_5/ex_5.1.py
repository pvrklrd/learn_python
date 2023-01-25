import os
def clear_the_console_screen():
    if(os.name == 'nt'):
        os.system('cls')
    else:
        os.system('clear')

clear_the_console_screen()

std_hts = input("Input a list of student heights : ").split(",")
tot_ht = 0
stds = 0
for hts in std_hts:
    tot_ht += int(hts)
    stds += 1
avg_ht = round(tot_ht/stds)
print(f"\n\tThere are {stds} students in the class and their avergae height is : {avg_ht}.\n")