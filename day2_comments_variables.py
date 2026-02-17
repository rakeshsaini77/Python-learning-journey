## Day 2 
# Topice covered:
# 1.comments
# 2.variables

# coments

# This is a single line comment

# Program to print a message
print("Hello Rakesh")



# Inline comment example

age = 17  # Storing age value
name = "Rakesh"  # Storing name

print("Name:", name)
print("Age:", age)


"""
This is a multi-line comment example.
It explains the purpose of this program.
Python ignores this block during execution.
"""

print("This program demonstrates multi-line comments.")


## 2. variable and Typing 

# Variable Declaration
a = 5
b = 6
c = 7

print("Value of a:", a)
print("Value of b:", b)
print("Value of c:", c)

# Multiple Assignment
x, y, z = 4, 5, 6

print("Value of x:", x)
print("Value of y:", y)
print("Value of z:", z)


# Python is dynamically typed
num = 10
print("num:", num, "Type:", type(num))

num = "Rakesh"
print("num:", num, "Type:", type(num))





#  Simple Function (Static Binding concept explanation)
def greet():
    print("Hello Rakesh")

greet()


# - Dynamic Binding (Method Overriding)

class A:
    def show(self):
        print("Class A")

class B(A):
    def show(self):
        print("Class B")

obj = B()
obj.show()   # Runtime decides which method to call


