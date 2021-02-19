import random

class Player():
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.lives = 3
        self.items = []
        self.blanket_pieces = 3

        def death(self):
            print("We need to some code for what happens if the character loses all three lives")



class Hungry_hippos():
    def __init__(self):
        self.hippo_attack = 3
        self.pearls = 0
        self.hippo_pearls = 0
        self.hippo_story()
        self.play()

    def hippo_story(self):
        print("""
You open your eyes but you are surround by darkness… as you
try to take a step forward, you realize there is no floor in front of
you or on either side of you. A loud CLICK! A spotlight is on
you! You look below you and you are on a black levers that seems
to be attached to a hot pink blob. Over a loud speaker you hear.
It's a race, it's a chase, hurry up and feed their face! Who will
win? No one knows! Feed the hungry hip-ip-pos! Hungry hungry
hippos! open up and there it goes!
CLICK CLICK CLICK The room lights up!
You find yourself standing on a the back of a
hot pink hungry hungry hippos!
Across the room you see a plastic lifeless hippo staring you
) ʘ   ʘ ( in your eyes.Even though it’s lifeless you understand it has a
hunger that can not be satisfied......
           ∩  ︵  ∩
          ) ʘ   ʘ (
         (  ●  ●   )
         ___________
         ╰━━━━━━━━━━╯
CLICK A waterfall of hippos pearls fall from the abyss above.
        |   |     |
        | |   |  ||
        |  |  |   |
        |'. .' .`.|
        |0oOO0oO0o|

As the pearls continue to fall you watch the
lime green hippo open its mouth fast and furious
to gobble up as much white balls as it can.
           ∩  ︵  ∩
          ) ʘ   ʘ (
         (__●__●___)
         \ U     U /
          )        (
         /__n_____n_\

        ╰━━━━━━━━━━━━╯
You remember fondly remember playing this game as a
child and it clicks in your head that the lever is
controlling your hippo.
""")


    def play(self):
        while self.pearls < 10:
            quit = input("Q to Quit. Anyother key to continiue : ")
            if quit == "Q":
                break
            else:
                self.player_input()

    def player_input(self):
        player_action = input("""Player1 _ what would you like to do?
        A. Jump
        B. Run away
        Please type A or B for your action: """)
        if player_action == 'A':
            #depending on your strength this will work
            print("You jumped!")
            self.battle_hippo()
        else:
            print("You coward..jump...JUMP!")

    def battle_hippo(self):
        if self.pearls < 9 and self.hippo_pearls < 9:
            #may want to give this a the player?
            p1_pearl = random.randint(1, 9)
            self.pearls =  self.pearls + p1_pearl
            hippo_pearl = random.randint(1, 3)
            self.hippo_pearls =  self.hippo_pearls + hippo_pearl
            print(f"Hippo now has {self.hippo_pearls}")
            print(f"You now have {self.pearls}")
        elif self.pearls > 9:
            print("YOU HAVE WON!")
            self.pearls = 10
        elif self.hippo_pearls < 9:
            print("YOU HAVE LOST!")
            #player.health - self.hippo_attack


Hungry_hippos()
#tame a hippo and busted thru a wall
#
