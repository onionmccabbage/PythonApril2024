
def someMaths(n):
    return n*n # any mathematics can happen here

# Here we define our own custom generator
def makeGen():
    '''generate the squares of integers between two values'''
    return (someMaths(num) for num in range(-100, 101)) # we could include an if clause

if __name__ == '__main__':
    g = makeGen()
    print(type(g), g)

    # a generator will yield each value in the sequence when asked
    print( g.__next__() ) # 10,000
    print( g.__next__() ) # 9801
    print( g.__next__() ) # 9604

    # we might choose to iterate over our generator
    for _ in g: # typical python convention
        print( _, end=', ')

    # the generator is now exhausted (there are no values left to yield)
    # print( g.__next__() ) # nope

    # we need another instance of our generator
    g2 = makeGen()
