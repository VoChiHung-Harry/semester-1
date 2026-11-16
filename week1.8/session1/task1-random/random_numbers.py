import random

# Get user to input how many random numbers they want
number = int(input("please enter a number: "))
# Generate this many random numbers
k = random.choices(range(0,101),k=number)

# Write the random numbers to a file named random.txt, one number per line
with open("random.txt","w") as outfile:
    for n in k:
        outfile.write(f"{n}\n")