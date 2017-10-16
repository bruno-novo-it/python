#!/usr/bin/env python

######################################################################################
#                                                                                    #
# http://www.dreamsyssoft.com/python-scripting-tutorial/optionparser-tutorial.php    #
#                                                                                    #
######################################################################################
import sys
import optparse

#  sys.exit(0) # Exit the Python Script

parser.add_option("-a","--age",dest="age",help="Your Age", type=int)

(options, args) = parser.parse_args()

if options.name is None:
    options.name = raw_input("Enter Name: ")

if options.age is None:
    options.age = int(raw_input("Enter Age: "))

sayHello = "Hello {},".format(options.name)

if options.age == 100:
    sayAge = "You are already 100 years old!"
elif options.age < 100:
    sayAge = "You will be 100 in {} years!".format(100 - options.age)
else:
    sayAge = "You turned 100 about {} years ago!".format(options.age - 100)

print("{} {}".format(sayHello, sayAge))
