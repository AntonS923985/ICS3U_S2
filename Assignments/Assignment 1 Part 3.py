change = int(input("Please input the amount of money in cents: ")) # Asks the user for an amount of money and converts to int data type

print("Checking for value above one dollar...") # Informs the user that dollar amount is being removed if they inputted above a dollar

if change >= 100:
    change = change % 100  # Removes dollar value if present

qamt = change // 25
remq = change % 25

damt = remq // 10
remd = remq % 10

namt = remd // 5
remn = remd % 5

pamt = remn  # Directly the number of pennies left

# Prints the results, not including coins that are not included in the final result
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
