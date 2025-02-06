"""
I predict the user will be asked to input a whole number, meaning 
no decimals. For the second line, I think that the number that was 
inputted will be assigned to the variable "num", which will be 
classified as an integer data type because it has "int" in front of it.
For the third line, I predict that the variable "num2" will represent 
the number entered by the user divided by 6. On the fourth line of code,
I predict that it will print the result of the number entered divided by 6.
"""

num = input("Please input a whole number: ") 
num = int(num) 
num2 = num / 6
print("When", num, " is divided by 6", "the result is:", num2)

"""
The code stopped the execution because it reached the final line.
I inputted the number 90, and it did match when I tested it in a
calculator, the result was 15.
"""

num = input("Please input a whole number: ") 
num2 = input("Please input any whole number except for zero.")
num = int(num)
num2 = int(num2)
num3 = num / num2
print("When", num, " is divided by", num2, "the result is:", num3)

"""
The instrution specifies not to put zero into the input for num2
because you cannot divide by 0, and it will just output an error.
"""
