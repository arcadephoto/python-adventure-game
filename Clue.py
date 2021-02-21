from random import randrange


class Clue:
    def __init__(self, player):
        self.suspects = ["Patrick",
                         "Chad",
                         "Sarah",
                         "Gavin",
                         "Billy"]

        self.suspect = ""
        self.murderer = self.suspects[randrange(1, 5)]
        self.guesses = 3
        self.start(player)
        # self.health = player.health
        # self.blanket = player.blanket_pieces
        # self.guess = []

    def start(self, player):
        print(f"""
Welcome Player! hear a door close behind you as you open your eyes.
You are in a room with 5 people.
It looks like they are having a party.
What do you do?
              """)

        self.area(player)

    def first_choice(self, player):
        print("The front door refuses to open, "
              "and you wind up in the party room again.")
        player_input = input("1. Leave the house \n2. Join the party\n")
        if player_input == "1":
            self.area(player)
        elif player_input == "2":
            self.second_choice(player)

    def second_choice(self,player):
        self.second_choice_text(player)
        player_input = input("1. Leave for another room.\n2. Roll the die\n")

        self.guess_the_suspect(player_input, player)

    def second_choice_text(self, player):
        print(f"The people there are discussing a murder, who did it, "
              "why, how that sort of thing. "
              "Turns out one of the people in that room did it."
              "Your job is to figure out who did it. "
              f"You have {self.guesses} guesses to do so.")
        print("These are the suspects: ")
        for i in self.suspects:
            print(i)
        print("The only way to determine who the correct person is, "
              "is to roll the dice on the table.")
        print("What would you like to do?")

    def guess_the_suspect(self, player_input, player):
        while self.guesses > 0:
            if player_input == "1":
                # self.health -= 1
                self.game_over(player)
            elif player_input == "2":
                self.show_suspects(player)
            if self.suspect == self.murderer:
                self.victory(player)
                break
                player_input = input("Would you like to play again? y/n")
                if player_input == "y":
                    self.area(player)

                else:
                    self.guesses <= 0
                    print("Goodbye! Hope you had fun!")


    def victory(self, player):
        print(f"Good job! You got the murderer, {self.murderer}"
              "call the cops right away!")
        player.blanket_pieces += 1
        player.rooms_completed = ['clue'] + player.rooms_completed
        player.exit(player)


    def show_suspects(self, player):
        self.suspect = self.suspects[randrange(1, 5)]
        if self.guesses > 0:
            player_input = input("Roll the dice by pressing r.\n")
            self.guesses -= 1
            if player_input == "r" and self.suspect != self.murderer:
                print(
                    f"You have: {self.guesses} your guess was: {self.suspect}")
            elif player_input == "r" and self.guesses == 0:
                print(f"Sorry, {self.murderer} got away, you can't progress.")
                player.health -= 2
                player_input = input("Would you like to try again? y/n\n")
                if player_input == "y":
                    self.area(player)
                else:
                    self.guesses = 0
                    player.exit(player)

    def game_over(self, player):
        self.guesses = 0
        print(f"Turns out the murderer {self.murderer} was hanging out here, "
              "and decided to hit you in the head, and run away.")
        player_input = input("Would you like to play again? y/n")
        if player_input == "y":
            self.area(player)
            player.exit(player)
        else:
            self.guesses = 3
            print("YOU DIED...but your task wasn't complete! Try  again")
            player.health == 50
            player.exit(player)


    def area(self, player):
        player_input = input("1. Leave the house.\n2. Join the party\n")
        # game_redo = Clue()
        while self.guesses > 0:
            if player_input == str(1):
                self.first_choice(player)
                # game_redo.area()
            elif player_input == str(2):
                self.second_choice(player)


# game = Clue()
# game.start()
