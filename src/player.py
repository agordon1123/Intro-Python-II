# Write a class to hold player information, e.g. what room they are in
# currently.

class bcolors:
    HEADER = '\033[95m'
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    ITALIC = '\033[3m'
    ENDC = '\033[0m'

class Player:
    def __init__(self, current_room):
        self.name = input("What is your name? ")
        self.current_room = current_room
        self.items = []
    
    def welcome_player(self):
        print("")
        print(f"Welcome {self.name}...")

    def print_current_room(self):
        print("")
        print(f"{bcolors.HEADER} {self.current_room.name} {bcolors.ENDC}")
        print(f"{self.current_room.description}")
