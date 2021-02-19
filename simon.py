import time
import random
# from Game import Player
# from connect_four import Player

# player = Player("Bob")

class Simon():
    def __init__(self, player):
        self.player = player
        player.health = 10
        print("You have stumbled across an insane evil scientist named Dr. Heinz Longnameovich, who is bent on understanding the workings of the human mind. He has kidnapped you so that he can undertake a psychological experiment on you. The scientist is hoping to find someone with the ability to get through 5 rounds of Simon without guessing something wrong, because such an individual would have the rare condition known as 'scolactomemorandizitis'. He ties you to a chair and makes you play the game, and if you win, you will get something very special. If you get a wrong answer, he shocks you with his machine and that takes away 2 player.health. If you lose though, he kills you.\n\nDr. Longnameovich: Okay, here's how to play. Memorize each number I spurt out at you, and repeat them back to me, in order.\n")

        start_game = input("Dr. Longnameovich: Press any button to begin. ")

        difficulty = 0
        lost = False
        while 1:
            repeat = False
            if difficulty == 5:
                break
            else:
                if not lost:
                    difficulty += 1
                else:
                    lost = False
                list_of_numbers = []
                for enter in range(5000):
                    print("\n")
                for index in range(difficulty):
                    random_number = random.randint(1, 4)
                    list_of_numbers.append(random_number)
                    print(f"                              {random_number}")
                    time.sleep(2)
                    for enter in range(5000):
                        print("\n")
                for number in range(len(list_of_numbers)):
                    prompt = input(f"Dr. Longnameovich: Please repeat each number back to me. ")
                    if int(prompt) == list_of_numbers[number]:
                        print("Dr. Longnameovich: Hmmm, very good!")
                        time.sleep(2)
                    else:
                        print("Dr. Longnameovich: Why, you got one wrong. BZZZZZRRRTTT!!")
                        time.sleep(2)
                        lost = True
                        player.health -= 1
                        if player.health <= 0:
                            print("You died resulting from electric shock.")
                            exit()
                        else:
                            repeat = True
                            break
                if repeat == True:
                    continue
                else:
                    list_of_numbers.clear()
        print("Dr. Longnameovich: Ah! I'm astounded! You actually won! Well, then, indeed I have learned a lot about the condition of scolactomemorandizitis. Here, I will give you this blanket piece. You may now be on your way!\n\n(Oh by the way, due to your condition and your age, you have 3 days left to live. Just a heads up...)")
        player.blanket_pieces += 1

# simon = Simon()
