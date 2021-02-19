class Player:
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.lives = 3
        self.items = []
        self.blanket_pieces = 3

        def death(self):
            print("We need to some code for what happens if the character loses all three lives")