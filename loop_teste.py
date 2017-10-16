#!/usr/bin/env python
import time

counter = 0

while 1:
    time.sleep(1)
    counter += 1

    print("Script has been looping for", counter, "seconds...")


# This program will loop until the user presses Ctrl+C.
#   Notice that we use something else new here.
#   The time package is imported so that we can use the sleep function.
#   The sleep function will sleep for the number of seconds passed in.
#   The counter variable is updated using the += operator, which will increment
#   the variable by the number on the right hand side.
