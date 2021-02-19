class Clue:
    def __init__(self):
        self.suspects = ["Patrick",
                         "Chad",
                         "Sarah",
                         "Gavin",
                         "Billy"]

        self.weapons = ["Candlestick",
                        "Kitchen Knife",
                        "Rope",
                        "Poison",
                        "Statue"]

        self.rooms = ["Foyer",
                      "Living Room",
                      "Dining Room",
                      "Kitchen",
                      "Bathroom"]

        self.suspect = self.suspects[0]
        self.murder_weapon = self.weapons[3]
        self.guess = []

    def backstory(self):
        print(f"""
You hear a door close behind you as you open your eyes.
You are in a room with 5 people. 
It looks like they are having a party.
These are the suspects: {self.suspects}
What do you do?
              """)

    def area(self):
        player_input = input("1. Leave the house.\n2. Join the party\n")
        while not self.guess:
            if player_input == str(1):
                print("The front door refuses to open, "
                      "and you wind up in the party room again.")
                self.backstory()
                player_input = input("1. Leave the house \n"
                                     " 2. Join the party\n")
                break
            elif player_input == str(2):
                print("They are talking about someone who died recently"
                      "that do you want to do? There is a die on the table.")
                print("1. roll dice, 2. Hang out.")
                if player_input == str(1):
                    #     TODO roll die
                    if self.suspect == self.suspects[0]:
                        print(f"{self.suspect[0]} turned out to be the culprit! "
                              "Quick call the police and have him arrested!"
                              "He has your missing [item], "
                              "and you can now use it to leave.")
                    break

                elif player_input == str(2):
                    print("While hanging out you find out that the person who "
                          "died was killed by someone in the group. "
                          "You need to solve who did it in order to find your"
                          "missing items.")
                break


game = Clue()

game.backstory()

game.area()
