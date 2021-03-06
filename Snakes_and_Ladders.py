import random
# from Player import Player

class Snakes_and_ladders():

    def __init__(self, player):
        self.player1Pos = 1
        self.snakePos = 1
        self.dice_value = 0
        self.welcome_msg(player)




    def welcome_msg(self, player):
        msg = f"""
        Welcome to Snakes and Ladders.


        Rules:
          1. Both players begin at starting position.
             Take turns rolling the dice.
             Move forward the number of spaces shown on the dice.
          2. Some spaces will move you forward or backwards.
          3. If you land on the Snake Eye, he will take health from you.
          4. The first player to get to the FINAL position is the winner.

        """
        print(msg)

        self.playgame(player)

    def roll(self, player):
        min = 1
        max = 7
        return random.randint(min, max)


    def roll_the_dice(self, player):
        player_roll = input("press r to roll the dice or q to quit")
        if player_roll == "r":
            self.dice_value = self.roll(player)
            print(f"you rolled a {self.dice_value}")
        else:
            print("ok")
#             break
#1,20
#2,6,9,10,12,14,16 = safe
#3,5,8,11,15,18 = minus 1
#4 = plus 2
#7,13 plus 1
#9,19

    def snake_play(self, player):
        self.snakePos = self.snakePos + self.dice_value
        if self.snakePos == 2 or self.snakePos == 6 or self.snakePos == 7 or self.snakePos == 10 or self.snakePos == 12 or self.snakePos == 14 or self.snakePos == 16:
            print("snake is safe here... for now")
        elif self.snakePos == 3 or self.snakePos == 5 or self.snakePos == 8 or self.snakePos == 11 or self.snakePos == 15 or self.snakePos == 18:
            print("snake landed on a bad spot, they moved back 1!")
            self.snake_updated_position = self.snakePos - 1 # is this correct formating
        elif self.snakePos == 4:
            print("snake landed on the ladder, they moveded forward 2")
            self.snake_updated_position = self.snakePos + 2
        elif self.snakePos == 9 or self.snakePos == 19:
            print("snake landed on the ladder, they moveded forward 1")
            self.snake_updated_position = self.snakePos + 1
        elif self.snakePos == 17:
            print("snake jumped to the win space, try again loser")
            self.snake_updated_position = self.snakePos + 3
        elif self.snakePos == 20:
            print("snakey has won, try again")
        elif self.snakePos == 7 or self.snakePos == 13:
            print("the snake is safe on the Snakes Eye")
        else:
            print("snake is doing something!")



    def player_play(self, player):
        self.player1Pos = self.player1Pos + self.dice_value
        print(f"Bob postions is {self.player1Pos} and snake is at { self.snakePos} ")
        if self.player1Pos == 2 or self.player1Pos == 6 or self.player1Pos == 7 or self.player1Pos == 10 or self.player1Pos == 12 or self.player1Pos == 14 or self.player1Pos == 16:
            print("you are safe here... for now")
        elif self.player1Pos == 3 or self.player1Pos == 5 or self.player1Pos == 8 or self.player1Pos == 11 or self.player1Pos == 15 or self.player1Pos == 18:
            print("you are in a snakes spot... it bit you and you moved back 1!")
            self.updated_position = self.player1Pos - 1 # is this correct formating
        elif self.player1Pos == 4:
            print("you landed on a ladder, you have moved forward 2 spaces")
            self.updated_position = self.player1Pos + 2
        elif self.player1Pos == 9 or self.player1Pos == 19:
            print("you landed on a ladder, you have moved forward 1 space")
            self.updated_position = self.player1Pos + 1
        elif self.player1Pos == 17:
            print("you have landed on a special space and have been promoted to winner status")
            self.updated_position = self.player1Pos + 3
        elif self.player1Pos == 20:
            print("you have won the game against the snakey snake!!!congrats")
        elif self.player1Pos == 7 or self.player1Pos == 13:
            print("You have landed on the Snakes Eye, the snake has severely hurt you and you have taken damage to your health!")
        else:
            print("try to make it to the end before the snakey boy does!")

    def playgame(self, player):
        self.roll_the_dice(player)
        while self.player1Pos <= 20 or self.snakePos <= 20:
            self.player_play(player)
            print(f"you are at position {self.player1Pos}")
            self.snake_play(player)
            print(f"snake is at position {self.snakePos}")
            self.playgame(player)
            if self.player1Pos >= 20:
                print("YOU WIN!!!")
                player.blanket_pieces += 1
                player.rooms_completed = ['snakes'] + player.rooms_completed
                player.exit(player)
            elif self.snakePos >= 20:
                print("the snake has won, you couldnt make it there in time!")
                if input("Play again?") == "y":
                    self.player1Pos = 1
                    self.snakePos = 1
                    self.dice_value = 0
                    self.playgame(player)

# def playgame(self, player):
#     self.roll_the_dice(player)
#     if self.player1Pos < 20 and self.snakePos < 20:
#         self.player_play(player)
#         print(f"you are at position {self.player1Pos}")
#         self.snake_play(player)
#         print(f"snake is at position {self.snakePos}")
#         self.playgame(player)
#     elif self.player1Pos > 19:
#         print("YOU WIN!!!")
#         player.exit(player)
#         player.blanket_pieces += 1
#         player.rooms_completed = ['snakes'] + player.rooms_completed
#     elif self.snakePos > 19:
#         print("the snake has won, you couldnt make it there in time!")
#     if input("Play again?") == "y":
#         self.player1Pos = 1
#         self.snakePos = 1
#         self.dice_value = 0
#         self.playgame(player)



# snakes = Snakes_and_ladders(player)
# snakes.welcome_msg(player)
