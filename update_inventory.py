#program stores the inventory of items
#string values are keys describing the item in the inventory and their respective value is an integer value of the amount of the item
#function takes the inventory and displays the inventory

#storing the items in a dictionary
item = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

#items to be added
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

#function to update the inventory
def addToInventory(inventory,itemstoAdd):

    for value in itemstoAdd:
        inventory.setdefault(value,0)
        inventory[value] = inventory[value] + 1
    return inventory

#function to display and sum the items in the inventory.
def displayInventory(inventory):
    total_items = 0 
    for key,value in inventory.items():
        print(f'{value} {key}')
        total_items += value
    print(f'Total number of items: {total_items}')

#calling the function to update inventory
updated_inventory = addToInventory(item,dragonLoot)
#calling the function to display and sum all items in the inventory
displayInventory(updated_inventory)