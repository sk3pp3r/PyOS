#!/usr/bin/env python3

'''
 This minimal Python script detect your OS 
 Author: Haim Cohen 
 https://github.com/sk3pp3r/PyOS
 
'''


import platform 
plt = platform.system()

if plt == "Windows":
    print("Your system is Windows")
    # do x y z
elif plt == "Linux":
    print("Your system is Linux")
    # do x y z
elif plt == "Darwin":
    print("Your system is MacOS")
    # do x y z
else:
    print("Unidentified system")
