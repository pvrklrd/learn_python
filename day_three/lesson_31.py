"""
if height is greater than 120cm then can ride and buy ticket. 
ticket costs $7 for children below or at 18. ticket cost is $12 if the age is grater tha 18.
finally, children below 120cm height are not allowed.
"""
age = int(input("\n\n\tEnter your age : "))
name = input("\tYour name please : ")
height = int(input("\tWhat's your height in centimeter? : "))

if(height > 120):
    print(f"\n\tHey {name} you can ride and get the ticket")
    if(age > 18):
        print(f"\tYour ticket cost is $12\n")
    elif(age >= 12 and age < 18):
        print(f"\tYour ticket cost is $7\n")
    else:
        print(f"\tYour ticket cost is $5\n")
else:
    print(f"\n\tHey {name} you can't ride. You gotta grow up!\n")
    
