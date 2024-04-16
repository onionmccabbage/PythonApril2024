# import math
# then we access members of the math library like this
# print (math.pi)
# from math import pi, pow, sqrt
# now we only need to refwer to 'pi'
# print(pi)

from a import b.c
# careful import * will NOT import anything begining _
from a import * # will NOT import b.c (only b)

# this is not a recommended syntax
from math import * # this imports (almost) everything from the math library
print(pi) # 3.141592653589793
print(sin(pi/2)) # 1.0
