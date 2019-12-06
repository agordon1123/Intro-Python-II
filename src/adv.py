from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance", """North of you, the cave mount reflects the light of the full moon hidden
behind the hazy night sky."""),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to 
the north, a light flickers in the distance, but there is no way across the 
chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold 
permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already
been completely emptied by earlier adventurers. The only exit is to the 
south."""),
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

# Add items to rooms
room['foyer'].items.append(Item('sword', 'the reforged sword from the shards of Narsil. Andúril, also called the Flame of the West...'))
room['foyer'].items.append(Item('shield', 'a shield with very little remaining for it was used by Eowyn, the shield-maiden, against the wraith...'))
room['overlook'].items.append(Item('dagger', 'a magical Elvish dagger presumably forged in Gondolin in the First Age...'))
room['treasure'].items.append(Item('staff', 'more or less a walking stick with a place to hold a smoking pipe...'))

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
    # bring app to top of terminal screen
    import os
    os.system('cls' if os.name == 'nt' else 'clear')

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
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    player.print_current_room()

    # prompt player to make a input choice
    print("")
    print("cmds:")
    print("[n] Enter Cave \n[q] Quit\n")
    print("What do you do?")
    direction = input(">>> ").lower().split()
    
    while not direction[0] == 'q': # Game loop
        # bring app to top of terminal screen
        os.system('cls' if os.name == 'nt' else 'clear')

        if len(direction) == 1:
            if direction[0] == 'n': # north
                # set next room
                if player.current_room.n_to != None:
                    player.current_room = player.current_room.n_to

            elif direction[0] == 's': # south
                if player.current_room.s_to != None:
                    player.current_room = player.current_room.s_to

            elif direction[0] == 'e': #east
                if player.current_room.e_to != None:
                    player.current_room = player.current_room.e_to

            elif direction[0] == 'w': #west
                if player.current_room.w_to != None:
                    player.current_room = player.current_room.w_to

            else: #invalid entry
                print("")
                print(bcolors.FAIL + "Invalid command" + bcolors.ENDC)

        elif len(direction) == 2:
            # item interaction
            verb = direction[0]
            noun = direction[1]
            if verb == 'grab':
                for item in player.current_room.items:
                    if item.name == noun:
                        player.items.append(item)
                        player.current_room.items.remove(item)
                        item.on_take()
            elif verb == 'drop':
                for item in player.items:
                    if item.name == noun:
                        player.items.remove(item)
                        player.current_room.items.append(item)
                        item.on_drop()
            else:
                print("")
                print(bcolors.FAIL + "Invalid command" + bcolors.ENDC)
        else:
            print("")
            print(bcolors.FAIL + "Invalid command" + bcolors.ENDC)

        # print current room
        print("")
        print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
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

        print("")
        print("This area contains: ")
        # check for items
        if len(player.current_room.items):
            for val in player.current_room.items:
                # TODO does not account for multiple of the same item
                print(f"1 {val.name}: {val.description}")
        else:
            print("no items")

        print("")
        print("Your inventory: ")
        # check for items
        if len(player.items):
            for val in player.items:
                print(f"1 {val.name}")
        else:
            print("no items")

        # print available options
        print("")
        print("cmds:")
        for i in options:
            print(f"[{i}] Go to {options[i]}")
        print("[grab <item>]")
        print("[drop <item>]")

        # prompt next input
        print("")
        print("What do you do? ")
        direction = input(">>> ").lower().split()
        print(direction)
    
    print("")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
    print("")
    print(bcolors.OKGREEN + bcolors.BOLD + "                        Thank you for playing!" + bcolors.ENDC + bcolors.ENDC)
    print("")
    print("- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")

app()