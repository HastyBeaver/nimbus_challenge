#  Create and call a python function that : 
#  stores a random integer A between 1 and 9
#  stores a random integer B between 1 and 9
#  multiplies A and B together as C
#  Prints A and C for every result until C = 4
#  If C = 4 , print ‘Success!’ and the results for A and B
#  Store your code on a GitHub account and share it with the email-address given in the SQL test, including your CV

import random # I am importing python built-in module called `random`.
 
while True: # keep iterating until I choose to stop
    a = random.randint(1, 9) # initialise a, b, two random integers between 1 and 9.
    b = random.randint(1, 9)
    c = a * b # multiply them
    if c != 4: # if their result is different than 4, print a and c.
        print(a, c)
    elif c == 4: # if their result == 4, print(...)
        print(f"Success! number {a} and {b} gave this result: {c}.")
        break # <- use this to stop the loop, otherwise it will keep iterating!