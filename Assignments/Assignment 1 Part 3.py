import math
change = int(input("Please input the amount of money in cents: "))

print("Removing dollar value...")

change = change % 100 # removes dollar value

# variables must be defined outside "else" statements or an error will occur

qamt = change // 25
remq = change % 25

damt = remq // 10 
remd = remq % 10

namt = remd // 5
remn = remd % 5

pamt = remn // 1

# rem for pennies is not needed

if remq == 0:
    print(change, "cents can be", qamt, "quarters.")
if namt == 0:
  print(change, "cents can be", qamt, "quarters,", namt, "nickels, and", pamt, "pennies.")
elif remd == 0:
    print(change, "cents can be", qamt, "quarters, and", damt, "dimes.")
if namt == 0:
  print(change, "cents can be", qamt, "quarters,", damt, "dimes, and", pamt, "pennies.")
elif remn == 0:
    print(change, "cents can be", qamt, "quarters,", damt, "dimes, and", namt, "nickels.")
