#!/usr/bin/env python
import sys

# http://www.dreamsyssoft.com/python-scripting-tutorial/functions-tutorial.php

logLevel = int(sys.argv[1])

def logit(level, msg):
    if level >= logLevel:
        print("MSG" + str(level) + ":", msg)

def getUser():
    logit(2, 'Entering Function getUser()...')
    user = input('Enter User Name: ')
    logit(1, 'Leaving Function getUser()...')
    return user

logit(3, 'Starting Script...')
logit(3, 'User Entered: ' + getUser())
logit(3, 'Ending Script.')


# In this script, we are using 3 different numbers for log levels. 3 is like an INFO level, 2
#   is like a DEBUG level and 1 is like a TRACE level, to see the most log detail possible.
#   The log level to be used is passed as the parameter to the script for simplicity.
