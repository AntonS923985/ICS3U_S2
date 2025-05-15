# Modify 1

print("--8<--" * 10)

# Try This

S = "#"
low = 1
step = -1
for i in range(11, low - 1, step):
    print(S * i)

# Modify 2

spaces = 4
for i in range (1, 10, 2):
  print(" " * spaces, "#" * i)
  spaces -= 1

# Modify 3

spaces = 5
for i in range (1, 13, 2):
  print(" " * spaces, "#" * i)
  spaces -= 1
  
spaces = 1
for i in range (9, 0, -2):
  print(" " * spaces, "#" * i)
  spaces += 1
