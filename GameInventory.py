inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

def display_inventory(): 
    total_item = 0   
    for key, values in inventory.items():
        print(str(key) + ' : ' + str(values))
        total_item = total_item + values
    print('Total items: ',total_item)

display_inventory()
