"""
if height is greater than 120cm then can ride and buy ticket. 
ticket costs $7 for children below or at 18. ticket cost is $12 if the age is grater tha 18.
finally, children below 120cm height are not allowed. 
Add addition $3 whoever needs a photograph
"""
age = int(input("\n\n\tEnter your age : "))
name = input("\tYour name please : ")
height = int(input("\tWhat's your height in centimeter? : "))

if(height > 120):
    print(f"\n\tHey {name} you can ride and get the ticket")
    if(age > 45 and age < 55):
        if(input("Do you need a photograph? Answer 'yes' or 'no'") == "yes"):
            print(f"Its costs addition $3 and the the total cot is : $3")
        else:
            print(f"\tWe offer free of cost ticket and please enjoy your ride\n")
    elif(age > 18 and age <= 45):
        if(input("Do you need a photograph? Answer 'yes' or 'no'") == "yes"):
            print(f"Its costs addition $3 and the the total cot is : $15")
        else:
            print(f"\tYour ticket cost is $12\n")
    elif(age >= 12 and age < 18):
        if(input("Do you need a photograph? Answer 'yes' or 'no'") == "yes"):
            print(f"Its costs addition $3 and the the total cot is : $10")
        else:
            print(f"\tYour ticket cost is $7\n")
    else:
        if(input("Do you need a photograph? Answer 'yes' or 'no'") == "yes"):
            print(f"Its costs addition $3 and the the total cot is : $8")
        else:
            print(f"\tYour ticket cost is $5\n")
else:
    print(f"\n\tHey {name} you can't ride. You gotta grow up!\n")