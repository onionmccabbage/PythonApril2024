# very often we have a main module
# we may choose to import only PARTS Of another module
from my_util import isOdd
# this can also work for biult-in libraries
from datetime import datetime

# avoid the following:
# from . import * # this will import (almost) EVERYTHING from the current package

def main(m): # by convention we call our main funtion 'main'
    return isOdd(m)


if __name__ == '__main__':
    print(f'Today is {datetime.now()}')
    r = main(3) # invoke the function called 'main'
    print(r)