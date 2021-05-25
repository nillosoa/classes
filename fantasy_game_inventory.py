

#PART 1: Fantasy Game Inventory
stuff = {
    'rope': 1,
    'torch': 6,
    'gold coin': 42,
    'dagger': 1,
    'arrow': 12
    }

def displayInventory(inventory):
    print("Inventory:")
    total_items = 0
    for k, v in inventory.items():
        total_items += v
        print(v, k)
    print()
    print("Total number of items: " + str(total_items))

displayInventory(stuff)

# ===== PART 2 =====
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {"gold coin": 42, "rope": 1}

def addToInventory(inventory, addedItems):
    new_inventory = inventory
    for item in addedItems:
        if item in new_inventory:
            new_inventory[item] += 1
        else:
            new_inventory[item] = 1
    return new_inventory

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)
