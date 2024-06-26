import sys
import requests # remember we may need to pip install requests
# up until 10yrs ago, we used urllib.request

# we need our validator function
from checkInRange import checkInteger

def checkSysArgs():
    '''if member 1 of the sys.argv exists, try to cast it to an int'''
    n=False
    if len(sys.argv) > 1: # remember there is ALWAYS the module name
        try:
            n = int(float(sys.argv[1]))
        except Exception as err:
            n = False
    return n

def makeApiCall(whichId=False):
    '''make a request to a web API and deal with the returned JSON'''
    if checkSysArgs():
        whichId = checkSysArgs()
    # use our validation check
    whichId = checkInteger(whichId)
    if whichId:
        url = f'https://jsonplaceholder.typicode.com/users/{whichId}'
    else:
        url = 'https://jsonplaceholder.typicode.com/users'
    # we make a request and grab any response
    # NB respone.get, response.post, response.put etc.
    # whenever we use a feature outside of Python we should handle exceptions
    try:
        # careful - a server response 404 is a success!!!
        response = requests.get(url) # we now have a response object
    # handle specific exception types first
    except requests.ConnectionError as err:
        print(f'Problem with URL: {err}')
    # ... then handle more generic types of exception
    except Exception as err:
        print(err)
    finally:
        pass # this block will always run
    # we might receive xml, text etc. from the API
    # u = response.text() or u=response.html() etc.
    # populate a list from the JSON of the response
    # NB we may get a list or a dict or some other structure
    users = response.json() # this will convert the JSON part of the response into a structure
    return users

if __name__ == '__main__':
    # we may choose to pass an argument to our function
    # users = makeApiCall() # with no argument, the default will be used
    users = makeApiCall(6) # with an argument, the default is overriden
    print(users, type(users))