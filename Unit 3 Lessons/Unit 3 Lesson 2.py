# Unit 3, Exercise 3: Arrays of Different Types
#
# Place your code below!

# I predict it will find the length of each word and state the 
# output as an integer and then print the word next to it

"""
items = ["Apples", "Bananas", "Cherries", "Dosa"]
sizes = []
for i in range(len(items)): # Predict A: State the purpose,
                            # data types, and any output
    sizeI = len(items[i])
    sizes.append(sizeI)

for i in range(len(sizes)): # Predict B: State the output
    print("%d %s" % (sizes[i], items[i]))
"""

# Modify

items = int(input("How many items are you entering? "))
itemlist = []
print("Enter your items now, one by one:")
i = 0
while i < items:
  next_item = input("Next item:")
  i += 1
  itemlist.append(next_item)
print("You have entered %d items." % i)

for x in itemlist:
  print(x)
    
