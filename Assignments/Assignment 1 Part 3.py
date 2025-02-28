"""
Variable Dictionary:

change: amount of money inputted
qamt: amount of quarters
remq: money remaining after dividing by 25
damt: amount of dimes
remd: money remaining after dividing remq by 10
namt: amount of nickels
remn: money remaining after dividing remd by 5
pamt: amount of pennies, equal to remn
"""

change = int(input("Please input the amount of money in cents: ")) # Asks the user for an amount of money and converts to int data type

print("Checking for value above one dollar...") # Informs the user that dollar amount is being removed if they inputted above a dollar

if change >= 100: # Preforms a check for value above 100
    change = change % 100  # Removes dollar value if present

# Assigns variables to the coin amounts and remainders

qamt = change // 25 # Quarter amount
remq = change % 25 # Quarter remainder

damt = remq // 10 # Dime amount
remd = remq % 10 # Dime remainder

namt = remd // 5 # Nickel amount
remn = remd % 5 # Nickel remainder

pamt = remn  # Directly the number of pennies left

# The following code prints the results, not including coins that are equal to zero in the final result

if qamt == 0:
  print("You have one dollar.") # If 100 is entered, returns with this message instead of zero quarters
else:
  print(change, "cents can be:") 
if qamt > 0:
  print(qamt, "quarters")
if damt > 0:
  print(damt, "dimes")
if namt > 0:
  print(namt, "nickels")
if pamt > 0:
  print(pamt, "pennies") 
