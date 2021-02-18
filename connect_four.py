import random
# import game

class Player():
    def __init__(self, name):
        self.name = name
        self.health = 10
        self.lives = 3
        self.items = []
        self.blanket_pieces = 3

        def death(self):
            print("We need to some code for what happens if the character loses all three lives")


class Connect_four():
    def __init__(self):
        pieces_in_play = 0

    def connect_four(self):
        print("Ahead of you looms El Quatro, a stone structure reaching high into the darkness. It's a soaring tower with four parallel vertical channels.")
        print("A voice booms from the darkness, 'Choose! Choose the first of your four trials!'")
        print("\n")
        choice = input("You will face four trials. Choose the first.")
        if choice == "1":
            print("Taking a deep breath, you step under the first channel. A hundred-ton stone disc hangs high overhead, just waiting for you to screw up.")
            self.column_one()
        if choice == "2":
            print ("Second trial")
        if choice == "3":
            print ("Third trial")
        if choice == "4":
            print ("Fourth trial")
        else:
            print("Choose 1-4. Don't be a wise-ass.")
            self.connect_four()

    def column_one(self):
        print("\nA voice booms from the darkness, 'This is the Trial of Stone! I'd say good luck, but I wouldn't mean it.'")




player1 = Player('Bob')
four = Connect_four()

class connect_room():

    print('''Darkness.\nSilence. \nYou are alone. And then light. You're in a spotlight - a white pillar reaching
    up into the unfathomable darkness. Your breath ices in the freezing air. Motes of dust swirl in the light, drifting,
    then come to rest on the ground next to a suspicious splotch of crusty dried ooze. The once-gray floor is stained the color of rust. And the air smells of, um, fear?
    Death? Despair? No, the air smells like dead adventurer! Dead, crushed, minced, pureed, pulverized,
    and otherwise formerly living mincemeat pie of once-hopeful game player.
    Let's hope you make better choices,''', player1.name,".")
    print('''

    ''')

    def star_msg():
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
    star_msg()
