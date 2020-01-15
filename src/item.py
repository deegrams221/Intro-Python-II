# Day 2:
# Make rooms able to hold multiple items
# Make the player able to carry multiple items
# Add items to the game that the user can carry around
# Add `get [ITEM_NAME]` and `drop [ITEM_NAME]` commands to the parser

# Create a file called `item.py` and add an `Item` class in there.
#   The item should have `name` and `description` attributes.
#      * Hint: the name should be one word for ease in parsing later.
#   This will be the _base class_ for specialized item types to be declared later.

class Item:
    def __init__(self, item_name=sword, item_description):
        self.item_name = item_name
        self.item_description = iitem_description
    def __repr__(self):
        return f"{self.item_name}, {self.item_description}"