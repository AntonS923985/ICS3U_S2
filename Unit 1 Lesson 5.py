"""
I predict that on the first line of code, the python math function
will be imported. On the second line, I think that the user will be
asked to input a value to assign to the variable "length".
I think the code will then classify the value inputted as a floating
point. The code will then use the math function we imported to 
square the value of length, using math.pow. It will then print the 
value it calculated.
"""

import math
length = input("Please input a length: ")
length = float(length)
area = math.pow(length, 2)
print("The area of a square of side length", length, "is:", area)

"""
It stopped executing code because there were no more lines of 
code to run. I inputted the integer 90, and I got 8100, which is 
accurate to what i got on my calculator.
"""

#Modify

import math
radius = input("Please input a radius: ")
radius = float(radius)
areasemicircle = 0.5*math.pi*math.pow(radius, 2)
areasquare = 4*math.pow(radius, 2)
areatotal = areasemicircle + areasqare
print("The total area of the window is", areatotal)
