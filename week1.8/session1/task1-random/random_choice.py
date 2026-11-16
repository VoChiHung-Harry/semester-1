import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices
user = int(input("please enter a number: "))
chosen = random.sample(names,user)

# Display the chosen names, one per line
for name in chosen:
    print(name)