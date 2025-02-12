"""
I think that the code will ask for two variables, x & y, then assign
the int data type. It will then tell the user it is checking if y
is a factor of x, by checking if the remainder from division is zero. 
if it is zero, it will tell the user that y is a factor, if it is 
not zero, it will not print anything else. if i input x = 6,
and y = 3, i expect it to say that it is a factor of 6. if i 
input x = 6 and y = 5, i expect the code to stop executing.
"""

import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
print("Now deciding if", y, "is a factor of", x, "...")
rem = x % y
if rem == 0:
    print("Yes!", y, "is a factor of", x)

# the code did match what i did on my calculator.

# Modify

import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
if(y != 0):
  rem = x % y
  if rem == 0:
    print("Yes!", y, "is a factor of", x)

# Modify 2

import math

x = input("Please input a whole number: ")
x = int(x)
y = input("Please input another nonzero whole number")
y = int(y)
if(y != 0):
  rem = x % y
  if rem == 0:
    print("Yes!", y, "is a factor of", x)
else:
    print("You cannot divide by zero. Please enter a non-zero number.")

# Modify 3

import math

x = input("Please input a whole number between 1 and 20: ")
x = int(x) # x must be defined as an integer data type before it can undergo a greater or less than check
if ((x < 1 or x > 20)):
    print("Error: The number must be between 1 and 20. Try again.")
else:
    y = input("Please input another nonzero whole number between 1 and 20:")
    y = int(y) # y must also be defined as an integer data type before undergoing math equations or a greater or less than check
    if ((y < 1 or y > 20)): 
        print("Error: The number must be between 1 and 20. Try again.")
    else:
      print("Now deciding if", y, "is a factor of", x, "...")
      if y != 0:  # This is still checked, but y cannot be 0 due to the range limit
            rem = x % y
            if rem == 0:
                print("Yes!", y, "is a factor of", x)
            else:
                print("No,", y, "is not a factor of", x, "...")
# Make sure all indents line up
