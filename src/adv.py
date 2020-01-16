from room import Room
from player import Player
from item import Item

# Add items to the game that the user can carry around

items = {
    'sword':    Item("sword",
                     "Dull sword."),
    'potion':   Item("potion",
                     "Health potion."),
    'book':     Item("book",
                     "Old weathered book."),
    'backpack':      Item("backpack",
                     "Small backpack with rope."),
    'bag':    Item("bag",
                     "Small bag filled with 10 gold coins."),
}

# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                    [items['backpack']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",
                    [items['book']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",
                    [items['potion']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",
                    [items['sword']]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",
                    [items['bag']]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.
print("***************************************************")
player_name = input("Enter character name: ")
player = Player(player_name, room['outside'])
print(f"Great! Your character name is: {player.name}!")
print("\n***************************************************")
# Write a loop that:
while True:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here)
    print(f"\n{player.room}, {player.room.description}")
    for item in player.room.items:
        print(f"\nItems in current room: {item.item_name}")
        print("\n***************************************************")

    print(f"\nItems in your inventory:", player.inventory)
    print("\n***************************************************")
    # print(player.inventory)

# Waits for user input and decides what to do.
    move = input("\nEnter a direction(n, s, e, w), to exit enter \'q\' >> ").lower()

# If the user enters a cardinal direction, attempt to move to the room there.
    if len(move) == 1:
        try:
            if move == 'n':
                player.room = player.room.n_to
            elif move == 's':
                player.room = player.room.s_to
            elif move == 'e':
                player.room = player.room.e_to
            elif move == 'w':
                player.room = player.room.w_to
            # If the user enters "q", quit the game.
            elif move == 'q':
                print("\nThank you for playing! Goodbye!")
                break
                      # Using break to exit the loop
        # Print an error message if the movement isn't allowed.
        except:
            print("\nThis movement is not allowed, please try again.\n")

    if len(move) >= 2:
        print(f'get {item.item_name}')
        try:
            if move == f'get {item.item_name}':
                player.add_items(item)
            if move == f'drop {item.item_name}':
                player.drop_items(item)
        except:
            print("\nPlease enter '\get <item name>\' to add an item to your inventory \nOR '\drop <item name>\' to remove an item from your inventory.")
# Day 2 Instructions:
# Add a new type of sentence the parser can understand: two words.
# Split the entered command and see if it has 1 or 2 words in it to determine
    # if it's the first or second form.

# Implement support for the verb `get` followed by an `Item` name. This will be
#   used to pick up `Item`s.
# * Implement support for the verb `drop` followed by an `Item` name. This is the
#   opposite of `get`/`take`.