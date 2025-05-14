# Part A

num = int(input("Please enter a number:"))
count = num
fact = 1
while count >0:
    fact *= count
    count -= 1
print("%d is equal to %d" % (num, fact))

# Part B

n = int(input("Please enter a number: "))
count = n

print(n, "factorial is equal to ", end="")

while count > 0:
  if count == 1:
    print("1")
    quit()
  print(count, "x", end=" ")
  count -= 1

# Part C

n = int(input("Please enter a number: "))
count = n
fac = 1

while count > 0:
  
    fac *= count
    count -= 1
    
print(n, "factorial is equal to", fac)
