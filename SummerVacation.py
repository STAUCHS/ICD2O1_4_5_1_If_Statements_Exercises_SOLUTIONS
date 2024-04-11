#-------------------------------------------------------------------------
# Name:		    Summer Vacation
# Purpose:	  Determine if user is allowed to go on a summer vacation
# Author:		  Chen. C
# Created:		11/04/2024
#-------------------------------------------------------------------------

# Get info from user
average = float(input("Enter your average (%): "))
income = float(input("Enter your total income: "))

# Decide if user can go on summer vacation
if average >= 80 and income >= 500:
  print("Congratulations! You can go to Europe in the summer.")
elif average >= 80:
  print("Well done! You can go to California in the summer.")
else:
  print("Sorry, you cannot go on vacation this summer.")