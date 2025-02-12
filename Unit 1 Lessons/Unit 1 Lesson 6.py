dob = int(input("Please input your year of birth:"))
age = int(input("Please input your age:"))
result = dob * 2 + 5
result = result * 50 + age
result = (result - 250) / 100
print("Your birth year with your age added as a decimal is:" , result)
