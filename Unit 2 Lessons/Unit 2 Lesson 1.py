"""
I predict that the code will print the output statement "I prefer
cherries."
"""

print("Make a choice from the following menu: ")
print("A: apples")
print("B: bananas")
print("C: cherries")

ch = input("Your choice: ")

if (ch == "A"):
    print("I prefer apples")
elif (ch == "B"):
    print("I prefer bananas")
else:
    print("I prefer cherries")

"""
The program does do what i predicted it would do. If you
enter anything other than the provided choices, such as a dollar
or a comma, it will just default to cherries. This issue is that
all inputs other than A and B will result in an output of 
"I prefer cherries" even though C is the only intended valid input.
"""

# Modify 1

valid = False
while not valid:
    print("Make a choice from the following menu: ")
    print("A: apples")
    print("B: bananas")
    print("C: cherries")
    ch = input("Enter your choice: ")
    valid = (ch == "A" or ch == "B" or ch == "C")
    if(ch == "A"):
      print("I prefer apples.")
    if(ch == "B"):
      print("I prefer bananas.")
    if(ch == "C"):
      print("I prefer cherries.")
    if not valid:
      print("Input not recognized. Please try again.")

# Modify 2

print (input("Welcome to the grade calculator! Please input your grade in percent format:"))
input = int(grd)
valid = False
while not valid:
  if(grd)
