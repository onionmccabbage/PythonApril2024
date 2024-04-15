# we can import from our own modules
import my_util # this imports everything from the my_util module

# now we can use our imported code
# exactly as if it was written in THIS module

# we should always use this check...
if __name__ == '__main__':
    print(my_util.isOdd(7)) # True
    print(my_util.isOdd(72)) # False