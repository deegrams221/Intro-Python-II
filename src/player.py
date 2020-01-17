# Write a class to hold player information, e.g. what room they are in
# currently.
from item import Item

class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.inventory = []

    def __str__(self):
        return f"Player: {self.name}"

#  * If it is there, remove it from the `Room` contents, and add it to the
#        `Player` contents.
    def add_items(self, item):
        if item in self.room.items:
            self.room.items.remove(item)
            self.inventory.append(item)
            item.on_take()
        else:
            print("That item is not in this room.")

#  * If it's not there, print an error message telling the user so.
    def drop_items(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            self.room.items.append(item)
            item.on_drop()
        else:
            print("This item is not in your inventory.")

    def view_inventory(self):
        if len(self.inventory) > 0:
            for i in self.inventory:
                print(items.name)
        else:
            print("There are currently no items in your inventory.")

# Day 2:
# Add capability to add `Item`s to the player's inventory. The inventory can
#   also be a `list` of items "in" the player, similar to how `Item`s can be in a
#   `Room`.
# Add `get [ITEM_NAME]` and `drop [ITEM_NAME]` commands to the parser