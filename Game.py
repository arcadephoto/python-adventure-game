# should this go in here?
import random
from connect_four import Connect_four
from connect_four import Connect_room
from connect_four import Drop_game
from Hungry_Hungry_Hips import Hungry_hippos


connect = Connect_four()

class Player():
    def __init__(self, name):
        self.name = name
        self.health = 50
        # self.lives = 3
        self.items = []
        self.blanket_pieces = 0
        self.lastroom = ""
        self.rooms_completed = []

class Game():
    def __init__(self):
        self.player = Player('Bob')
        self.back_story()
        self.eight_ball_word()
        self.play()


    def death(self):
        print("You have died.")
        if "mushroom" in self.player.items:
            self.player.items.remove("mushroom")
            print("But what's this? You have the silver mushroom! The mushroom disappears from your hand and you find yourself back where you were.")
            self.room()
        if self.player.lives > 0:
            self.player.lives = self.player.lives - 1
            print("But what's this? It seems you have", self.player.lives, "more lives to give. Good luck!")
            self.room()
        if self.player.lives == 0:
            print("You have died and in real life, unlike video games, there are no do overs. Now press RETURN to do over!")
            print("game start command")

    def room(self):
        if self.lastroom == "connect":
            four.column_one()
        if self.lastroom == "hippo":
            print("hippo start")
        if self.lastroom == "simon":
            print("simon start")
        if self.lastroom == "clue":
            print("clue start")
        if self.lastroom == "ladders":
            print("ladders start")



































































    def back_story(self):
        print(f"You're babysitting the 3-year-old son of Inventor Lampton, whose Helicopter will revolutionize aviation. You are {self.player.name}, financial sponsor of the Helicopter, who will back anything—with his father's money. There is also Colonel Annesley, who wants the Helicopter for the U.S. Government.\n\n...but those people have absolutely nothing to do with this story. I just told you about them to make this intro a bit longer. :3\n\nYou are reading the child a bedtime story and suddenly you    get sucked into the book. In order to escape the book world, you must get 5 blanket pieces, which each exist in one respective room.\n\nAs you are now a fictional character, if you die in the book world, the universe will forever forget you and you will be erased from existence.")


    def play(self):
        while self.player.health > 0 or self.player.blanket_pieces == 5:
            print('playing game')
            room_choice = random.randint(1,2)
            if room_choice == 1:
                self.lastroom = "connect"
                connect.start(self.player)
                if not 'connect' in self.player.rooms_completed:
                    if self.player.health <= 0:
                        self.player.lastroom = "connect"
                        self.death()
                    else:
                        print("You're hurt but, amazingly,you're   still alive. If you everwant to return to  the real world,you should try the game again.")
                        drop_game.play_again(self.player)
        # if room_choice == 2:
        #     self.lastroom = "hippo"
        #     Hungry_hippos(self.player)
            elif room_choice == 2:
                self.lastroom = "hippo"
                Hungry_hippos(self.player)
            elif room_choice == 3:
                print("PATRICK")
                Hungry_hippos(self.player)
            elif room_choice == 4:
                print("BILLY")
                Hungry_hippos(self.player)
            else:
                print("GAVIN")
                Hungry_hippos(self.player)
        if self.player.health == 0:
            print("You have died.")
            death()
        elif self.player.blanket_pieces == 5:
            ending_story()
        # if room_choice == 3:
        #     #patrock room



    # def death(self):
    #     print("You have died.")
    #     if "mushroom" in self.player.items:
    #         self.player.items.remove("mushroom")
    #         print("But what's this? You have the silver mushroom! The mushroom disappears from your hand and you find yourself back where you were.")
    #         self.room()
    #     if self.player.health > 0:
    #         self.player.lives = self.player.lives - 1
    #         print("But what's this? It seems you have", self.player.lives, "more lives to give. Good luck!")
    #         self.room()
    #     if self.player.health == 0:
    #         print("You have died and in real life, unlike video games, there are no do overs. Now press RETURN to do over!")
    #         print("game start command")
    #
    # def room(self):
    #     if self.lastroom == "connect":
    #         connect.start(self.player)
    #     if self.lastroom == "hippo":
    #         hungry_hips.pre_bossfight()
    #     if self.lastroom == "simon":
    #         print("simon start")
    #     if self.lastroom == "clue":
    #         print("clue start")
    #     if self.lastroom == "ladders":
    #         print("ladders start")


    def ending_story(self):
        print("""As you come too.. you realize your sitting in a chair with a book in your hand. Comfort overcomes you as your realize you are in the
        bedroom of childs name. The child is at your side grabbing for what seems
        to be a blanket. You hand over the blanket.
        The child rubs their eyes and crawls back into bed. The child says, "Thank you
        for the wonderful adventure story".
        As the child tumbles into slumber... you begin to ask yourself about the
        past events... You swore that blanket was in 5 pieces... that you were never ..not in danger of death... yet....
        You hear a door open...YOU JUMP UP. Ready for a fight.. it's two human adults you recongize.
        They are rushing towards you with... with..with money in their hands. Thank youing for getting
        their child to sleep. Ushering you out the door and thank youing for a great
        job of babysitting.
        You look down at your hand with $75 in your hand and can only think of
        the money you have now.
        """)



    def eight_ball_word(self):
            print("""
    What seems to be a doorless hallway is in front of you.
    You walk down the hallway...approaching what seems to be
    an eight ball...on a table?

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
            self.shake_ball()

    def shake_ball(self):
        shake_eight_ball = input("Would you like to shake the eight ball? Y/N ")
        if shake_eight_ball == "Y":
            self.play()
        else:
            print("WHAT! Take a chance!... you fall foward... the ball rolls off the table..")
            self.play()





game = Game()
game.Game()



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
