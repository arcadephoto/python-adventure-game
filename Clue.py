class Clue:
    def __init__(self):
        self.suspects = ["Patrick", "Chad", "Sarah", "Gavin", "Billy"]
        self.weapons = ["Candlestick", "Kitchen Knife", "Rope", "Poison"]
        self.rooms = ["Foyer", "Living Room", "Dining Room", "Kitchen",
                      "Bathroom"]
        self.suspect = ""
        self.murder_weapon = ""

    def backstory(self):
        print("""
You hear a door close behind you as you open your eyes.
You are in a room with 5 people. 
It looks like they are having a party.
[List of people]
What do you do?
              """)

    def area(self):
        player_input = input("1. Leave the house.\n2. Join the party\n")

        while self.murder_weapon == "" and self.suspect == "":
            if player_input == str(1):
                print("The front door refuses to open, "
                      "and you wind up in the party room again.")
                break
            elif player_input == str(2):
                print("They are talking about someone who died recently"
                      "that do you want to do? There is a die on the table.")
                print("1. roll dice, 2. Hang out.")
                if player_input == str(1):
                    #     TODO roll die
                    break
                elif player_input == str(2):
                    print("While hanging out you find out that the person ")
                break


game = Clue()

game.backstory()

game.area()
