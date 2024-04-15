#receiving user input - ALWAYS a string-type
# the code execution stops to wait for the user input
# we might loop until a valid entry is available
while True: # loop endlessly - use with care!!!
    u = input('Please enter a value ') # this waits for a human to type something at the console
    if u == 'quit': # == compares values
        break # breaks out of the current loop
    elif u.isnumeric(): # check if the value contains ONLY numeric values
        # if we need an int, the safest thing is to first cast as a float
        r = int(float(u)) # we should now have an integer
        # we need to know if a number is odd or even
        if r%2 == 0: # it must be an even number (no remainder!!)
            print('the numeric value is even', r)
        else:
            print('it is an odd number')
    elif isinstance(u, str): # elif means 'else if' and requires a condition
        print('of course it is a string!!')
    else:
        print(u, type(u))

# validation
# conditional code


# iterating over collections


# print formatting

