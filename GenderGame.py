#-------------------------------------------------------------------------
# Name:		    Courtesy Titles
# Purpose:	  Determine what title should be used for the user (Ms., Mrs., Mr. or none)
# Author:		  Chen. C
# Created:		11/04/2024
#-------------------------------------------------------------------------

# Get info from user
gender = input("What is your gender (M, F or None): ")
first_name = input("First name: ")
last_name = input("Last name: ")

# CASE 1: Gender = M or F
if gender != "None":
  age = int(input("Age: "))

  # CASE 1A: Age < 20
  if age < 20:
    print(f"Then I shall call you {first_name} {last_name}")

  # CASE 1B: Gender = Female
  elif gender == "F" and age >= 20:
    married = input(f"Are you married, {first_name} (y/n)? " )
    if married == "y":
      print(f"Then I shall call you Mrs. {last_name}.")
    else:
      print(f"Then I shall call you Ms. {last_name}")

  # CASE 1C: Gender = Male
  else:
    print(f"Then I shall call you Mr. {last_name}")

# CASE 2: Gender = None
else:
  print(f"Then I shall call you {first_name} {last_name}")



