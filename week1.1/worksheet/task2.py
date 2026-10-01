"""
Portfolio Task - Week 1
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: 
"""

name = input("What is your name? ")
print(f"Welcome to LeedsBank's savings calculator {name}!")

# Ask the user to input an amount they want to save every month - this should be an integer.
# Validate that they have entered an integer.
x = 0
while x==0:
    try:
        money = int(input("please enter the amount you want to save every month: "))
        x = 1
    except ValueError:
        print("Invalid input, please enter a whole number greater 0!")    

# Calculate the total amount of money they will have saved by the end of the year (amount per month multiplied by 12).
total = money * 12
# print this out for the user with a suitable message.
print (f"after 12 months, your total is {total}")

# Calculate the total amount of money including interest (0.8% of the final annual amount) they will have saved in a year.
new_total = total * 1.008
# print this out in the format £X.XX (to two decimal places).
print(f"your total amount after your interest is £{new_total:.2f}")


