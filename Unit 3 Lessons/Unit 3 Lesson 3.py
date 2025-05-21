# Unit 3, Exercise 4: Simple 2D Arrays
#
# Place your code below!

# Predict
# A) prints the array in a grid and B) prints each array seperately with brackets.

"""
ar2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]
for i in range(len(ar2)):
  ar3 = ar2[i]
  for j in range(len(ar3)):
      print(ar3[j], end=" ")
  print() # PREDICT A

print(ar2) # PREDICT B
"""

# Modify

arr = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]
added = []
for i in range(len(ar2)):
  ar3 = ar2[i]
  amount = 0
  for j in range(len(ar3)):
    amount = amount + ar3[j]
  added.append(amount)
  
print(added)
