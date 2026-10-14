# Worksheet 1.2: Task 2 Solution
import sys # for exit 
from util import read_numbers # for user to enter series of number

numbers = read_numbers()

# Exit if no input
if not numbers:
    sys.exit("Error: no numbers provided")

# All statistic required
minimum = min(numbers)
maximum = max(numbers) 
mean = sum(numbers) / len(numbers)

ordered_number = sorted(numbers)
mid = len(numbers) // 2
median = (numbers[mid] + numbers[~mid]) / 2

# Print each statistic in different line
print(f"Minimum =", minimum)
print(f"Maximum =", maximum)
print(f"Mean =", mean)
print(f"Median =", median)