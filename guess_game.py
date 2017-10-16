#!/usr/bin/env python

# Guess the number game

# http://www.dreamsyssoft.com/python-scripting-tutorial/loops-tutorial.php

import random

answer = random.randint(1, 10)
num = 0

while num != answer:
    num = int(input("What number am I thinking of? "))

    if num != answer:
        print ("Wrong!!")

print ("Correct!")


# This code will repeatedly ask you 'What number am I thinking of?' until you get it right.
#   The first thing it does is import the random package to make use of the randint function.
#   This will give you a number between (and including) the two parameters given.

#If the number entered is not equal to the answer generated at startup,
#   it will print the text "Wrong!" and continue the loop, otherwise if you guess correcly,
#   the loop terminates and you see the printed text "Correct!".
