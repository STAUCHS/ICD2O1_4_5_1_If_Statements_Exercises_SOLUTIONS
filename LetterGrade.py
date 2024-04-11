#-------------------------------------------------------------------------
# Name:		    Letter Grade
# Purpose:	  Determine the letter grade based off a mark
# Author:		  Chen. C
# Created:		11/04/2024
#-------------------------------------------------------------------------

# Get mark from user
mark = float(input("Enter your mark: "))

# Check which letter grade the mark is equal to
if mark >= 80 and mark <= 100:
  print("Your letter grade is A.")
elif mark >= 70 and mark < 80:
  print("Your letter grade is B.")
elif mark >= 60 and mark < 70:
  print("Your letter grade is C.")
elif mark >= 50 and mark < 60:
  print("Your letter grade is D.")
elif mark >= 0 and mark < 50:
  print("Your letter grade is F.")
else:
  print("Invalid input. Mark must be between 0 and 100.")