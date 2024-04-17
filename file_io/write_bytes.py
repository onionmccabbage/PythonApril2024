def writeBytes(my_bytes):
    'Sometimes it is useful to write to file in chunks'
    try:
        # 'a' will append 'w' will (over)write 'x' for exclusive access
        fout = open('my_log', 'ab') # 'b' will write bytes
        fout.write( my_bytes ) # write a slice of the text string
        fout.close()
    except FileExistsError as err:
        print(f'Cannot get exclusive access: {err}')
    except Exception as err:
        print(err)

def readBytes():
    '''read any bytes back from a file'''
    try:
        with open('my_log', 'rb') as fin: # 'with' will close when done
            b = fin.read() # read the entire file
        return b
    except Exception as err:
        print(err)


if __name__ == '__main__':
    values = range(0,256) # these are NOT string values
    w = bytes(values)
    writeBytes(w) # pass the bytes into our writer
    # use our bytet reader
    result = readBytes()
    print(result) # if they are string values, use .decode()