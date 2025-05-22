"""
Author : Anton Simashkevich
Student number: 923985
Course code: ICS3U
Revision date : May 21, 2025
Program : Wordle Database Search
Description : A program that accesses a Wordle solution file, and provide the user with the word on a specific date, or the date a word was played.

VARIABLE DICTIONARY :
  arr (list) = Stores lines read from the Wordle solution file
  dateNum (list) = Stores all dates in integer YYYYMMDD format
  words (list) = Stores all the words from the file
  month (list) = Contains month abbreviations used to convert month names to numbers
  f (file) = Used to open and read the wordle.dat file
  EndOfFile (bool) = Flags whether the end of the file has been reached
  line (str) = Temporarily stores a line read from the file before processing
  monthS (str) = Stores the month abbreviation extracted from a line of the file
  day (str) = Stores the day extracted from a line of the file
  year (str) = Stores the year extracted from a line of the file
  word (str) = Stores the Wordle solution word extracted from a line of the file
  monthNum (int) = Stores the numerical representation of a month
  date (int) = Stores a date converted into YYYYMMDD format
  choice (str) = Stores the user input for selecting either word or date search
  user_year (int) = Stores the year input by the user when searching by date
  user_month (int) = Stores the month input by the user when searching by date
  user_day (int) = Stores the day input by the user when searching by date
  user_date (int) = Stores the date input by the user when searching for a date
  user_word (str) = Stores the word entered by the user when searching for a word
"""

# List to hold lines from file
arr = []  
# List for storing numerical date values
dateNum = []  
# List for storing Wordle words
words = []  

# Month abbreviation list
month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", 
         "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

# Function to combine year, month, and day into an integer date
def merge(p, q, r):
    return p * 10000 + q * 100 + r

# Try to open and read the file
try:
    f = open("wordle.dat", "r")  # Open the file "wordle.dat" for reading
    EndOfFile = False  # Flag to check for end-of-file
    while not EndOfFile:  # Loop until the end of the file is reached
        line = f.readline().strip()  # Reads a line and remove leading/trailing spaces
        EndOfFile = (line == "")  # Check if the next line is empty
        if not EndOfFile:
            arr.append(line)  # Store the line in the array if it's not empty
    f.close()
except OSError:
    print("OSError")
except EOFError:
    print("EOFError")

# Process each line and populate words and dateNum lists
for i in range(len(arr)):
    [monthS, day, year, word] = arr[i].split()
    monthNum = month.index(monthS) + 1
    words.append(word)
    date = merge(int(year), int(monthNum), int(day))
    dateNum.append(date)

# Greet the user
print("Welcome to the Wordle Database!")

# Ask user for type of search
choice = input("Enter w if you are looking for a word, or d for a word on a certain date: ").upper()

if choice != "W" and choice != "D":
    print("Please enter one of the options")

# Search by date
if choice == "D":
    try:
        user_year = int(input("Enter the year: "))
        user_month_str = input("Enter the month (3-letter abbreviation, as in 'Jan' for 'January'): ")
        user_month = month.index(user_month_str.capitalize()) + 1
        user_day = int(input("Enter the day: "))
        user_date = merge(user_year, user_month, user_day)
        if 20210619 <= user_date <= 20240421:
            print("The word entered on", user_date, "was", words[dateNum.index(user_date)])
        elif user_date < 20210619:
            print(user_date, "is too early. No Wordles occurred before 20210619. Enter a later date.")
        else:
            print(user_date, "is too recent. Our records only go as late as 20240421. Please enter an earlier date.")
    except ValueError:
        print("Invalid input. Please enter numeric values for the year and day.")

# Search by word
if choice == "W":
    user_word = input("What word are you looking for? ").upper()
    try:
        print("The word", user_word, "was the solution to the puzzle on", dateNum[words.index(user_word)])
    except ValueError:
        print(user_word, "was not found in the database.")
