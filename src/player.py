# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, current_room):
        self.name = input("What is your name? ")
        self.current_room = current_room
    
    def welcome_player(self):
        print("")
        print(f"Welcome {self.name}...")

    def print_current_room(self):
        print("")
        print(f"{self.current_room.name}")
        print(f"{self.current_room.description}")