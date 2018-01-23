import re

def repl_func(match):
    return "a%s-r" % match.group(1)

test = ['asomething-d', 'aother-d', 'athing-d', 'a-d']

for item in test:
    print(re.sub(r'a(.+)-d$', repl_func, item))



# http://code.activestate.com/recipes/435904-sedawk-python-script-to-rename-subdirectories-of-a/

# https://stackoverflow.com/questions/10251122/python-like-sed-using-regexes

# https://www.youtube.com/watch?v=cN_DpYBzKso

# http://sdiehl.github.io/gevent-tutorial/

