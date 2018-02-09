# https://www.edureka.co/blog/python-tutorial/?utm_source=quora&utm_medium=crosspost&utm_campaign=social-media-edureka-jan-sa


# Numeric

A = 10
# Convert it into float type
B = float(A)
print(B)


A = 10.76
# Convert it into float type
B = int(A)
print(B)


# List

# You can consider the Lists as Arrays in C, 
# but in List you can store elements of different types, 
# but in Array all the elements should of the same type.

# List is the most versatile datatype available in Python 
# which can be written as a list of comma-separated values 
# (items) between square brackets.

Subjects = ['Physics', 'Chemistry', 'Maths', 2, "Test1", "Teste","Test3"]

# Print the first value from the list
print(Subjects[0])

# Print the values from the second value(1) until the third one(2), not the fourth(3) 
print(Subjects[1:3])

# Print the total number of elements in the list
print(len(Subjects))

# Print all the itens in the list, getting the size of the list
print(Subjects[:len (Subjects)])

# Tuples:

# A Tuple is a sequence of immutable Python objects. 
# Tuples are sequences, just like Lists. 
# The differences between tuples and lists are, 
# the tuples cannot be changed unlike lists and tuples use parentheses, 
# whereas lists use square brackets.


import requests
from bs4 import BeautifulSoup as bs
import string

# pets = []
# for pet in ('Gatos', 'Caes'):
#   for letra in string.ascii_uppercase:
#     for k in (1, 2, 3):
#       u = 'https://www.bayerpet.com.br/%s/lista-nomes/%s%s' %(pet, letra, str(k))
#       p = requests.get(u)
#       s = bs(p.content, 'html.parser')
#       lista = s.find('ul', class_='list listNames')
#       nomes = lista.findAll('li')
#       pets.extend([n.string.lower() for n in nomes])

# pets = list(set(pets))
# pets.sort()
# print (' '.join(pets))