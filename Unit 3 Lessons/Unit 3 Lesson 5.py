# Unit 3, Exercise 5: Intro to Subprograms: Functions
#
# Place your code below!

"""
Predict: I believe this code will add the numbers 7 and 2, and 
print them in a float data type.

def add(a: float, b: float) -> float:
   sum = a + b
   return sum

print(add(7, 2))
"""


# Modify 1
"""
# Print them in a float data type.

def add(a: float, b: float) -> float:
   sum = a + b
   return sum

sum = add(7.0, 2.0)
print(sum)
"""

# Modify 2

def myAbs(n):
    if n < 0:
      return -n
    else:
      return n
b = -12
a = myAbs(b)
print("The absolute value of %d is %d" % (b, a))
