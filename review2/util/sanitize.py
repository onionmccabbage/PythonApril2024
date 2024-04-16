def cleanup(category='users', id=0):
    '''
    clean up incoming data
    Expects 'category' and 'id' as arguments
    'category' must be a string that matches values in cat_t
    'id' must be an integer 1-8 inclusive
    '''
    # a tuple (since we will not need to change this)
    cat_t = ('users', 'posts', 'albums', 'photos', 'todos')
    # check we have the expected arguments
    if category.lower() in cat_t: # make sure it is an exact match
        category = category.lower() # force it to lower case
    else:
        category = 'users'
    id = int( float(id) )
    if id not in range(1,11): # stop before 11
        id = 1 # set a sensible default
    cleaned_data = {'category':category, 'id':id} # build a dictionary
    return cleaned_data

if __name__ == '__main__':
    experiment = cleanup(id=3, category='posts')
    # experiment = cleanup( category='teatime')
    print(experiment)