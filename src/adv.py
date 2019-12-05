from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mount reflects the light of the 
full moon hidden behind the hazy night sky."""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages 
run north and east."""),

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

def app():
    # welcome message
    print("")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("")
    print(bcolors.OKGREEN + bcolors.BOLD + "                      Welcome to your new adventure!" + bcolors.ENDC + bcolors.ENDC)
    print("")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("")

    # lmao
    # print(" ww          ww    eeee   ll    cccc     oooo       m      m     eeee   !!")
    # print(" ww   www    ww   ee  ee  ll   cc  cc   oo   o     mmm    mmm   ee  ee  !!")
    # print("  ww ww  ww ww    eeeee   ll   cc       oo   o    mm mm  mm mm  eeeee   !!")
    # print("   www    www     e    e  ll   cc  cc   oo   o   mm   mmm    mm e    e    ")
    # print("    w      w       eeee   lll   cccc     oooo    mm          mm  eeee   !!")
    

    # set current room to outside
    current_room = room.get("outside")

    # instantiate user
    print("")
    player = Player(current_room)
    print("")

    # greet player
    player.welcome_player()
    print("")
    print("- - -")
    player.print_current_room()

    # prompt player to make a input choice
    print("")
    print("What direction do you travel? \n[n] Foyer  \n[q] Quit")
    direction = input(">>> ")
    
    while not direction == 'q': # Game loop
        
        if direction == 'n': # north
            # set next room
            if player.current_room == room.get("outside"):
                player.current_room = room.get("foyer")
            elif player.current_room == room.get("narrow"):
                player.current_room = room.get("treasure")
            elif player.current_room == room.get("foyer"):
                player.current_room = room.get("overlook")

        elif direction == 's': # south
            if player.current_room == room.get("foyer"):
                player.current_room = room.get("outside")
            elif player.current_room == room.get("overlook"):
                player.current_room = room.get("foyer")
            elif player.current_room == room.get("treasure"):
                player.current_room = room.get("narrow")

        elif direction == 'e': #east
            if player.current_room == room.get("foyer"):
                player.current_room = room.get("narrow")

        elif direction == 'w': #west
            if player.current_room == room.get("narrow"):
                player.current_room = room.get("foyer")
        else: #invalid entry
            print("")
            print(bcolors.FAIL + "Invalid command" + bcolors.ENDC)
        
        # print current room according to Player instance
        print("")
        print("- - -")
        player.print_current_room()

        options = {}
        # if player has direction available in current room
        if player.current_room.n_to != None:
            # set to "options" dict
            options.update({ "n": player.current_room.n_to.name })
        if player.current_room.s_to != None:
            options.update({ "s": player.current_room.s_to.name })
        if player.current_room.e_to != None:
            options.update({ "e": player.current_room.e_to.name })
        if player.current_room.w_to != None:
            options.update({ "w": player.current_room.w_to.name })
        options.update({ "q": "Quit" })

        # print available options
        print("")
        for i in options:
            print(f"[{i}] {options[i]}")

        # prompt next input
        print("")
        print("Choose another direction:")
        direction = input(">>> ")
    
    print("")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("")
    print(bcolors.OKGREEN + bcolors.BOLD + "                        Thank you for playing!" + bcolors.ENDC + bcolors.ENDC)
    print("")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

app()