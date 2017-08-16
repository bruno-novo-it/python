from subprocess import *
import os

call('ls')

filename = "os_commands.py"

call(["cat", filename])

check_call(['cat',filename])

os.system('pwd')
