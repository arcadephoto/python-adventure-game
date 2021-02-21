
import random
from connect_four import connect_four

# from Hungry_Hungry_Hips import Hungry_hippos
# from Clue import Clue
# from simon import Simon

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
        self.health = 50
        # self.lives = 3
        self.items = []
        self.blanket_pieces = 0
        self.lastroom = ""
        self.rooms_completed = []

    def start_game(self, player):
        msg = '''
        THIS IS THE WELCOME SCREEN. It's the first thing the player sees.
        It will give a little back story, then ask the player's name,
        then launch the 8-Ball function.
        '''
        print(msg)
        self.eight_ball(player)

    def eight_ball(self, player):
        msg = '''
        This is the 8-ball function.
        We can definitely use Sarah's
        function. This is just a test.
        '''
        print(msg)
        i = random.randint(1, 5)
        if i == 1:
            if "connect" not in player.rooms_completed:
                print("Connect Four")
                connect_four.enter(player)
            else:
                self.eight_ball(player)
        if i == 2:
            print("Hippos")
            #hungry_hungry_hips.enter(player)
        if i == 3:
            print("Clue")
            #clue.enter(player)
        if i == 4:
            print("Snakes and Ladders")
            #snakes_and_ladders.enter(player)
        if i == 5:
            print("Simon")
            #simon.enter(player)


    def exit(self, player):
        msg = '''
    THIS IS WHERE YOU GO AFTER WINNING A GAME.
    It fires the 8 ball routine again, but this time the
    rooms_completed attribute should keep the player from
    going to the same game twice.
    Press any key to contiue.
    input()
    '''
        print(msg)
        self.eight_ball(player)



    def won_the_game(self, player):
        ##THIS IS WHERE THE END-GAME WILL GO. IT WILL BE TRIGGERED
        ##BY LEN(SELF.ROOMS_COMPLETED) == 5



    # class Game():




player = Player('Player from Game.py')
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
    # def eight_ball_word(self):
    #         print("""
    # What seems to be a doorless hallway is in front of you.
    # You walk down the hallway...approaching what seems to be
    # an eight ball...on a table?
    #
    #        ******
    #     ,dP9CGG8888@b,
    #   ,IP  _   Y88888@@b,
    #  dIi  (_)   G888898@b
    # dCII  (_)   G888888@@b
    # GCCIi     ,GG888888@@@
    # GGCCCCCCCGGG8888888@@@
    # GGGGCCCGGGG8888888@@@@
    # Y8GGGGGG8888888@@@@P
    #  `Y8888888@@@@@@@P'
    #     `@@@@@@@@@P'
    # ______________________
    #         """)
    #         # self.shake_ball()
    #
    # def shake_ball(self):
    #     shake_eight_ball = input("Would you like to shake the eight ball? Y/N ")
    #     if shake_eight_ball == "Y":
    #         room = random.randint(1,6)
    #     else:
    #         print("WHAT! Take a chance! Shake the ball!")
    #         self.eight_ball_word()
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
