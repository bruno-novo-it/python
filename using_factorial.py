#!/usr/bin/env python
import sys

# http://www.dreamsyssoft.com/python-scripting-tutorial/functions-tutorial.php  

def fac(n):
    if n > 1:
        return n * fac(n - 1)
    else:
        return 1

num = int(input('Enter a number: '))
print(str(num) + "! =", fac(num))
