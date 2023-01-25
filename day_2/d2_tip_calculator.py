#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
#Write your code below this line 👇

bill_amt = float(input("\n\nEnter the bill amount $:"))
no_of_ppl = int(input("How many of you would like to share the bill amount :"))
tip_percent = int(input("\nHow much tip you wanna offer. Select one among the choices based on percentage given below \
\n\t\t10 for 10%\n\t\t12 for 12%\n\t\t15 for 15% \nEnter the percentage : "))

idvl_bill_amt = (bill_amt+(bill_amt*tip_percent/100))/no_of_ppl

print(f"\nThe equal share for {no_of_ppl} persons is ${idvl_bill_amt:.2f} for the bill amount ${bill_amt:.2f} \
along with ${(bill_amt*tip_percent/100):.2f} tip.\n")
