# this module may contain a useful utility

# NB all functions are object in Python
def isOdd(n): # this is how we define a function
    answer = bool(n%2 != 0) # != means not equal
    return answer
# remember - the code block ends when we stop indenting!

# we can exercise our code
print(isOdd, type(isOdd))
print(isOdd(3)) # True
print(isOdd(2)) # False
print(isOdd(-99)) # True