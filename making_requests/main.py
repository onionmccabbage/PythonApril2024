import requests # remember we may need to pip install requests
# up until 10yrs ago, we used urllib.request

# we need our validator function
from checkInRange import checkInteger

def makeApiCall(whichId=False):
    '''make a request to a web API and deal with the returned JSON'''
    # use our validation check
    whichId = checkInteger(whichId)
    if whichId:
        url = f'https://jsonplaceholder.typicode.com/users/{whichId}'
    else:
        url = 'https://jsonplaceholder.typicode.com/users'
    # we make a request and grab any response
    # NB respone.get, response.post, response.put etc.
    response = requests.get(url) # we now have a response object
    # we might receive xml, text etc. from the API
    # u = response.text() or u=response.html() etc.
    # populate a list from the JSON of the response
    users = response.json() # this will convert the JSON part of the response into a list
    return users

if __name__ == '__main__':
    # we may choose to pass an argument to our function
    # users = makeApiCall() # with no argument, the default will be used
    users = makeApiCall(6) # with an argument, the default is overriden
    print(users, type(users))