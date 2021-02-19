import random
import textwrap
# import game

class Player():
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.lives = 3
        self.items = []
        self.blanket_pieces = 3
        self.lastroom = ""

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
            four.connect_four()
        if self.lastroom == "hippo":
            print("hippo start")
        if self.lastroom == "simon":
            print("simon start")
        if self.lastroom == "clue":
            print("clue start")
        if self.lastroom == "ladders":
            print("ladders start")






class Connect_four():
    def __init__(self):
        pieces_in_play = 0

    def connect_four(self):
        print("Ahead of you looms El Quatro, a stone structure reaching high into the darkness. It's a soaring tower with four parallel vertical channels.")
        print('''In three of the channels, a massive stone disc has fallen and crushed the earth at the base of the tower. In the fourth channel stands
        a pedestal with your name on it. Heh heh heh.''')
        print("A voice booms from the darkness, 'Step up to your trial!'")
        self.column_one()


    def column_one(self):
        print("\nA voice booms from the darkness, 'This is the Trial of Stone! I'd say good luck, but I wouldn't mean it.'")
        print()
        print(f'''You approach the pedestal. It's a gray, cold stone and is oddly cracked and chipped,
        as if it's been smashed to bits and glued back together dozens of times before.''')
        print("Sitting on the pedestal is a simple wooden frame and a small pile of stone discs. Next to the frame is a tattered piece of paper.")
        print("The paper reads: 'THESE ARE THE RULES'")
        print("'Your goal is to place three stones on top of each other in a single column. The enemy will try to block you.''")
        print("'You may not play on an X. If you reach the top, you win. If you run out of moves, you lose.''")
        print("'Diagonals mean nothing. This isn't tic-tac-toe.''")
        print("'Good luck. Hopefully this game doesn't crush your spirits.''")
        print()
        print("Ominously, the huge stone boulder swings high over your head.")
        print("You pick up a stone, and the game begins.")
        drop_game.activate_drop()






class Connect_room():

    def start(self):
        print(f'''
        Darkness.\nSilence. \nYou are alone. And then light. You're in a spotlight - a white pillar reaching
        up into the unfathomable darkness. Your breath ices in the freezing air. Motes of dust swirl in the light, drifting,
        then come to rest on the ground next to a suspicious splotch of crusty dried ooze. The once-gray floor is stained the color of rust. And the air smells of, um, fear?
        Death? Despair? No, the air smells like dead adventurer! Dead, crushed, minced, pureed, pulverized,
        and otherwise formerly living mincemeat pie of once-hopeful game player.
        Let's hope you make better choices, {player1.name}.
        ''')
        print('''

        ''')
        self.star_msg()

    def star_msg(self):
        print('''In the puddle of dried goo you spot a silvery glint. Would you like to investigate?''')
        if (input("Investigate? ") == "y"):
            print("It's a toy tin mushroom! You pick it up and put it in your pocket")
            player1.items.insert(0, "mushroom")
            print("You have added the MUSHROOM BADGE.")
#             print(player1.items)
            four.connect_four()
        else:
            print("Just select Y, wise-ass.")
            star_msg()




class Drop_game():
    def __init__(self):
        self.row1 = [".", "_", "_", "_"]
        self.row2 = [".", "_", "_", "_"]
        self.row3 = [".", "_", "_", "_"]
        self.game_over = False
        self.blocked = ["_", "_", "_"]
        self.wins = 0


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
        if self.blocked == ["X", "X", "X"]:
            print("All ways up are blocked. The horrible enemy is victorious!")
            self.lost_game()
            return;
        i = input("Pick a column, 1-3:   ")
        self.drop(int(i))

    def win_game(self):
        self.wins = self.wins + 1
        if self.wins < 2:
            print("The booming invisible voice echoes through the cavern: 'WHAT? Well, uh, best two out of three.'")
            print("It quickly adds, 'For you. If I win I win.'")
            self.play_again()
        elif self.wins == 2:
            print("The booming invisible voice echoes through the cavern: 'You have triumphed! Now take your prize and scram!'")
            print("Before you, the pedestals and stones and blood and crushed remains of previous competitors fade away, leaving behind a simple wooden table atop which sits a silver locket.")
            print("You take the locket in hand. It feels solid and well-made. You press its latch, and it opens easily.")
            print("The world fades away around you...")
            print("HERE IS THE FUNCTION TO TAKE THE PLAYER BACK TO THE HALLWAY")

        # if input("Play again?") == "y":
        #     self.play_again()


    def computer_turn(self):
        i = random.randint(1, 3)
        print("The mysterious foe has chosen Column", i,".")
        print("A stone materializes in the air and drops into the game board")
        if self.blocked[int(i-1)] == "_":
            self.blocked[int(i-1)] = "X"
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
        dmg = random.randint(6, 12)
        print("\n")
        print("The massive stone plummets overhead. It strikes you, dealing", dmg, "points of damage!")
        player1.health = player1.health - 10
        if player1.health <= 0:
            player1.death()
            player1.lastroom = "connect"
        else:
            print("You're hurt but, amazingly, you're still alive. If you ever want to return to the real world, you should try the game again.")
            self.play_again()

    def play_again(self):
        self.row1 = [".", "_", "_", "_"]
        self.row2 = [".", "_", "_", "_"]
        self.row3 = [".", "_", "_", "_"]
        self.blocked = ["_", "_", "_"]
        self.activate_drop()


player1 = Player('Bob')
four = Connect_four()
drop_game = Drop_game()
connect = Connect_room()
# connect.start()
player1.lastroom = "connect"
player1.death()
