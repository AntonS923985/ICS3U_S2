print("Welcome to the even or odd detector!")

print("This program can determine if the product of two numbers is even or odd!")

num1 = int(input("Please enter a number:"))

num2 = int(input("Please enter another number:"))

product = num1*num2

product = int(product)

rem = product % 2

if(rem == 0):
    print("The product of", num1, "*", num2, "is an even number.")
else:
    print("The produce of", num1, "*", num2, "is an odd number.")
