from subprocess import *

call('ls')

filename = "os_commands.py"

call(["cat", filename])

check_call(['cat',filename])
