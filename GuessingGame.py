#-------------------------------------------------------------------------
# Name:		    Guess Two Numbers
# Purpose:	  Program generates two randum numbers between 1 and 10. User guess both numbers.
# Author:		  Chen. C
# Created:		11/04/2024
#-------------------------------------------------------------------------

import random 

# Output title and description
print("** Guess the Numbers! **")
print("I will generate 2 random numbers between 1 and 10 for you to guess. "
       "Try to guess both of them!\n")

# Generate two random numbers between 1 and 10
random_num_one = random.randrange(1, 10)
random_num_two = random.randrange(1, 10)

# Get guesses from user
guess_one = int(input("Guess one: "))
guess_two = int(input("Guess two: "))

# Check if their guesses are correct
if (guess_one == random_num_one and guess_two == random_num_two) or \
   (guess_one == random_num_two and guess_two == random_num_one):
  print("Congratulations! You guessed both numbers!")
elif (guess_one == random_num_one or guess_two == random_num_two) or \
     (guess_one == random_num_two or guess_two == random_num_one):
  print("Not bad! You guessed one of the numbers.")
else:
  print("Sorry, you did not guess correctly.")