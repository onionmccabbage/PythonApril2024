# we can choose to pass arguments in at the point where we run our module
import sys

def showSysArgs():
    '''Any system arguments will exist in a list of strings
    The zeroeth member of the argv list is ALWAYS the module name'''
    return sys.argv

if __name__ == '__main__':
    args = showSysArgs()
    for _ in args:
        print(f'Member {_} of the system arguments ')