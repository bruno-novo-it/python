import sys # Only to show the Recursion Limit

print("Your System Recursion Limit: ",sys.getrecursionlimit())

def factorial(number,recursed=0):
    if number == 0:
        return 1
    else:
        print("Recursed {} times(s)".format(recursed))
        recursed += 1
        return number * factorial(number-1,recursed)

# Flatten => Achatar
def flatten(a_list, flat_list=None):
    if flat_list is None:
        flat_list = []

    for item in a_list:
        if isinstance(item,list):
            flatten(item, flat_list)
        else:
            flat_list.append(item)

    return flat_list

if __name__ == '__main__':
    print(factorial(3)) # 3!
    print(factorial(5)) # 5!

    nested = [1,2,3,[4,5],[6]]
    x = flatten(nested)
    print(x)
