#-------------------------------------------------------------------------
# Name:		    Two Questions
# Purpose:	  Computer guesses an answer based on two questions (like 20 questions game but with 2 questions)
# Author:		  Chen. C
# Created:		11/04/2024
#-------------------------------------------------------------------------

# Output title
print("TWO QUESTION!")
print("Think of an object, and I'll try to guess it.\n")

# Ask the questions
question_one = input("Question 1) Is it a(n) animal, vegetable, or mineral? ")
question_two = input("Question 2) Is it bigger than a breadbox (y/n)? ")

# Decide on answer
if question_one == "animal":
  if question_two == "y":
    print("\nMy guess is that you are thinking of a moose.")
  else:
    print("\nMy guess is that you are thinking of a squirrel.")

elif question_one == "vegetable":
  if question_two == "y":
    print("\nMy guess is that you are thinking of a cabbage.")
  else:
    print("\nMy guess is that you are thinking of a tomato.")

else:
  if question_two == "y":
    print("\nMy guess is that you are thinking of a car.")
  else:
    print("\nMy guess is that you are thinking of a paper clip.")
  
    