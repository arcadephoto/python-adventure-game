import random
# import Game
# from Game import Player
#
# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.health = 10
#         self.lives = 3
#         self.items = []
#         self.blanket_pieces = 3



class Hungry_hippos():
    def __init__(self, player):
        self.hippo_damage = 2
        self.hippo_attack = 3
        self.pearls = 0
        self.hippo_pearls = 0
        self.enter(player)
        self.play(player)

    def enter(self, player):

        print(f"""
{player.name} open your eyes but you are surround by darkness... as you
try to take a step forward, you realize there is no floor in front of
you or on either sidxe of you. A loud CLICK! A spotlight is on
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

    def play(self, player):
        print('refiring play method')



        while self.pearls < 10 and self.hippo_pearls < 10:
            quit = input("Q to Quit. Anyother key to continiue : ")
            if quit == "Q":
                break
            else:
                self.player_input(player)

        if self.pearls >= 10:
            print("YOU HAVE WON!")
            self.pearls = 10
            print(r""" THE HIPPO BEAST IS IMPRESSED

                     .^.,*.
                    (   )  )
                   .~       "-._   _.-'-*'-*'-*'-*'-'-.--._
                 /'             `"'                        `.
               _/'                                           `.
          __,""    ʘ                                            ).--.
       .-'       `._.'                                          .--.\
      '                                                         )   \`:
     ;                                                          ;    "
    :                                                           )
    | 8                                                        ;
     =                  )                                     .
      \                .                                    .'
      ● `.            ~  \                                .-'
    O//     `-._ _ _ . '    `.          ._        _        |
    |                       |        /  `"-*--*' |       |
   / \                      |        |           |       :
 -------------------------------------------------------------------------------


            You have recived a golden pearl! """)
            print(f"{player.name}'s health is {player.health}")
            player.items.push("golden-pearl")
            self.chance_to_smooth_talk(player)
        elif self.hippo_pearls >= 10:
            print("YOU HAVE LOST!")
            player.health = player.health - (self.hippo_damage * 2)
            print(f"{player.name} you have {player.health}")
            choice = input("A. Play another round or B. Move forward in shame Type A or B: ").lower()
            if choice == 'b':
                self.chance_to_smooth_talk(player)
            elif choice == 'a':
                self.pearls = 0
                self.hippo_pearls = 0
                self.play(player)

    def player_input(self, player):
        player_action = input("""player _ what would you like to do?
        A. Jump
        B. Run away
        Please type A or B for your action: """).lower()
        if player_action == 'a':
            #depending on your strength this will work
            print("You jumped!")
            self.battle_hippo(player)
        else:
            print("You coward..jump...JUMP!")

    def battle_hippo(self, player):
        # if self.pearls < 9 and self.hippo_pearls < 9:
            #may want to give this a the player?
            p1_pearl = random.randint(1, 2)
            self.pearls =  self.pearls + p1_pearl
            hippo_pearl = random.randint(1, 9)
            self.hippo_pearls =  self.hippo_pearls + hippo_pearl
            print(f"Hippo now has {self.hippo_pearls}")
            print(f"You now have {self.pearls}")
        # elif self.pearls > 9:
        #     print("YOU HAVE WON!")
        #     self.pearls = 10
        # elif self.hippo_pearls > 9:
        #     print("YOU HAVE LOST!")
        #     choice = input("A. Play another round or B. Move forward in shame Type A or B: ")
        #     if choice == 'B' or 'b':
        #         self.chance_to_smooth_talk()
        #     elif choice == 'A' or 'a':
        #         self.pearls = 0
        #         self.hippo_pearls = 0
        #         self.play()
            #player.health - self.hippo_attack



    def chance_to_smooth_talk(self, player):
        print("You have a pearl in hand...")
        gold_pearl_choice = input("""What will you do with the pearl
                                    A. Chuck the pearl at hippo
                                    B. Pocket it for later
                                    Type A or B: """)
        if gold_pearl_choice == "A":
            self.pre_bossfight(player)
        else:
            print("Smart choice!")
            print("You see the a hallway on the other side of the room..Right when the Hippo steps into your view.")
            smooth_talk_choice = input("""Hippo is staring blankly at you...
            then ROARS SMALL HUMAN... best me at one more game and I shall give you the item
            you seek!
            A. Play a game with Hippo
            B. Try to compliment the Hippo
            C. Run for hallway
            Type A B or C""")
            if smooth_talk_choice == 'A':
                self.pre_bossfight(player)
            elif smooth_talk_choice == 'B':
                self.compliment_game(player)
            else:
                self.pre_bossfight(player)

    def compliment_game(self, player):
        print("You bat your eyelashes at the hippo and say...")
        print(r"""

    ／￣￣￣￣￣￣￣￣
　　 |　...so I bet your favorite music is HIP...HOP......
　　 ＼＿　 ＿＿＿＿＿＿
　　　　　　　∨　　　　　　　　　　　　
         O
        /|\
        / \ """)
        print(r"""


 ／￣￣￣￣￣￣￣￣
 |　...whAT? Did you say?
　 _＿＿＿＿＿＿
　　∨ ,_,
    (ʘ_ʘ) ----------_
   (_._._)           |~'
   `-----'           /
     `|__|~-----~|__|""")

        compliment_choice = input("The Hippo foruntley didn't hear you, what compliment would you like to say? ")
        if "nice" or "hip" in compliment_choice:
            print(r"""

       @_______ ,_,
       (       /ʘ"ʘ\
        ||--||(_____)
        '"  '"'-----'


                   ／￣￣￣￣￣￣￣￣
                   |　SMALL HUMAN...you amsume me!!
                   \_ ＿＿＿＿
               _.._  ∨
              (.--.)
       @______'\__/'
       (       /~~\.
        ||--||(.__.)
        '"  '" ~~~~

        You look an a piece of blanket appears in your left hand,
        a rainbow pearl appears in you right hand""")
        else:
            print("The rainbow pearl seems to be cracking...")
            # self.player get a piece of blanket.
            # ENTER HALLWAY TO TELEPORT OUT FUN
            #is this the messed up line
            print("""

                   ／￣￣￣￣￣￣￣￣
                   |　HOW DARE YOU!!!
                   \_ ＿＿＿＿
               _.._  ∨
              (.--.)
       @______'\__/'
       (       /~~\.
        ||--||(.__.)
        '"  '" ~~~~  """)
            self.pre_bossfight()



    def pre_bossfight(self, player):
        if "golden-pearl" in player.items:
            health_boost_choice = input("Would you like to use your golden pearl now? Y/N ")
            if health_boost_choice == "Y" or "Yes":
                print("Your health has been restored!")
                player.health = 10
                self.boss_fight(player)
            else:
                print(f"{player.name}'s health is at {player.health}")
                self.boss_fight(player)
        else:
            print(f"{player.name}'s health is at {player.health}")
            self.boss_fight(player)

    def boss_fight(self, player):
        print("YOU HAVE ANGER THE HUNGRY HIPPO NOW HE IS HANGRY!!!!!")
        print(r"""
  .-''''-. _
 ('    '  '0)-/)
 '..____..:    \._
   \u  u (        '-..------._
   |     /      :   '.        '--.
  .nn_nn/ (      :   '            '\
 ( '' '' /      ;     .             \
  ''----' "\          :            : '.
         .'/                           '.
  | |    / /                             '.
   |    /_|       )                     .\|
   ●     |      /\                     . '
         '--.__|  '--._  ,            /
                      /'-,          .'
 ?                   /   |        _.'
 O                   (____\       /
/|\                        \      \
/ \                         '-'-'-' """)
        print("""You must dodge the falling pearls!
        The pearls are falling in tile spaces 1-5..
        To successfully dodge the pearls you must be in the tile space the pearl does not fall on!""")
        falling_pearls = 10
        while falling_pearls != 0:
            # try:
            where_to_stand = int(input("Pick a tile 1-3 to dodge the falling pearl by typing 1, 2, or 3"))
            falling_pearl = random.randint(1,3)
            if where_to_stand == falling_pearl:
                print(r"""

 ● *BOnK
 O
/|\
/ \
                """)
                player.health = player.health - self.hippo_damage
                falling_pearls -= 1
            else:
                    print("""

  *DOgdE
 O   ____
/|\  _     ●
/ \  ____
                """)
                    falling_pearls -= 1
            # except ValueError:
            #         print("Try a number 1-5")
        if player.health > 1:
            print(r"""

                   ／￣￣￣￣￣￣￣￣
                   |　SMALL HUMAN...YOU BESTED ME!
                   | take these items...
                   \_ ＿＿＿＿
               _.._  ∨
              (.--.)
       @______'\__/'
       (       /~~\.
        ||--||(.__.)
        '"  '" ~~~~

        You look an a piece of blanket appears in your left hand.
        """)
            print(f"{player.name}'s health is {player.health}")
            player.blanket_pieces += 1
            player.rooms_completed = ['hippos'] + player.rooms_completed
            player.exit(player)

        else:
            print(f"{player.name}'s health is {player.health}")
            print("YOU DIED...but your task wasn't complete! Try  again")
            player.eight_ball(player)

            #do something if they die
#tame a hippo and busted thru a wall
