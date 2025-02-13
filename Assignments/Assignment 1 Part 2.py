import math

print("This program will find the inner diagonal for any edge length provided!")

length = int(input("Please input any non-zero number for the edge length of your cube:"))
if(length == 0):
    print("Edge length of zero will result in zero! Please try again.")
else:
    diagonal = length*math.sqrt(3)
    print("The inner diagonal length for a cube with a side length of", length, "is", diagonal)
