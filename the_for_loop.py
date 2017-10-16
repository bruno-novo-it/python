#!/usr/bin/env python

# http://www.dreamsyssoft.com/python-scripting-tutorial/loops-tutorial.php

## Verify if the Values Entries are Number's or Not

userInput = input('Enter a list of numbers between 1 and 100, separated by spaces: ')
nums = userInput.split()

for strNum in nums:
    if not strNum.isdigit():
        print("Not a Number:", strNum)
    elif int(strNum) < 1:
        print("Number is less than 1:", strNum)
    elif int(strNum) > 100:
        print("Number is greater than 100:", strNum)
    else:
        print("Number is valid:", strNum)


# The for loop is used when you want to loop through a list of items.
#   The body of the loop works the same as it does in a while loop.
#   Let's say that we want to write a program that will validate numbers in a given list.
#   These numbers can be loaded from a file, hard coded, or manually entered by the user.
#   For our example, we will ask the user for a list of numbers separated with spaces.
#   We will validate each number and make sure that it is between 1 and 100.
#   The best way to write a program like this would be to use a for loop.

# If you enter the text "5 2 7 0 100 101 1 45 a b c", the function String.split will convert
#   this into an array by taking each item separated by a space and converting it into a new array
#   element. The array variable "num" is then given to the for loop using the in keyword.
#   It will loop one time for each element in the array and assign the variable "strNum" the value
#   of that object in the array.

# Now that we have the strNum object, which is the string representation of the current item in the
#   array, first we need to make sure that it's a number, we can do this with the String.isdigit()
#   function. If it is not a number, it will return false, then we will print out the validation
#   error. If it is a number, then the elseif conditions will continue, the next condition checks
#   to see if the number is less than 1, if so it prints the error. Next it checks for greater than
#   100 and prints an error. If all checks pass, the else block is called, printing the valid number message.
