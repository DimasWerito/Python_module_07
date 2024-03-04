"""
Update the code from the earlier challenge about your small grocery store. 
Now, if the store's revenue is exactly $2000, the program should print 
"We are breaking even!" instead of "Everything is ok!". 
Incorporate this new response using an elif statement.
"""


revenue = 2000

# Modify your conditional statement
if revenue < 2000:
  print("We suffer losses!")
# Add comparison of revenue with 2000
elif revenue == 2000:
  # Output 'We are breaking even!'
  print('We are breaking even!')