# should this go in here?


class Player():
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.lives = 3
        self.items = []
        self.blanket_pieces = 0
        self.lastroom = ""


class Game():
    def back_story(self):
        print(f"You're babysitting the 3-year-old son of Inventor Lampton, whose Helicopter will revolutionize aviation. You are {self.name}, financial sponsor of the Helicopter, who will back anything—with his father's money. There is also Colonel Annesley, who wants the Helicopter for the U.S. Government.\n\n...but those people have absolutely nothing to do with this story. I just told you about them to make this intro a bit longer. :3\n\n")

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
            if shake_eight_ball = "Y"
                room = random.randint(1,6)
            else:
                print("WHAT! Take a chance! Shake the ball!")
                self.eight_ball_word()


    def death(self):
        print("You have died.")
        if "mushroom" in self.items:
            self.items.remove("mushroom")
            print("But what's this? You have the silver mushroom! The mushroom disappears from your hand and you find yourself back where you were.")
            self.room()
        if self.lives > 0:
            self.lives = self.lives - 1
            print("But what's this? It seems you have", self.lives, "more lives to give. Good luck!")
            self.room()
        if self.lives == 0:
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
