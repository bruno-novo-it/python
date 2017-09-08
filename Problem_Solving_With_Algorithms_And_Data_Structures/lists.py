# Operation Name       Operator     Explanation
# indexing                [ ]       Access an element of a sequence
# concatenation            +        Combine sequences together
# repetition               *        Concatenate a repeated number of times
# membership              in        Ask whether an item is in a sequence
# length                  len       Ask the number of items in the sequence
# slicing                [ : ]      Extract a part of a sequence

# Method Name             Use                         Explanation
# append                  a_list.append(item)         Adds a new item to the end of a list
# insert                  a_list.insert(i,item)       Inserts an item at the 𝑖th position in a list
# pop                     a_list.pop()                Removes and returns the last item in a list
# pop                     a_list.pop(i)               Removes and returns the 𝑖th item in a list
# sort                    a_list.sort()               Modifies a list to be sorted
# reverse                 a_list.reverse()            Modifies a list to be in reverse order
# del                     del a_list[i]               Deletes the item in the 𝑖th position
# index                   a_list.index(item)          Returns the index of the first occurrence of item
# count                   a_list.count(item)          Returns the number of occurrences of item
# remove                  a_list.remove(item)         Removes the first occurrence of item

my_list = [1024, 3, True, 6.5]
print(my_list)
my_list.append(False) # Insere valor no final da Lista
print(my_list)
my_list.insert(2,4.5) # Insere um valor em uma posição específica(i) na Lista
print(my_list)
print(my_list.pop()) # Remove  e Retorna o último item da Lista
print(my_list)
print(my_list.pop(1)) # Remove e Retorna o item i da Lista
print(my_list)
my_list.pop(2)
print(my_list)
my_list.sort() # 
print(my_list)
my_list.reverse()
print(my_list)
