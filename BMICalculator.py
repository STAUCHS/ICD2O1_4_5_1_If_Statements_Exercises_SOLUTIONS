#-------------------------------------------------------------------------
# Name:		    BMI Calculator
# Purpose:	  To calculate the BMI for the user and to tell them if they are above, below, or in the healthy range
# Author:		  Chen. C
# Created:		11/04/2024
#-------------------------------------------------------------------------

# Get the height and weight from user
height_m = float(input("Height (in m): "))
weight_kg = float(input("Weight (in kg): "))

# Calculate BMI
BMI = weight_kg / (height_m ** 2)

# Decide if they are above, below, or within the healthy range
if BMI < 19:
  print("\nYou are below the healthy range.")
elif BMI <= 25: 
  print("\nYou are within the healthy range.")
else:
  print("\nYou are above the healthy range.")