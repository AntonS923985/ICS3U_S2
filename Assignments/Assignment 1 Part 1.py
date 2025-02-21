print("Welcome to the even or odd detector!") # Welcomes the user to the program

print("This program can determine if the product of two numbers is even or odd!") # Informs the user of what the program does

num1 = int(input("Please enter a number:")) # Requests an input from the user

num2 = int(input("Please enter another number:")) # Requests another number from the user

# Classified both variables as int data types

product = num1*num2 # Multiplies the two numbers entered by the user

product = int(product) # Classifies the product of the previous multiplication as an int data type

rem = product % 2 # Divides the product of multiplication by 2 to check if it is even or odd based on the remainder

if(rem == 0): # Checks if remainder is zero
    print("The product of", num1, "times", num2, "is an even number.") # Prints that the product is even if previous statement is true
else: # Checks if remainder is not zero
    print("The produce of", num1, "times", num2, "is an odd number.") # Prints that the product is odd if the statement on like 17 is false
