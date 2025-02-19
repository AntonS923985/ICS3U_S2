print("Welcome to the even or odd detector!")

print("This program can determine if the product of two numbers is even or odd!") # Informs the user of what the program does

num1 = int(input("Please enter a number:")) 

num2 = int(input("Please enter another number:"))

# Classified both variables as int data types

product = num1*num2

product = int(product)

rem = product % 2 # Divides the product of multiplication by 2 to check if it is even or odd based on the remainder

if(rem == 0):
    print("The product of", num1, "times", num2, "is an even number.")
else:
    print("The produce of", num1, "times", num2, "is an odd number.")
