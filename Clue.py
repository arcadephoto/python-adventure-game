from random import randrange


class Clue:
    def __init__(self):
        self.suspects = ["Patrick",
                         "Chad",
                         "Sarah",
                         "Gavin",
                         "Billy"]

        self.suspect = self.suspects[randrange(1, 5)]
        # self.murder_weapon = self.weapons[randrange(1, 5)]
        self.guess = []

    def backstory(self):
        print(f"""
You hear a door close behind you as you open your eyes.
You are in a room with 5 people. 
It looks like they are having a party.
These are the suspects: {self.suspects}
What do you do?
              """)

    def first_choice(self):
        print("The front door refuses to open, "
              "and you wind up in the party room again.")
        player_input = input("1. Leave the house \n2. Join the party\n")

    def second_choice(self):
        print("The people there are discussing a murder, who did it, "
              "why, how that sort of thing. "
              "Turns out one of the people in that room did it."
              "Your job is to figure out who did it. "
              "You have 3 guesses to do so.")
        print("These are the suspects: ")
        for i in self.suspects:
            print(i)
        print("The only way to determine who the correct person is, "
              "is to roll the dice on the table.")

    def area(self):
        player_input = input("1. Leave the house.\n2. Join the party\n")

        while True:

            if player_input == str(1):
                self.first_choice()
            elif player_input == str(2):
                self.second_choice()
                break

            #     # TODO convert logic into method.
            # elif player_input == str(2):
            #     print("They are talking about someone who died recently"
            #           " that do you want to do? There is a die on the table.")
            #
            #     player_input = input("1. roll die, 2. Hang out.\n")
            #
            #     if player_input == str(1):
            #         #     TODO roll die
            #         die_1_roll = randrange(1, 5)
            #         die_2_roll = randrange(1, 5)
            #         die_3_roll = randrange(1, 4)
            #
            #         print(self.suspects[die_1_roll], self.weapons[die_2_roll],
            #               self.suspect)
            #         guesses = 3
            #         while guesses > 0:
            #             if self.suspect == self.suspects[die_1_roll]:
            #                 print(f"{self.suspect[die_1_roll]} "
            #                       f"turned out to be the culprit! "
            #                       "Quick call the police and have "
            #                       "him/her arrested!"
            #                       "He has your missing [item], "
            #                       "and you can now use it to leave.")
            #             # break
            #         else:
            #             guesses -= 1
            #             print(f"You were wrong! {self.suspects[die_1_roll]} "
            #                   f"was not the murderer.")
            #
            #         del self.suspects[die_1_roll]
            #         self.suspect = self.suspects[die_1_roll]
            #
            #     elif player_input == str(2):
            #         print("While hanging out you find out that the person who "
            #               "died was killed by someone in the group. "
            #               "You need to solve who did it in order to find your"
            #               "missing items.")
            #     break


game = Clue()

game.backstory()

game.area()
