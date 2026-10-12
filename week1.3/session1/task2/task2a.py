# Week 1.3, Session 1: Task 2a

# As written this is an infinite loop.
# If you run it, use <Ctrl>C to exit the running program.
'''
while True:
    k = 2 * k 
    print(k)
'''

# 1. Add a break statement to exit the loop if k>200
'''
k = 2
while True:
    k = 2 * k 
    if k > 200:
        break
    print(k)
'''


# 2. Rewrite the code to directly use the while loop instead of break.
k = 2 
while k < 200:
    print(k)
    k *= 2 
