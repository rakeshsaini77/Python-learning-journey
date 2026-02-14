
# Day 1 - Python Basics
# Topic: print() function & Data Types

# PRINT FUNCTION


print("Hello World")
print(6)
print(False)

print("India", "Pakistan", "Nepal", "SriLanka")

print("India", 5, True)

# Using separator
print("India", "Pakistan", "Nepal", "SriLanka", sep=" | ")

print("India", "Pakistan", "Nepal", "SriLanka", sep=" - ")

# Default new line behavior
print("Hello")
print("World")

# Using end parameter
print("Hello", end=" ")
print("World")

# DATA TYPES

# 1️⃣ Basic Types

# Integer
print(4)
print(type(4))

# Float
print(4.5)
print(type(4.5))

# Boolean
print(True)
print(False)
print(type(True))

# Complex
print(4 + 5j)
print(type(4 + 5j))

# String
print("Rajasthan")
print('Rajasthan')
print("""Rajasthan""")
print(type("Rajasthan"))

# 2️⃣ Container Types


# List
print([1, 2, 3, 4, 5])
print(type([1, 2, 3, 4, 5]))

# Tuple
print((1, 2, 3, 4, 5))
print(type((1, 2, 3, 4, 5)))

# Set
print({1, 2, 3, 4, 5})
print(type({1, 2, 3, 4, 5}))

# Dictionary
student = {
    "Name": "Rakesh",
    "Age": 20
}
print(student)
print(type(student))

# 3️⃣ User Defined Type

class Student:
    pass

print(type(Student))
