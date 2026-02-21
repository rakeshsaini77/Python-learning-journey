# Correct Email: campusx@gmail.com
# Correct Password: 1234

email = input("Apna email batao: ")

# Step 1: Email check
if email == "campusx@gmail.com":
    
    password = input("Apna password batao: ")
    
    # Step 2: Password check
    if password == "1234":
        print("Welcome 🎉")
    
    else:
        print("Password Incorrect ")
        
        # Second chance for password
        password = input("Password fir se bolo: ")
        
        if password == "1234":
            print("Finally Correct  Welcome!")
        else:
            print("Still Incorrect Access Denied")

else:
    print("Email galat hai  Pehle sahi email likho")


## indentaion:
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even number")
else:
    print("Odd number")
