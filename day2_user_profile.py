# Day 2 - Variables, Input, Type Casting, If-Else

print("---- User Profile Generator ----")

# Taking user input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
state = input("Enter your state: ")
fav_language = input("Enter your favorite programming language: ")

# Processing
age_after_5_years = age + 5

print("\n---- User Profile ----")
print(f"Name: {name}")
print(f"Age after 5 years: {age_after_5_years}")
print(f"State: {state}")
print(f"Favorite Language: {fav_language}")

# Eligibility check
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

