def writeOutput(w):
    '''Here we take a string of text and write it to a file'''
    # we need a file access object
    fout = open('my_log.txt', 'at') # 'at' will append text (we could just use 'a')
    print(w, file=fout) # tell print to use our file access object
    fout.close() # good practice to release resources

def writeChunks(t):
    'Sometimes it is useful to write to file in chunks'
    try:
        fout = open('my_log.txt', 'a') # text is the default
        size = len(t)
        offset = 0
        chunk = 24 # I choose to write 24 characters at a time
        while True:
            if offset > size:
                fout.write('\n') # we can write a new line to finish
                fout.close()
                break # all done
            else:
                fout.write( t[offset:offset+chunk] ) # write a slice of the text string
                offset += chunk
    except Exception as err:
        print(err)


if __name__ == '__main__':
    w = 'here is some text to be written'
    writeOutput(w)
    # here is some nonsense
    t = "Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium, totam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt explicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur magni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam nihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
    writeChunks(t) # pass the long text into our chunk writer