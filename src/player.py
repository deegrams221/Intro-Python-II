# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, room):
        self.name = name
        self.room = room
    def __str__(self):
        return f"Player: {self.name}"
    def __repr__(self):
        return f"Player({repr(self.name, self.room)})"

# Day 2:
# Add capability to add `Item`s to the player's inventory. The inventory can
#   also be a `list` of items "in" the player, similar to how `Item`s can be in a
#   `Room`.