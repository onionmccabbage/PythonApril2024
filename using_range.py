# range will generate a sequence of values we may need
# NB these values NEVER exist in memory all at once

def basicRange():
    l = [2, 4, 6, 8, 10] # all these values exist in memory at once
    #       (start, stop-before, step)
    r = range(2, 1000, 2)  # only the range object exists in memory (NOT the values)
    print(type(r))
    # a range object will yield the next values in the sequence when we need them
    for i in r:
        print(i, end=(', ')) # 2, 4, 6, 8, 10,

    # we may also use a range to check existance, e.g. for validation
    t = range(-6, 42) # default step is 1
    curent_temperature = -13
    print(curent_temperature in t) # False

# we can also make generators
def makeTuple():
    '''use a range to populate a tuple'''
    r = range(-99, 100, 2) # start, stop-before, step
    r_t = tuple(r) # at this point all the values from the range will exist in memory (inside this tuple)
    return r_t
def makeList():
    '''use a range to populate a list'''
    return list(range(-5, 6)) # same thing only shorter

# we may need a more complex sequence of values
def oddList():
    '''return a list of odd numbers'''
    odd_l = [ num for num in range(-99, 100) if num%2 == 1 ] # or list()
    return odd_l
def myValues():
    '''return a tuple of values'''
    g = ( num/4 for num in range(-25, 26) ) # this is a generator object
    print(type(g)) # the values of generator do NOT all exist in memory - they are yielded on demand
    return tuple(g) # populate a tuple from the members of the generator


if __name__ == '__main__':
    basicRange() # call our function within this module
    print( makeTuple() )
    print( makeList() )
    q = myValues()
    print(q)
