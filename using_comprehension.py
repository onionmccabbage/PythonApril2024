# in Python 'comprehension' means to comprehensively deal with every member of a collection

def listComp(start, stop):
    '''comprehensively deal with all the members of a list'''
    r = range(start, stop) # stop is stop-before
    # here we have list cmprehension
    l = [ num**2 for num in r ] # we have comprehensively dealt with all the members of the range
    return l

def tupleComp(start, stop):
    r = range(start, stop)
    # this is called tuple comprehension
    t = tuple(num**0.5 for num in r)
    return t

# we can also deal with every member of a dict - this is dictionary comprehension
def dicComp(s): # we will pass in a string
    '''In this case, we count the frequency of each letter within the string 's' '''
    characters_d = { letter:s.count(letter) for letter in s }
    return characters_d

if __name__ == '__main__':
    print(  listComp(0, 99)  )
    print(  tupleComp(0, 99)  )
    print(  dicComp('is it time for our morning coffee break yet?') )
