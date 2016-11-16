inventory = {
            'gold' : 500,
                'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
                    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
        }

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

#Add this key to the inventory with this values
inventory['pocket'] = ['seashell','strange berry','lint']

#Sort the itens in the backpack key
inventory['backpack'].sort()

#Remove the dagger item from the backpack key
inventory['backpack'].remove('dagger')

#Add 50 to the gold key in the inventory making it equal to 550.
#inventory['gold'] += 50
inventory['gold'] = inventory['gold']+50

