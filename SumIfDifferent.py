#-------------------------------------------------------------------------
# Name:		    Sum If Different
# Purpose:	  Sums the values of integers that are unique from 3 ints inputted by the user.
# Author:		  Chen. C
# Created:		11/04/2024
#-------------------------------------------------------------------------

# Get numbers from user:
num_one = int(input("Enter the value of a: "))
num_two = int(input("Enter the value of b: "))
num_three = int(input("Enter the value of c: "))

sum = 0

# Sum the unique values
# All numbers are different
if (num_one != num_two) and \
   (num_two != num_three) and \
   (num_one != num_three):
  sum = num_one + num_two + num_three

# a and b are the same - sum = a + c 
elif (num_one == num_two) and \
     (num_one != num_three) and \
     (num_two != num_three):
  sum = num_one + num_three

# a and c are the same - sum = a + b
elif (num_one == num_three) and \
     (num_one != num_two) and \
     (num_two != num_three):
  sum = num_one + num_two

# b and c are the same - sum = a + b
elif (num_one != num_two) and \
     (num_one != num_three) and \
     (num_two == num_three):
  sum = num_one + num_two

# All numbers are the same
else:
  sum = num_one

print(f"The sum is {sum}.")
