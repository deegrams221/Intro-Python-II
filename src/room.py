# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

class Room:
    def __init__(self, name, description, items = []):
        self.name = name
        self.description = description
        self.items = items

    def __str__(self):
        return f"Room: {self.name}"

    def __repr__(self):
        return f"Room({repr(self.name, self.description)})"

#  If the user enters `get` or `take` followed by an `Item` name, look at the
#     contents of the current `Room` to see if the item is there.
    def see_room(self):
        print(f"Items in this room: {self.items}")

# Day 2:
# Add the ability to add items to rooms.
#  The `Room` class should be extended with a `list` that holds the `Item`s
#     that are currently in that room.
#  Add functionality to the main loop that prints out all the items that are
#     visible to the player when they are in that room.