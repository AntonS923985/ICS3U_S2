import math

print("This program will find the inner diagonal for any edge length provided!") # Informs the user of what the program does

length = int(input("Please input any non-zero number for the edge length of your cube:"))
if(length == 0):
    print("Edge length of zero will result in zero! Please try again.") # included error message in case zero is inputted
else:
    diagonal = length * math.sqrt(3)
    print("The inner diagonal length for a cube with a side length of", length, "is %.2f" % diagonal) # Prints the value of the diagonal, using %.2f to substitute the string and round to 2 decimal places.
