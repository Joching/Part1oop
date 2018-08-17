from player import Player
import random


class Cloud(Player):
    def run_play(self):
        play = random.choice(Player.playbook)
        if play == 'Camp':
            print("Cloud: I don't know that play... ")
        else:
            print (f"Cloud: I'll {play}")

class Zss(Player):
    def run_play(self):
        play = random.choice(Player.playbook)
        if play == 'Camp':
            print("Zss: I don't know that play... ")
        else:
            print (f"Zss: I'll {play}")

class Bayonetta(Player):
    def run_play(self):
        play = random.choice(Player.playbook)
        if play == 'Space':
            print("Bayonetta: I don't know that play... ")
        else:
            print (f"Bayonetta: I'll {play}")

class Diddy(Player):
    def run_play(self):
        play = random.choice(Player.playbook)
        if play == 'Camp' or 'Spam':
            print("Diddy: I don't know that play... ")
        else:
            print (f"Diddy: I'll {play}")

class Jiggly_puff(Player):
    def run_play(self):
        print (f"Jiggly puff: I don't know that play...")


