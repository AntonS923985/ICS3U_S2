"""
Author: Anton Simashkevich
Student Number: 923985
Revision date: 15 Jun, 2025
Program: Credit Card Report
Description: Report of credit cards in a customer database that have expired or about to expire
             Outputs the name, credit card type, number, and expiry status of cards with expiry date on or before June 2024.

VARIABLE DICTIONARY :
  filename: str - name of file to read
  fh: file object - file handle for input file
  names: list - list of full names (first and last)
  cc_nums: list - list of credit card numbers
  cc_types: list - list of credit card types
  expiry_dates: list - list of expiry dates in yyymm integer format
  lines: list - list of all lines in the file (excluding header)
  output_filename: str - name of output file
  output file: file object - file handle for output file
  expired_text: str - text that says either EXPIRED or RENEW IMMEDIATELY
  formatted_date: str - MM/YYYY format of the expiry date
"""

# Merge sort algorithm to sort expiry dates & match other arrays accordingly
def mergesort(arr, arr2, arr3, arr4, 1, r):
    if 1 < r:
      m = 1 + (r-1) // 2 #midpoint
      mergesort(arr, arr2, arr3, arr4, 1, m) # Sort left half
      mergesort(arr, arr2, arr3, arr4, m + 1, r) # Sort right half
      merge(arr, arr2, arr3, arr4, 1, m, r) # Merge both halves

# Merge function that merges primary array alongside other ones
def merge(arr, arr2, arr3, arr4, 1, m, r):
  n1 = m - 1 + 1
  n2 = r - m

  # Temporary arrays for both halves
  L = [0] * n1
  L2 = [0] * n1
  L3 = [0] * n1
  L4 = [0] * n1
  R = [0] * n2
  R2 = [0] * n2
  R3 = [0] * n2
  R4 = [0] * n2

  # Copy data to left arrays
  for i in range(n1):
    L[i] = arr[l + i]
    L2[i] = arr2[l + i]
    L3[i] = arr3[l + i]
    L4[i] = arr4[l + i]

  # Copy data to right arrays
  for j in range(n2):
    R[j] = arr[m + 1 + j]
    R2[j] = arr2[m + 1 + j]
    R3[j] = arr3[m + 1 + j]
    R4[j] = arr4[m + 1 + j]
    
 # Merge sorted arrays
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            arr2[k] = L2[i]
            arr3[k] = L3[i]
            arr4[k] = L4[i]
            i += 1
        else:
            arr[k] = R[j]
            arr2[k] = R2[j]
            arr3[k] = R3[j]
            arr4[k] = R4[j]
            j += 1
        k += 1

    # Copy any remaining elements from the left
    while i < n1:
        arr[k] = L[i]
        arr2[k] = L2[i]
        arr3[k] = L3[i]
        arr4[k] = L4[i]
        i += 1
        k += 1

    # Copy any remaining elements from the right
    while j < n2:
        arr[k] = R[j]
        arr2[k] = R2[j]
        arr3[k] = R3[j]
        arr4[k] = R4[j]
        j += 1
        k += 1

# Initialize file name and empty lists for data
filename = "data.dat"
names = []
cc_nums = []
cc_types = []
expiry_dates = []

# Try and open and read the file
try:
  fh = open(filename, 'r')
  lines = fh.readlines()
  fh.close()
except FileNotFoundError
  exit()

# Remove the header
if lines:
  lines.pop(0)

# Process each line
for line in lines
  try:
      # Parse CSV line into fields
      given_name, surname, cc_type, cc_number, exp_mo, exp_yr = line.strip().split(',')
      
      # Combine names
      name = given_name + ' ' + surname

      # Format month as two digits
      if len(exp_mo) == 1:
          exp_mo = '0' + exp_mo

      # Combine year and month into one integer for sorting/comparison
      expiry_date = int(exp_yr + exp_mo)

      # Add parsed values to respective lists
      names.append(name)
      cc_types.append(cc_type)
      cc_nums.append(cc_number)
      expiry_dates.append(expiry_date)
  except ValueError:
      print("Warning: Skipped malformed line:", line.strip())

# Sort all lists based on expiry date using merge sort
mergeSort(expiry_dates, names, cc_nums, cc_types, 0, len(expiry_dates) - 1)

# Output file setup
output_file_name = "output.txt"
try:
    output_file = open(output_file_name, "w")
except:
    print("Error: Could not open output file.")
    exit()


# Loop through sorted expiry dates
for i in range(len(expiry_dates)):
    # Skip cards that are not expired or expiring yet (after June 2024)
    if expiry_dates[i] > 202406:
        break

  # Format expiry date as MM/YYYY
    year = expiry_dates[i] // 100
    month = expiry_dates[i] % 100
    formatted_date = f"{month:02}/{year}"

    # Determine status message
    if expiry_dates[i] < 202406:
        expired_text = "EXPIRED"
    else:
        expired_text = "RENEW IMMEDIATELY"

# Format and print each line to console and file
    line = "%-35s %-15s %-20s %-10s %-15s" % (
        names[i] + ':', cc_types[i], '#' + cc_nums[i], formatted_date, expired_text
    )

    print(line)
    output_file.write(line + "\n")

# Close output file
output_file.close()
print("\nOutput sent to", output_file_name)
