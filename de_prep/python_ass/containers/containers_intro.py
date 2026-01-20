'''Containers (Overview)
 Project: containers_intro.py 
 Create and use: list tuple dict set 
Show: indexing key access uniqueness in set help me with these project '''

# LIST
# Ordered, mutable, allows duplicates
fruits = ["apple", "banana", "cherry", "banana"]

print("List:", fruits)
print("First item (indexing):", fruits[0])
print("Last item (indexing):", fruits[-1])

# Modify list
fruits.append("orange")
print("After append:", fruits)


# TUPLE
# Ordered, immutable, allows duplicates
coordinates = (10, 20, 10, 41)

print("\nTuple:", coordinates)
print("X coordinate (indexing):", coordinates[0])
print("Y coordinate (indexing):", coordinates[-1])

# coordinates[0] = 5  # This would crash. Tuples cannot be modified.


# DICTIONARY
# Key-value pairs, keys must be unique
student = {
    "name": "Mawa",
    "program": "Data Engineering",
    "country": "Canada"
}

print("\nDictionary:", student)
print("Name (key access):", student["name"])
print("Program.get (key access):", student.get("program"))
print("Program (key access):", student["program"])

# Update value
student["program"] = "Data Analytics"
print("Updated dictionary:", student)

#print(student["age"])      # ❌ CRASHES
print(student.get("age"))      # Return None

# SET
# Unordered, mutable, NO duplicates
numbers = {1, 2, 3, 3, 2, 1}

print("\nSet:", numbers) # Notice duplicates are removed automatically

# Add item
numbers.add(4)
print("After adding 4:", numbers)
