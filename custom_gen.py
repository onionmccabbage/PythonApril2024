from random import randint

def genSquares(n=1, stop=10):
    '''This generator will yield sequential square nubmers'''
    number  = n
    while number < stop: # we often use 'while' to make a run-loop
        # most function will 'return' something
        # a generator will 'yield' stuff repeatedly
        yield number**2 # yield the square of the next number
        number += 1
        # break # this will break out of our while loop

def genRandomInt():
    '''generate random integers'''
    while True:
        yield randint(0,10)

if __name__ == '__main__':
    # we need an instance of our generator
    my_g = genSquares(n=1, stop=10)
    print(type(my_g)) # <generator>
    print( my_g.__next__() ) 
    print( my_g.__next__() ) 
    print( my_g.__next__() ) 
    # we might choose to iterate over the members of the generator
    for _ in my_g:
        print(f'The next square nubmer is {_}')
    my_rand = genRandomInt()
    print( my_rand.__next__() )
    print( my_rand.__next__() )
    print( my_rand.__next__() )
    print( my_rand.__next__() )
    print( my_rand.__next__() )
    print( my_rand.__next__() )