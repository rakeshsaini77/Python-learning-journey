

# Topic: 
# 1.print() function 
# 2.Data Types


# 1.print() function 

print("Hello World")
print(6)
print(False)

print("India", "Pakistan", "Nepal", "SriLanka")

print("India", 5, True)


print("India", "Pakistan", "Nepal", "SriLanka", sep=" | ")

print("India", "Pakistan", "Nepal", "SriLanka", sep=" - ")


print("Hello")
print("World")


print("Hello", end=" ")
print("World")

  #2.DATA TYPES


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

## container data type
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

# User Defined Type

class Student:
    pass

print(type(Student))
