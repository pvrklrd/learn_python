""" Based on a user's order, work out their final bill.
Small Pizza: $15            Medium Pizza: $20           Large Pizza: $25
Pepperoni for Small Pizza: +$2      Pepperoni for Medium or Large Pizza: +$3     Extra cheese for any size pizza: + $1 """

# 🚨 Don't change the code below 👇
print("\n\nWelcome to Python Pizza Deliveries!")
size = input("\tWhat size pizza do you want? S, M, or L ")
add_pepperoni = input("\tDo you want pepperoni? Y or N ")
extra_cheese = input("\tDo you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆
#Write your code below this line 👇
s_prc = 15
m_prc = 20
l_prc = 25
s_pep_prc = 2
ml_pep_prc = 3
chs_prc = 1

def no_pep_no_chs(size):
    if(size=='S'):
        return s_prc
    elif(size=='M'):
        return m_prc
    elif(size=='L'):
        return l_prc
    else:
        print(f"Oops, it seems invalid input!!!")

def pep_n_chs(size):
    if(size=='S'):
        return (s_prc+s_pep_prc+chs_prc)
    elif(size=='M'):
        return (m_prc+ml_pep_prc+chs_prc)
    elif(size=='L'):
        return (l_prc+ml_pep_prc+chs_prc)
    else:
        print(f"Oops, it seems invalid input!!!")

def w_chs_no_pep(size):
    if(size=='S'):
        return (s_prc+chs_prc)
    elif(size=='M'):
        return (m_prc+chs_prc)
    elif(size=='L'):
        return (l_prc+chs_prc)
    else:
        print(f"Oops, it seems invalid input!!!")

def no_chs_w_pep(size):
    if(size=='S'):
        return (s_prc+s_pep_prc)
    elif(size=='M'):
        return (m_prc+ml_pep_prc)
    elif(size=='L'):
        return (l_prc+ml_pep_prc)
    else:
        print(f"Oops, it seems invalid input!!!")

if(add_pepperoni=='Y' and extra_cheese=='Y'):
    total_cost = pep_n_chs(size)
    print(f"Your final bill is: ${total_cost}.")
elif(add_pepperoni=='N' and extra_cheese=='N'):
    total_cost = no_pep_no_chs(size)
    print(f"Your final bill is: ${total_cost}.")
elif(add_pepperoni=='Y' and extra_cheese=='N'):
    total_cost = no_chs_w_pep(size)
    print(f"Your final bill is: ${total_cost}.")
elif(add_pepperoni=='N' and extra_cheese=='Y'):
    total_cost = w_chs_no_pep(size)
    print(f"Your final bill is: ${total_cost}.")
else:
    print(f"Oops, it seems invalid input!!!")