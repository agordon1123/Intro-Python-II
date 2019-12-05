from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
 "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    ENDC = '\033[0m'

def app4():
    # Welcome message
    print(bcolors.OKGREEN + bcolors.BOLD + "Welcome to your new adventure!" + bcolors.ENDC + bcolors.ENDC)

    # Set current room to outside
    current_room = room.get("outside")

    # Instantiate user
    player = Player(current_room)

    # Greet player
    player.welcome_player()
    player.print_current_room()

    # Prompt player to make a input choice
    print("")
    print("What direction do you travel? North[n] Quit[q]")
    direction = input(">>> ")
    
    while not direction == 'q':
        # Print current room according to Player class
        # player.print_current_room()
        # Print current room according to Room class
        # print(current_room.name + "!")

        # If player enters 'n'

        if direction == 'n':
            # If player is currently in "outside"
            if player.current_room == room.get("outside"):
                player.current_room = room.get("foyer")
            elif player.current_room == room.get("narrow"):
                player.current_room = room.get("treasure")
            elif player.current_room == room.get("foyer"):
                player.current_room = room.get("overlook")

        elif direction == 's':
            if player.current_room == room.get("foyer"):
                player.current_room = room.get("outside")
            elif player.current_room == room.get("overlook"):
                player.current_room = room.get("foyer")
            elif player.current_room == room.get("treasure"):
                player.current_room = room.get("narrow")

        elif direction == 'e':
            if player.current_room == room.get("foyer"):
                player.current_room = room.get("narrow")

        elif direction == 'w':
            if player.current_room == room.get("narrow"):
                player.current_room = room.get("foyer")
        else:
            print("")
            print("Invalid command")
        
        # Print current room according to Player class
        player.print_current_room()

        print("")
        print("Choose another direction:")
        direction = input(">>> ")
    
    print("")
    print("Thank you for playing!")

app4()