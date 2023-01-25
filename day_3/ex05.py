""" To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE occurs. 
Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number. """
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("\nWhat is your name? \n\t")
name2 = input("What is their name? \n\t")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1.lower() + name2.lower()

true_score = name.count('t') + name.count('r') + name.count('u') + name.count('e')
love_score = name.count('l') + name.count('o') + name.count('v') + name.count('e')
overall_score = int(str(true_score)+str(love_score))

if(overall_score < 10 or overall_score > 90):
    print(f"Your score is {str(true_score)+str(love_score)}, you go together like coke and mentos.")
elif(overall_score > 40 and overall_score < 50):
    print(f"Your score is {str(true_score)+str(love_score)}, you are alright together.")
else:
    print(f"Your score is {str(true_score)+str(love_score)}.")