# Prediction A
"""
Predict A:
3 4 1 2 6 
9 2 3 7 5 
4 2 1 0 3 

Predict B:
[[3, 4, 1, 2, 6], [9, 2, 3, 7, 5], [4, 2, 1, 0, 3]]
"""

# Modify

arr2 = [[3, 4, 1, 2, 6],
      [9, 2, 3, 7, 5],
      [4, 2, 1, 0, 3]]
added_arr = []
for i in range(len(arr2)):
  arr3 = arr2[i]
  amount = 0
  for j in range(len(arr3)):
    amount = amount + arr3[j]
  added_arr.append(amount)
print(added_arr)
