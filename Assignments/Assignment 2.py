"""
Author : Anton Simashkevich
   Revison date : 18 March 2025
   Program : A Number Guessing Game Assignment
   Description : A number guessing game with a range of numbers from 1 to 100.
   VARIABLE DICTIONARY :
     num (int) = random number chosen by the program
     guessnum (String) = amount of guesses given to the user
     correct (Boolean) = a check if the users guess is correct or not.
     guess (int) = a guess inputted by the user
"""

import random # allows for random number generation
num = random.randrange(1, 100, 1) # the range in which numbers can be generated, 1 to 100 in this case
guessnum = 6 # sets the number of guesses to 6
print("I am thinking of a number between 1 and 100. You have 6 guesses, and I will tell you if you should guess higher or lower based on your input! Guess correctly in 6 or less tries and you win.") # tells the user about the program
correct = False # sets correct to false so the program doesn't immediately end
while not correct: # loops while a correct answer has not been inputted
  guess = int(input("What is your guess? You have %d guesses. " % guessnum)) # asks the user for a guess
  correct = (guess == num) # makes it so correct becomes true if the guess is equal to the generated number
  if correct: # checks if guess is equal to the generated number
    print("You got it! Nice job.") # informs the user that they guessed correctly and stops further guessing
  if(guess != num): # checks if the guess is not equal to the generated number
    guessnum -= 1 # subtracts 1 guess from the total amount of guesses and assigns the new value to guessnum
  if(guess > num): # checks if the guess is greater than the generated number
    print("Try guessing lower. You have %d guesses left" % guessnum) # if previous check is true, tells the user to guess a lower number and lets them know how many guesses remain
  if(guess < num): # checks if the guess is less than the generated number
    print("Try guessing higher. You have %d guesses left" % guessnum) # if previous check is true, tells the user to guess a higher number and lets them know how many guesses remain
  if(guessnum == 1 and guess > num): # included so the print statement wouldn't say "you have one guesses remaining", instead if "you have one guess remaining", for proper grammar
    print("Try guessing lower. You have %d guess left." % guessnum) # informs the user to guess lower in the case of the number of guesses being equal to 1
  if(guessnum == 1 and guess < num): # same function as line 29
    print("Try guessing higher. You have %d guess left." % guessnum) # informs the user to guess higher in the case of the number of guesses being equal to 1
  if(guessnum == 0): # checks if the number of guesses is equal to 0
    correct = True # sets correct to true so loop is closed
    print("Sorry! You ran out of guesses. The number was %d" % num) # informs the user they lost and tells them what the number was
