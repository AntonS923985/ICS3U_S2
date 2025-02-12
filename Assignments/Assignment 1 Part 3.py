change = int(input("Please input the amount of money in cents:"))
qamt = int(change / 25)
remq = change % 25
if(remq == 0):
  print(change, "cents can be", qamt, "quarters")
else:
  damt = int(remq / 10)
  remd = remq % 10
if(remd ==0):
  print(change, "cents can be", qamt, "quarters", damt, "dimes")
else:
  namt = int(remd / 5)
  remn = remd % 5
if(remd ==0):
  print(change, "cents can be", qamt, "quarters", damt, "dimes", namt, "nickels")
else:
  pamt = int(remn / 1)
  remp = remn % 1
if(remp ==0):
  print(change, "cents can be", qamt, "quarters", damt, "dimes", namt, "nickels", pamt, "pennies.")
