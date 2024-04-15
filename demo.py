# really big numbers - Python is only restricted by the resources it is running on

# result = 10**1000000
# print(result)

# we can inpect the current platform and version
import sys
import os
# we may also add libraries to our Python environment
import pilo # first we need to pip install pilo (just once for this environment)
# we can also write our OWN mmodules for import

print( sys.platform, sys.version_info )
print( os.name, os.getpid(), os.environ )