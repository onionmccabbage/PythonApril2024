# if we choose we can use an asterisk to gather together members of the argmetns collection
def usePositional(*args):
    '''every function may have positional arguments
    These always exist in a tuple'''
    print(args[0], args[1], type(args))

def useKeyword(**kwargs):
    '''every function may have keyword arguments
    These always exist in a dictionary'''
    print(kwargs)

def useBoth(*args, **kwargs):
    '''any positional arguments will exist in a tuple
    any keyword arguments will exist in a dictionary'''
    print(f'The positional arguments are {args}')
    for (k, v) in kwargs.items():
        print(f'The keyword {k} has the value {v}')

# There is no overloading in Python (only ONE of every function)
# BUT we can behave differently depending on the number of arguments
def doMaths(*args):
    '''if there is one argument, return it as an integer
    if there are two arguments, add them
    if there are three, multiple them all'''
    if len(args) == 1:
        return int(args[0])
    if len(args) == 2:
        return args[0] + args[1]
    if len(args) == 3:
        return args[0]*args[1]*args[2]
    
# we may choose to use defaults
def useD(x=3, y=4):
    return (x**2+y**2)**0.5
    
if __name__ == '__main__':
    usePositional(True, 33, 'hi', [4,3,2])
    useKeyword(x=3, y=4, n='Helen', a={5,3,8,0})
    # NB any keyword arguments must come AFTER any positional arguments
    useBoth(True, 33, 'hi', [4,3,2], x=3, y=4, n='Helen', a={5,3,8,0})
    print(doMaths(3.99)) # 4
    print(doMaths(4,6))  # 10
    print(doMaths(2,3,4)) # 24
    print(useD()) #x and y will be default
    print(useD(x=-3, y=-4)) # replace teh defaults with our own
    print(useD(y=5, x=2))
    print(useD(y=99)) # x willbe default
