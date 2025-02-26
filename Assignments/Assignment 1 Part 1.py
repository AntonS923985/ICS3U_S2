print("Welcome to the even or odd detector!") # Welcomes the user to the program

print("This program can determine if the product of two numbers is even or odd!") # Informs the user of what the program does

num1 = int(input("Please enter a number:")) # Requests an input from the user

num2 = int(input("Please enter another number:")) # Requests another number from the user

# Classified both variables as int data types

if(num1 % 2 == 0 and num2 % 2 == 0): # Preforms a check if both inputted values have a remainder of zero when divided by two
  print("The product of", num1, "and", num2, "will be an even number.") # Prints if both values have a remainder of two
  
elif(num1 % 2 == 1 and num2 % 2 == 0) or (num1 % 2 == 0 and num2 % 2 == 1): # Checks if one number has a remainder of zero when divided by two and if one has zero, both numbers checked
  print("The product of", num1, "and", num2, "will be an even number.") # Prints if one number has a remainder of zero when divided by two and if one has a remainder of zero.
  
elif(num1 % 2 == 1 and num2 % 2 == 1): # Checks if both inputted values have a remainder of one if divided by zero if the previous if and elif statements are false.
  print("The product of", num1, "and", num2, "will be an odd number.") # Prints if both numbers have a remainder of one if divided by two
