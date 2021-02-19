from random import randrange


class Clue:
    def __init__(self):
        self.suspects = ["Patrick",
                         "Chad",
                         "Sarah",
                         "Gavin",
                         "Billy"]

        self.suspect = self.suspects[randrange(1, 5)]
        self.murderer = self.suspects[randrange(1, 5)]
        self.guesses = 3
        self.guess = []

    def backstory(self):
        print(f"""
You hear a door close behind you as you open your eyes.
You are in a room with 5 people. 
It looks like they are having a party.
What do you do?
              """)

    def first_choice(self):
        print("The front door refuses to open, "
              "and you wind up in the party room again.")
        player_input = input("1. Leave the house \n2. Join the party\n")

    def second_choice(self):
        self.second_choice_text()
        player_input = input("1. Leave for another room.\n2. Roll the die\n")

        self.guess_the_suspect(player_input)

    def second_choice_text(self):
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

    def guess_the_suspect(self, player_input):
        while self.guesses > 0:
            if player_input == "1":
                self.game_over()
            elif player_input == "2":
                self.show_suspects()
            if self.suspect == self.murderer:
                self.victory()

    def victory(self):
        print("Good job! You got the murderer, "
              "call the cops right away!")

    def show_suspects(self):
        self.guesses -= 1
        self.suspect = self.suspects[randrange(1, 5)]
        print(f"{self.guesses}", f"{self.suspect}", f"{self.murderer}")

    def game_over(self):
        self.guesses = 0
        print("Turns out the murderer was hanging out here, "
              "and decided to hit you in the head, and run away.")
        return

    def area(self):
        player_input = input("1. Leave the house.\n2. Join the party\n")

        while self.guesses > 0:
            if player_input == str(1):
                self.first_choice()
            elif player_input == str(2):
                self.second_choice()


game = Clue()

game.backstory()

game.area()
