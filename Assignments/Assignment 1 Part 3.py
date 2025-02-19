change = int(input("Please input the amount of money in cents: "))

print("Removing dollar value...")

if change >= 100:
    change = change % 100  # Removes dollar value if present

qamt = change // 25
remq = change % 25

damt = remq // 10
remd = remq % 10

namt = remd // 5
remn = remd % 5

pamt = remn  # Directly the number of pennies left

# Print the result based on nonzero coin values
if qamt >= 0:
  print(change, "cents can be", qamt, "quarters")
if damt > 0:
  print(damt, "dimes")
if namt > 0:
  print(namt, "nickels")
if pamt > 0:
  print("and", pamt, "pennies")
