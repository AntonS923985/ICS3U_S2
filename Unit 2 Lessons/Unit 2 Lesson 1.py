"""
I predict that the code will print the output statement "I prefer
cherries."
"""

# Original Code

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
The program does do what I predicted it would do. If you
enter anything other than the provided choices, such as a dollar
or a comma, it will just default to cherries. This issue is that
all inputs other than A and B will result in an output of 
"I prefer cherries" even though C is the only intended valid input.
"""

# Modify 1

valid = False # Sets valid to false 
while not valid: # Sets a loop that runs if a valid choice is not made
    print("Make a choice from the following menu: ") # Provides instructions and choices to the user
    print("A: apples")
    print("B: bananas")
    print("C: cherries")
    ch = input("Enter your choice: ") # Asks the user for a choice
    valid = (ch == "A" or ch == "B" or ch == "C") # Lists valid choices so the program knows which ones will not run the loop again
    if(ch == "A"):
      print("I prefer apples.") # Response to choice "A"
    if(ch == "B"):
      print("I prefer bananas.") # Response to choice "B"
    if(ch == "C"):
      print("I prefer cherries.") # Response to choice "C'
    if not valid:
      print("Input not recognized. Please try again.") # Error statement for inputs other than "A", "B", or "C"

# Modify 2

valid = False # Sets valid to false
while not valid:
    grd = int(input("Welcome to the grade calculator! Please input your grade in percent format:")) # Informs the user of what the program is and instructs on what to do
    valid = (grd >= 0 and grd <= 100) # Sets valid input to values greater or equal to zero and less that or equal to 100
    if not valid:
      print("Your grade cannot be below 0 or above 100! Please enter a valid input.") # Error statement for bad inputs
if(grd >= 80 and grd <= 100): 
    # Checks if input is equal to or greater than 80 and equal to or less than 100
  print("You have an A! you must be proud!") # If the previous check is true, then this is printed.
if(grd >= 70 and grd <= 79): 
    # Checks if input is equal to or greater than 70 and equal to or less than 79
  print("You have an B! Good work!") # If the previous check is true, then this is printed.
if(grd >= 60 and grd <= 69): 
    #Checks if input is equal to or greater than 60 and equal to or less than 69
  print("You have a C! Try a bit harder next time.") # If the previous check is true, then this is printed.
if(grd >= 50 and grd <= 59): 
    # Checks if input is equal to or greater than 50 and equal to or less than 59
  print("You have a D! Not looking good...") # If the previous check is true, then this is printed.
if(grd < 50): 
    # Checks if input is less than 50
  print("You have an F... Yikes!") # If the previous check is true, then this is printed.
