import random
# from game import player

class Player:
    def __init__(self):
        self.player1Pos = 1
        self.snakePos = 1
        self.updated_postion = 0

#     def update_position(self, inPos):
#         self.playerPos = inPos

# updated_postion = 5
    def getPosition(self):
        return self.player_pos

class snakes_and_ladders():

    def __init__(self):
        self.player1Pos = 1
        self.snakePos = 1
        self.play()

    def welcome_msg(self):
        msg = """
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

    def roll(self):
        min = 1
        max = 7
        return random.randint(min, max)


    def roll_the_dice(self):
        player_roll = input("press r to roll the dice or q to quit")
        if player_roll == "r":
            self.dice_value = self.roll()
            print("you rolled a {dice_value}")
        else:
            print("ok")
#             break
#1,20
#2,6,9,10,12,14,16 = safe
#3,5,8,11,15,18 = minus 1
#4 = plus 2
#7,13 plus 1
#9,19

    def player_play(self):
        self.welcome_msg()
        self.player1Pos = self.roll()
        self.snakePos = self.roll()
        print(f"Bob postions is {self.player1Pos} and snake is at { self.snakePos} ")
        if player1Pos == 2 and player1Pos == 6 and player1Pos == 7 and player1Pos == 10 and player1Pos == 12 and player1Pos == 14 and player1Pos == 16:
            print("you are safe here... for now")
        elif player1Pos == 3 and player1Pos == 5 and player1Pos == 8 and player1Pos == 11 and player1Pos == 15 and player1Pos == 18:
            print("you are in a snakes spot... it bit you and you moved back 1!")
            self.updated_position = self.player1Pos - 1 # is this correct formating
        elif player1Pos == 4:
            print("you landed on a ladder, you have moved forward 2 spaces")
            self.updated_position = self.player1Pos + 2
        elif player1Pos == 9 and player1Pos == 19:
            print("you landed on a ladder, you have moved forward 1 space")
            self.updated_position = self.player1Pos + 1
        elif player1Pos == 17:
            print("you have landed on a special space and have been promoted to winner status")
            self.updated_position = self.player1Pos + 3
        elif player1Pos == 20:
            print("you have won the game against the snakey snake!!!congrats")
        elif player1Pos == 7 and player1Pos == 13:
            print("You have landed on the Snakes Eye, the snake has severely hurt you and you have taken damage to your health!")

        else:
            print("try to make it to the end before the snakey boy does!")

    def playgame(self):
        while self.player1Pos < 20 or self.snakePos < 20:
            self.player_play()
            print(f"you are at position {self.player1Pos}"")
            self.snake_play()
            print(f"snake is at position {self.snakePos}")
        if player1
            #do this
        elif #snake wins:
            #do this



#         if player1Pos == 2 and player1Pos == 4 and player1Pos == 6:
#             print("Your safe!")
#         if player1Pos == 3:
#             print("snake got ya")
#             player1.health = player1.health - self.snake_dam
#         else:
#             player1Pos =


snakes_and_ladders.self.welcome_msg()
snakes_and_ladders.roll_the_dice()
