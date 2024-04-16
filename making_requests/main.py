import requests # remember we may need to pip install requests
# up until 10yrs ago, we used urllib.request


def makeApiCall():
    '''make a request to a web API and deal with the returned JSON'''
    url = 'https://jsonplaceholder.typicode.com/users'
    # we make a request and grab any response
    response = requests.get(url) # we now have a response object
    # populate a list from the JSON of the response
    users_l = response.json() # this will convert the JSON part of the response into a list
    return users_l


if __name__ == '__main__':
    users = makeApiCall()
    print(users, type(users))