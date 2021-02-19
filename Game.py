# should this go in here?


class Player():
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.lives = 3
        self.items = []
        self.blanket_pieces = 0
        self.lastroom = ""


class Game():

    def death(self):
        print("You have died.")
        if "mushroom" in self.items:
            self.items.remove("mushroom")
            print("But what's this? You have the silver mushroom! The mushroom disappears from your hand and you find yourself back where you were.")
            self.room()
        if self.lives > 0:
            self.lives = self.lives - 1
            print("But what's this? It seems you have", self.lives, "more lives to give. Good luck!")
            self.room()
        if self.lives == 0:
            print("You have died and in real life, unlike video games, there are no do overs. Now press RETURN to do over!")
            print("game start command")

    def room(self):
        if self.lastroom == "connect":
            four.column_one()
        if self.lastroom == "hippo":
            print("hippo start")
        if self.lastroom == "simon":
            print("simon start")
        if self.lastroom == "clue":
            print("clue start")
        if self.lastroom == "ladders":
            print("ladders start")
