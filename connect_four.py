import random

# class Player():
#     def __init__(self, name):
#         self.name = name
#         self.health = 10
#         self.lives = 3
#         self.items = []
#         self.blanket_pieces = 0
#         self.lastroom = ""
#         self.rooms_completed = []

# player = Player("Bob")


class Connect_four():


    def __init__(self, player):
        self.row1 = [".", "_", "_", "_", "_", "_"]
        self.row2 = [".", "_", "_", "_", "_", "_"]
        self.row3 = [".", "_", "_", "_", "_", "_"]
        self.game_over = False
        self.blocked = ["_", "_", "_", "_", "_"]
        self.wins = 0
        self.enter(player)

    def enter(self, player):

        msg = (f'''

You're in a spotlight - a white pillar reaching into endless darkness.
Your breath ices in the freezing air. Motes of dust swirl then come
to rest on the ground next to a splotch of crusty dried viscera.

It's the remains of a ead, crushed, minced, pureed, pulverized, and
otherwise formerly living mincemeat pie of once-hopeful game player.

Let's hope you make better choices, {player.name}.

        ''')
        print(msg)
        self.connect_four(player)
        #input continue here


    def connect_four(self, player):
        msg = """
Ahead of you looms El Quatro, a soaring stone tower with four vertical
channels.

In three of the channels, a massive stone disc has fallen and crushed
the earth at the base of the tower. In the fourth channel stands a pedestal
with your name on it.

A voice booms from the darkness, 'Step up to your trial!'
              """
        print(msg)
        self.column_one(player)


    def column_one(self, player):
        msg = """
A voice booms from the darkness, 'This is the Trial of Stone! I'd say good
luck, but I wouldn't mean it.'

You approach the pedestal. It's a gray, cold stone and is oddly cracked and
chipped, as if it's been smashed to bits and glued back together dozens of
times before.
Sitting on the pedestal is a simple wooden frame and a small pile of stone
discs. Next to the frame is a tattered piece of paper.

The paper reads: 'THESE ARE THE RULES'

    - 'Your goal is to place three stones on top of each other in a
        single column. The enemy will try to block you.''
    - 'You may not play on an X. If you reach the top, you win. If
        you run out of moves, you lose.'
    - 'Diagonals mean nothing. This isn't tic-tac-toe.''")
    - 'Good luck. Hopefully this game doesn't crush your spirits.'

Ominously, the huge stone boulder swings high over your head.

You pick up a stone, and the game begins.

                """
        print(msg)
        self.activate_drop(player)





    def drop(self, slot, player):
        if self.game_over == False:
            if self.row3[slot] == "_":
                self.row3[slot] = "O"
            elif self.row2[slot] == "_":
                if self.row3[slot] == "X":
                    print("This column has been blocked. Please choose again.")
                    self.activate_drop(player)
                else:
                    self.row2[slot] = "O"
            elif self.row1[slot] == "_":
                if self.row2[slot] == "X" or self.row1[slot] == "X":
                    print("This column has been blocked. Please choose again.")
                    self.activate_drop(player)
                else:
                    self.row1[slot] = "O"
                    print("You reached the top! You won!")
                    self.win_game(player)
                    self.game_over = True
                    return
            else:
                print("That row is full. Please choose another")
                self.activate_drop(player)
            print(*self.row1, sep=" ")
            print(*self.row2, sep=" ")
            print(*self.row3, sep=" ")
            print("\n")
            print("The voice booms, 'And now it's my turn!")
            self.computer_turn(player)

    def activate_drop(self, player):
        print(*self.row1, sep=" ")
        print(*self.row2, sep=" ")
        print(*self.row3, sep=" ")
        if self.blocked == ["X", "X", "X", "X", "X"]:
            print("All ways up are blocked. The horrible enemy is victorious!")
            self.lost_game(player)
            return;
        i = input("Pick a column, 1-5:   ")
        if i in (["1", "2", "3", "4", "5"]):
            self.drop(int(i), player)
        else:
            print("Close, but try again.")
            self.activate_drop(player)

    def win_game(self, player):
        self.wins = self.wins + 1
        if self.wins < 2:
            print("The booming invisible voice echoes through the cavern: 'WHAT? Well, uh, best two out of three.'")
            print("It quickly adds, 'For you. If I win I win.'")
            self.play_again(player)
        elif self.wins == 2:
            self.game_over = True
            msg = '''

    The booming invisible voice echoes through the cavern: 'You have
    triumphed! Now take your prize and scram!'

    Before you, the pedestals and stones and blood and crushed remains of
    previous competitors fade away, leaving behind a simple wooden table atop
    which sits the tattered shard of a child's blanket.
    You take the shard in your hand. It's soft and warm and smells faintly
    of Saturday morning cartoons and fabric softener.
    The world fades away around you...
            '''
            print(msg)
            player.blanket_pieces += 1
            player.rooms_completed = ['connect'] + player.rooms_completed
            player.exit(player)



    def computer_turn(self, player):
        if self.game_over == False:
            i = random.randint(1, 5)
            print("The mysterious foe has chosen Column", i,".")
            print("A stone materializes in the air and drops into the game board")
            if self.blocked[int(i-1)] == "_":
                self.blocked[int(i-1)] = "X"
            self.computer_drop(int(i), player)

    def computer_drop(self, slot, player):
        if self.game_over == False:
            if self.row3[slot] == "_":
                self.row3[slot] = "X"
            elif self.row2[slot] == "_":
                self.row2[slot] = "X"
                if self.row2 == [".", "X", "X", "X", "X", "X"]:
                    print("Oh no! The cruel enemy has blocked all your moves. You lost!")
                    self.game_over = True
                    self.lost_game(player)
                    return
            elif self.row1[slot] == "_":
                self.row1[slot] = "X"
                print("Your foe has blocked column", slot, "!")
                if self.row2 == [".", "X", "X", "X", "X", "X"]:
                    print("Oh no! The cruel enemy has blocked all your moves. You lost!")
                    self.game_over = True
                    self.lost_game(player)
                    return
            else:
                print("That row was occupied, so the enemy chooses again. What a jerk!")
                self.computer_turn(player)
            if random.randint(1,3) == 3:
                print("Your opponent takes a free turn. What a cheater!")
                self.computer_turn(player)
            if self.game_over == False:
                print("\n")
                print("Your mysterious foe has played, and now it's your turn")
                self.activate_drop(player)

    def lost_game(self, player):
        dmg = random.randint(1, 3)
        print("\n")
        msg = (f'''
    The massive stone plummets overhead. It strikes you, dealing
    {dmg} points of damage!
        ''')
        print(msg)
        player.health = player.health - dmg
        if player.health <= 0:
            msg = '''
    You died! But this is a video game, and you still haven't finished
    your task, so try it again.
            '''
            print(msg)
            self.play_again(player)
        else:
            msg = '''
    You're hurt but, amazingly, you're still alive. If you ever
    want to return to the real world, you should try the game again.
            '''
            print(msg)
            self.play_again(player)
        return

    def play_again(self, player):
        self.game_over = False
        self.row1 = [".", "_", "_", "_", "_", "_"]
        self.row2 = [".", "_", "_", "_", "_", "_"]
        self.row3 = [".", "_", "_", "_", "_", "_"]
        self.blocked = ["_", "_", "_", "_", "_"]
        self.activate_drop(player)

# connect = Connect_four(player)
# connect.enter(player)
