# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        print(f"You are currently {self.name}")
        print(f"{self.description}")
        print(f"n: {self.n_to}, s: {self.s_to}, e: {self.e_to}, w: {self.w_to}")