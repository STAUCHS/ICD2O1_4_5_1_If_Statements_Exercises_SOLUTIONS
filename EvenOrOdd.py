#-------------------------------------------------------------------------
# Name:		    Even or Odd 
# Purpose:	  Determine if a number is even or odd
# Author:		  Chen. C
# Created:		11/04/2024
#-------------------------------------------------------------------------

# Output title
print("** Even or Odd? **")

# Get number from user
num = int(input("Enter a number: "))

# Check if it is even or odd or zero
if num == 0:
  print("\n0 is neither even nor odd.")
elif num % 2 == 0:
  print(f"\nYour number {num} is even.")
else:
  print(f"\nYour number {num} is odd.")