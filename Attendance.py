#-------------------------------------------------------------------------
# Name:		    Attendance
# Purpose:	  Let the user know how long they will need to wait during roll call
# Author:		  Chen. C
# Created:		11/04/2024
#-------------------------------------------------------------------------

# Get last name from user
last_name = input("Enter your last name: ")

# Check when they will be called
if last_name <= "carswell":
  print(f"You don't have to wait long, {last_name}")
elif last_name <= "jones":
  print(f"That's not bad, {last_name}")
elif last_name <= "smith":
  print(f"Looks like a bit of a wait, {last_name}")
elif last_name <= "young":
  print(f"It's gonna be a while, {last_name}")
elif last_name > "young":
  print(f"Not going anywhere for a while, {last_name}")