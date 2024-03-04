"""
You're provided with a number labeled num. Using if/else, display the message:

"The number num is odd" if num is odd.
"The number num is even" if num is even.
In the print() functions, fill in the ___ with the appropriate descriptor ('odd' or 'even'). Tip: 
A number is considered even if, when divided by 2, the remainder (using the % operator) is 0.

Note

In Python, the % operator is used as the modulo operator, 
which returns the remainder after dividing one number by another. 
For example, 5 % 2 would return 1, since 2 goes into 5 twice with a remainder of 1.
"""


num = 8941 % 931

# Define if/else construction
if num % 2 == 0:
  # Print message below
  print("The number num is", "even")
else:
  # Print another message below
  print("The number num is", "odd")