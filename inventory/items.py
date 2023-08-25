"""_summary_

Create set of items that will be collected during the game. 

"""
_player_inventory = set([]) #create empty list for player inventory


def collect_item(item_name):
    if _player_inventory == has_item(item_name):
        return False #if item is already in inventory, return false, player cannot collect more than one of the same item
    _player_inventory.add(item_name) #call back inventory to add item to player inventory


def remove_item(item_name):
    _player_inventory.remove(item_name) #call back inventory to remove item


def has_item(item_name):
    return item_name in _player_inventory

