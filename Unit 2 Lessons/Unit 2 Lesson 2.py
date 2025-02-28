"""
I predict the code will run a loop that prints the value of "count",
and each time it prints it will subtract 1 from the total value until
it reaches 0, which will trigger the != in the second line and it will
not run anymore.
"""

count = 9
while (count != 0):
    print(count)
    count -= 1
