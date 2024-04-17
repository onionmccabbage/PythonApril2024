# every module will have it's own global scope - not within ANY code block

g = 'this is in the global scope'

def fn():
    '''while it is possible to access global variables, we try to avoid this'''
    global g # now any refernec to g will mutate the global value
    g='this is in the local scope of this function'
    return g

if __name__ == '__main__':
    print(g)
    print(fn())
    print(g)