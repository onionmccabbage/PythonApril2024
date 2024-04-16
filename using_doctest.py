import doctest

def cubeIt(x):
    '''return the cube of the value
    >>> cubeIt(3)
    27
    >>> cubeIt(-3)
    -27
    >>> cubeIt(20)
    8000
    '''
    return x**3


if __name__ == '__main__':
    # print( cubeIt(3) ) # 27
    # print( cubeIt(-3) ) # -27
    doctest.testmod(verbose=True)