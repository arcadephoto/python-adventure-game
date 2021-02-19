import random

class Game():
    def __init__(self):
        self.row1 = [".", "_", "_", "_"]
        self.row2 = [".", "_", "_", "_"]
        self.row3 = [".", "_", "_", "_"]
        self.game_over = False


    def drop(self, slot):
        if self.game_over == False:
            if self.row3[slot] == "_":
                self.row3[slot] = "O"
            elif self.row2[slot] == "_":
                if self.row3[slot] == "X":
                    print("This column has been blocked. Please choose again.")
                    self.activate_drop()
                else:
                    self.row2[slot] = "O"
            elif self.row1[slot] == "_":
                if self.row2[slot] == "X" or self.row1[slot] == "X":
                    print("This column has been blocked. Please choose again.")
                    self.activate_drop()
                else:
                    self.row1[slot] = "O"
                    print("You reached the top! You won!")
                    self.win_game()
                    self.game_over = True
                    return
            else:
                print("That row is full. The game is over")
                return
            print(*self.row1, sep=" ")
            print(*self.row2, sep=" ")
            print(*self.row3, sep=" ")
            print("\n")
            print("The voice booms, 'And now it's my turn!")
            self.computer_turn()

    def activate_drop(self):
        print(*self.row1, sep=" ")
        print(*self.row2, sep=" ")
        print(*self.row3, sep=" ")
        i = input("Pick a column, 1-3")
        self.drop(int(i))

    def win_game(self):
        print("This activates when the player wins")
        if input("Play again?") == "y":
            self.play_again()


    def computer_turn(self):
        i = random.randint(1, 3)
        print("The mysterious foe has chosen Column", i,".")
        print("A stone materializes in the air and drops into the game board")
        self.computer_drop(int(i))

    def computer_drop(self, slot):
        if self.game_over == False:
            if self.row3[slot] == "_":
                self.row3[slot] = "X"
            elif self.row2[slot] == "_":
                self.row2[slot] = "X"
                if self.row2 == [".", "X", "X", "X"]:
                    print("Oh no! The cruel enemy has blocked all your moves. You lost!")
                    self.game_over = True
                    self.lost_game()
                    return
            elif self.row1[slot] == "_":
                self.row1[slot] = "X"
                print("Your foe has blocked column", slot, "!")
                if self.row2 == [".", "X", "X", "X"]:
                    print("Oh no! The cruel enemy has blocked all your moves. You lost!")
                    self.game_over = True
                    self.lost_game()
                    return
            else:
                print("The foe has chosen an unplayable row. Make your move!")
#             print(*self.row1, sep=" ")
#             print(*self.row2, sep=" ")
#             print(*self.row3, sep=" ")
            print("\n")
            print("Your mysterious foe has played, and now it's your turn")
            self.activate_drop()

    def lost_game(self):
        print("This is the sequence for losing the game")

    def play_again(self):
        self.row1 = [".", "_", "_", "_"]
        self.row2 = [".", "_", "_", "_"]
        self.row3 = [".", "_", "_", "_"]
        self.activate_drop()


game=Game()
game.activate_drop()
