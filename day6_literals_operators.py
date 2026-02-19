
## Day 4 
#Topic covered:
#1.Literals 
#2.Operators


#1.Literals
##  Numeric Literals

# Integer Literals
a = 0b1010     # Binary literal (10 in decimal)
b = 100        # Decimal literal
c = 0o310      # Octal literal (200 in decimal)
d = 0x12C      # Hexadecimal literal (300 in decimal)

print("Integer Literals:")
print(a, b, c, d)

# Float Literals
float_1 = 10.5
float_2 = 1.5e2    # 150.0
float_3 = 1.5e-3   # 0.0015

print("\nFloat Literals:")
print(float_1, float_2, float_3)

# Complex Literal
x = 3.14j
print("\nComplex Literal:")
print(x)


## String Literals



string1 = 'This is Python'
string2 = "This is Python"
char = 'C'

multiline_str = """This is a
multiline
string"""

raw_str = r"This is raw \n string"

print(string1)
print(string2)
print(char)
print(multiline_str)
print(raw_str)


## Boolean Literals


a = True + 4
b = False + 10

print("a:", a)
print("b:", b)


##Special Literal



a = None
print(a)



# 2. OPERATORS



x = 10
y = 3

# Arithmetic Operators
print("\nArithmetic Operators:")
print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Modulus:", x % y)
print("Exponent:", x ** y)
print("Floor Division:", x // y)

# Comparison Operators
print("\nComparison Operators:")
print(x > y)
print(x < y)
print(x == y)
print(x != y)

# Logical Operators
print("\nLogical Operators:")
print(True and False)
print(True or False)
print(not True)

# Assignment Operator
print("\nAssignment Operator:")
z = 5
z += 2
print("z:", z)

# Identity Operator
print("\nIdentity Operator:")
a = [1, 2]
b = a
print(a is b)

# Membership Operator
print("\nMembership Operator:")
print(2 in a)
print(5 not in a)

