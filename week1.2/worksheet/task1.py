# Worksheet 1.2: Task 1 Solution
import sys # for exit
user_grade = input("please enter your grade (0-100): ")

# Check if the input contain characters
if not user_grade.isdecimal():
    sys.exit("Error: Grade must be an integer between 0 and 100")

user_grade_ = int(user_grade)

# Check if the input is in betwwen 0 to 100
if user_grade_ < 0 or user_grade_ > 100: 
    sys.exit("Error: Grade must be an integer between 0 and 100")

# Clasify the grade
if user_grade_ <= 39:
    result = "Fail"
elif user_grade_ <= 69:
    result = "Pass"
else:
    result = "Distinction"

print(f"{user_grade_} is a {result}")           


    