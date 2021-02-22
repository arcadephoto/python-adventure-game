import random
from connect_four import Connect_four
from Hungry_Hungry_Hips import Hungry_hippos
from Clue import Clue
from simon import Simon
from Snakes_and_Ladders import Snakes_and_ladders
import sys

# =======
# from connect_four import Connect_four
# from Hungry_Hungry_Hips import Hungry_hippos
# from Clue import Clue
# from simon import Simon
# from Snakes_and_Ladders import Snakes_and_ladders
# >>>>>>> pulling saturdays update


class Player():
    def __init__(self, name):
        self.name = name
        self.health = 20
        # self.lives = 3
        self.items = []
        self.blanket_pieces = 0
        self.lastroom = ""
        self.babyname = "Windchester Jr. III"
        self.rooms_completed = []
#welcome to the game... whats the players name
#ending story
    def start_game(self, player):
        self.name = input("Welcome to the game, please type your name and then hit enter: ")
        msg = (f'''You're {self.name}, babysitting the 3-year-old {self.babyname} of Inventor
    Lampton, whose miniaturizaton ray will change the world.

    You are reading the child a bedtime story when you are suddenly
    miniaturized into the world of toys and games.
    In order to escape the toy world, you must win the games and collect
    your prizes: five pieces of a child's blanket.

    You feel yourself being pulled into a game...

    ''')
        print(msg)

        self.eight_ball(player)

    def eight_ball(self, player):
        while self.blanket_pieces != 5 and self.health != 0:
            i = random.randint(1, 5)
            if i == 1:
                if "connect" not in self.rooms_completed:
                    Connect_four(player)
                else:
                    self.eight_ball(player)
            elif i == 2:
                if "hippos" not in self.rooms_completed:
                    Hungry_hippos(player)
                else:
                    self.eight_ball(player)
            elif i == 3:
                if "clue" not in self.rooms_completed:
                    Clue(player)
                else:
                    self.eight_ball(player)
            elif i == 4:
                if "snakes" not in self.rooms_completed:
                    Snakes_and_ladders(player)
                else:
                    self.eight_ball(player)
            elif i == 5:
                if "simon" not in self.rooms_completed:
                    Simon(player)
                else:
                    self.eight_ball(player)
            elif len(self.room_choice) == 5:
                break
            if self.blanket_pieces >= 5:
                print("You have WON!")
                self.won_the_game(player)
                return
            elif self.health <= 0:
                print("""You have failed at your babysitting duty!
            Please continue your task to keep your job!
            """)
                game_over_choice = input("Press Q to quit the game or press any other key to continue your journey! ").lower()
                if game_over_choice == "q" or game_over_choice == "Q":
                    print(f"{self.babyname} will be without hisblanket forever.... Goodbye {self.name}...")
                else:
                    self.health = 50
                    self.room_choice = []
                    self.start_game(player)





    def exit(self, player):
        if self.blanket_pieces >= 5:
            print("You have WON!")
            self.won_the_game(player)
            return

        print("""

    What seems to be a doorless hallway is in front of you.
    You walk down the hallway...approaching what seems to be
    an eight ball on a table.

           ******
        ,dP9CGG8888@b,
      ,IP  _   Y88888@@b,
     dIi  (_)   G888898@b
    dCII  (_)   G888888@@b
    GCCIi     ,GG888888@@@
    GGCCCCCCCGGG8888888@@@
    GGGGCCCGGGG8888888@@@@
    Y8GGGGGG8888888@@@@P
     `Y8888888@@@@@@@P'
        `@@@@@@@@@P'
    ______________________
            """)
        self.shake_ball(player)

    def shake_ball(self, player):
        shake_eight_ball = input("Would you like to shake the eight ball? Y/N ")
        if shake_eight_ball == "Y" or shake_eight_ball == "y":
            self.eight_ball(player)
        else:
            print("WHAT! Take a chance! Shake the ball!")
            self.eight_ball(player)





    def won_the_game(self, player):
        msg = '''
        You have recovered the entire blanket, and now you can return
        to the real world. Thanks for playing!
        '''
        print(msg)
        sys.exit("Goodbye!")



    # class Game():




