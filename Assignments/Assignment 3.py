"""
Author           : Anton Simashkevich
Revision date    : April 8th 2025
Program          : Palindrome Checker
Description      : A program that checks whether words in a list are palindromes or not by comparing their letters.

VARIABLE DICTIONARY :
  list           (List of Strings)   = A list containing the words to be checked for palindrome status.
  word           (String)            = The current word being checked from the list.
  wlen           (int)               = The index of the last character in the current word (length of the word - 1).
  is_palindrome  (Boolean)           = A flag that determines whether the current word is a palindrome.
  d              (int)               = The index used to compare characters from the front and back of the word.
"""

list = ["civic", "level", "kayak", "madam", "tacocat", "racecar", "student", "rotor", "problem", "brick"] # Define a list of 10 words, some palindromes and some not

print("Palindrome program!") # Print the starting message

for c in range(len(list)): # Loop through each word in the list using its index
    word = list[c] # Get the current word from the list
    wlen = len(word) - 1 # Store the index of the last character in the word
    is_palindrome = True # Assume the word is a palindrome to start
    d = 0 # Start comparing from the first character

    while d < len(word) // 2:  # Loop while d is less than half the length of the word (only need to check halfway)
        if word[d] != word[wlen - d]: # If the character from the front doesn't match the corresponding back character
            is_palindrome = False # It's not a palindrome
            d = len(word) # Force the loop to exit by pushing d past the limit
        else:
            d += 1 # Move to the next character toward the center
            
    if is_palindrome:
        print("%s is a palindrome" % word) # If no mismatches were found
    else:
        print("%s is not a palindrome" % word) # If a mismatch was found
