# this module may contain a useful utility

# NB all functions are object in Python
def isOdd(n): # this is how we define a function
    '''we may write documentation
    strings at the top 
    of a code block'''
    answer = bool(n%2 != 0) # != means not equal
    return answer
# remember - the code block ends when we stop indenting!

if __name__ == '__main__': # then we must be running this module directly
    # we can exercise our code
    print(isOdd, type(isOdd))
    print(isOdd(3)) # True
    print(isOdd(2)) # False
    print(isOdd(-99)) # True
    # When we run a module directly, python ALWAYS sets __name__ to __main__
    # When we run code via an import, python sets __name__ to the module name
    print(f'Inside my_util: {__name__}') # 
