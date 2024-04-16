# here we take a value and check it is valid (within the range 1-10 integer)
# if invalid, return a sensible default

def checkInteger(v):
    '''the value of v must be an integer from 1-10'''
    valid = False
    if type(v) == int and v in range(1,11):
        valid = True
        return v
    else:
        return valid