player = Player('Bob')
# game = Game()
player.start_game(player)











    # def back_story(self):
    #     print(f"You're babysitting the 3-year-old son of Inventor Lampton, whose Helicopter will revolutionize aviation. You are {self.player.name}, financial sponsor of the Helicopter, who will back anything—with his father's money. There is also Colonel Annesley, who wants the Helicopter for the U.S. Government.\n\n...but those people have absolutely nothing to do with this story. I just told you about them to make this intro a bit longer. :3\n\nYou are reading the child a bedtime story and suddenly you    get sucked into the book. In order to escape the book world, you must get 5 blanket pieces, which each exist in one respective room.\n\nAs you are now a fictional character, if you die in the book world, the universe will forever forget you and you will be erased from existence.")
    #
    #
    # def play(self):
    #     while self.player.health > 0 or self.player.blanket_pieces == 5:
    #         print('playing game')
    #         room_choice = random.randint(1,4)
    #
    #         if room_choice == 1:
    #             connect.start(self.player)
    #         elif room_choice == 2:
    #             Hungry_hippos(self.player)
    #         elif room_choice == 3:
    #             Clue()
    #         elif room_choice == 4:
    #             Simon(self.player)
    #         else:
    #             print("GAVIN")
    #             Hungry_hippos(self.player)
    #     if self.player.health == 0:
    #         print("You have died.")
    #         death()
    #     elif self.player.blanket_pieces == 5:
    #         ending_story()
    #     # if room_choice == 3:
    #     #     #patrock room
    #
    #
    #

    # #
    # # def room(self):
    # #     if self.lastroom == "connect":
    # #         connect.start(self.player)
    # #     if self.lastroom == "hippo":
    # #         hungry_hips.pre_bossfight()
    # #     if self.lastroom == "simon":
    # #         print("simon start")
    # #     if self.lastroom == "clue":
    # #         print("clue start")
    # #     if self.lastroom == "ladders":
    # #         print("ladders start")
    #
    #
    # def ending_story(self):
    #     print("""As you come too.. you realize your sitting in a chair with a book in your hand. Comfort overcomes you as your realize you are in the
    #     bedroom of childs name. The child is at your side grabbing for what seems
    #     to be a blanket. You hand over the blanket.
    #     The child rubs their eyes and crawls back into bed. The child says, "Thank you
    #     for the wonderful adventure story".
    #     As the child tumbles into slumber... you begin to ask yourself about the
    #     past events... You swore that blanket was in 5 pieces... that you were never ..not in danger of death... yet....
    #     You hear a door open...YOU JUMP UP. Ready for a fight.. it's two human adults you recongize.
    #     They are rushing towards you with... with..with money in their hands. Thank youing for getting
    #     their child to sleep. Ushering you out the door and thank youing for a great
    #     job of babysitting.
    #     You look down at your hand with $75 in your hand and can only think of
    #     the money you have now.
    #     """)
    #
    #
    #

    #
    #     if self.player.lastroom == "connect":
    #         connect.start(self.player)
    #
    #     print('''You din't lose the connect ''')
    #     # if self.lastroom == "hippo":
    #     #     print("hippo start")
    #     # if self.lastroom == "simon":
    #     #     print("simon start")
    #     # if self.lastroom == "clue":
    #     #     print("clue start")
    #     # if self.lastroom == "ladders":
    #     #     print("ladders start")
    #
    #
    # def shake_ball(self):
    #     shake_eight_ball = input("Would you like to shake the eight ball? Y/N ")
    #     if shake_eight_ball == "Y":
    #         self.play()
    #     else:
    #         print("WHAT! Take a chance!... you fall foward... the ball rolls off the table..")
    #         self.play()




# game = Game()




    # def ending_story(self):
    #     print("""As you come too.. you realize your sitting in a chair with a book in your hand. Comfort overcomes you as your realize you are in the
    #     bedroom of childs name. The child is at your side grabbing for what seems
    #     to be a blanket. You hand over the blanket.
    #     The child rubs their eyes and crawls back into bed. The child says, "Thank you
    #     for the wonderful adventure story".
    #     As the child tumbles into slumber... you begin to ask yourself about the
    #     past events... You swore that blanket was in 5 pieces... that you were never ..not in danger of death... yet....
    #     You hear a door open...YOU JUMP UP. Ready for a fight.. it's two human adults you recongize.
    #     They are rushing towards you with... with..with money in their hands. Thank youing for getting
    #     their child to sleep. Ushering you out the door and thank youing for a great
    #     job of babysitting.
    #     You look down at your hand with $75 in your hand and can only think of
    #     the money you have now.
    #     """)
# Game()
