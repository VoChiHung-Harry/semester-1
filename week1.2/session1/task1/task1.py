# Week 1.2, Session 1: Task 1

# Create a shopping list

shopping = ["eggs", "milk", "flour", "carrots"]
print(shopping)

# We forgot something, so add it to list

shopping.append("bananas")
print(shopping)

# We bought something, so remove it from list

shopping.remove("eggs")
print(shopping)

# Replace bananas with grapes
index_bananas = shopping.index("bananas")
print(index_bananas)
shopping[3]= "grapes"
print(shopping)

# Add yoghurt, just after milk
index_milk = shopping.index("milk")
print(index_milk)
shopping.insert(1,"yoghurt")
print(shopping)