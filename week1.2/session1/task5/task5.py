# Week 1.2, Session 1: Task 5

rivers = {
    "London": "Thames",
    "Leeds": "Aire",
    "Liverpool": "Mersey"
}

print(rivers)

# Add two new entries to the rivers database
rivers["Leeds"]= "Aire"
rivers["Manchester"] = "Irwell"

# Display all the keys
print(rivers)
print(rivers.keys())

# Display all the values
print(rivers.values())

# Display all the key:value pairs, as tuples
print(list(rivers))

# Delete an entry from the rivers database
