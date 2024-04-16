def readText():
    '''Open a text file then read back the contents'''
    try:
        # we need a file access object
        with open('my_log.txt', 'rt') as fin: # this is more efficient, since it will auto close when done
            r = fin.read() # read the entire file as one string of text
            # r = fin.readline() # read the next line
            # r = fin.readlines() # read all the lines into a list of strings
            # when the 'with' ends, it will close 'fin'
        return r
    except FileExistsError as fe:
        print(f'The file already exists: {fe}')
    except FileNotFoundError as fnf:
        print(f'That file cannot be located: {fnf}')
    except Exception as err:
        print(err)

if __name__ == '__main__':
    r = readText()
    print(r)