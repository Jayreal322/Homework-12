from graphics import *
import random
import time

class Die:
    def roll(self):
        return random.choice(["L", "C", "R", ".", ".", "."])

class Player:
    def __init__(self, name):
        self.name = name
        self.chips = 3

class Pot:
    def __init__(self):
        self.chips = 0

    def add(self):
        self.chips = self.chips + 1

class TextInterface:
    def show_message(self, message):
        print(message)

    def show_status(self, players, pot):
        for player in players:
            print(player.name, "chips:", player.chips)
        print("Center pot:", pot.chips)

    def pause(self):
        input("Press Enter to continue...")

    def close(self):
        pass

class GraphicsInterface:
    def __init__(self):
        self.win = GraphWin("LCR Game", 500, 400)
        self.message = Text(Point(250, 80), "")
        self.message.draw(self.win)
        self.status = Text(Point(250, 200), "")
        self.status.draw(self.win)

    def show_message(self, message):
        self.message.setText(message)
        time.sleep(1)

    def show_status(self, players, pot):
        text = ""
        for player in players:
            text = text + player.name + " chips: " + str(player.chips) + "\n"
        text = text + "Center pot: " + str(pot.chips)
        self.status.setText(text)
        time.sleep(1)

    def pause(self):
        self.win.getMouse()

    def close(self):
        self.win.close()

class LCRGame:
    def __init__(self, num_players, interface):
        self.players = []
        for i in range(num_players):
            self.players.append(Player("Player " + str(i + 1)))

        self.pot = Pot()
        self.die = Die()
        self.current = 0
        self.interface = interface

    def active_players(self):
        count = 0
        for player in self.players:
            if player.chips > 0:
                count = count + 1
        return count

    def play_turn(self):
        player = self.players[self.current]
        self.interface.show_message(player.name + " turn.")

        dice_count = player.chips
        if dice_count > 3:
            dice_count = 3

        if dice_count == 0:
            self.interface.show_message(player.name + " skips.")
        else:
            for i in range(dice_count):
                roll = self.die.roll()
                self.interface.show_message(player.name + " rolled " + roll)

                if roll == "L":
                    player.chips = player.chips - 1
                    left = (self.current - 1) % len(self.players)
                    self.players[left].chips = self.players[left].chips + 1

                elif roll == "R":
                    player.chips = player.chips - 1
                    right = (self.current + 1) % len(self.players)
                    self.players[right].chips = self.players[right].chips + 1

                elif roll == "C":
                    player.chips = player.chips - 1
                    self.pot.add()

        self.current = (self.current + 1) % len(self.players)

    def play_game(self):
        while self.active_players() > 1:
            self.play_turn()
            self.interface.show_status(self.players, self.pot)

        for player in self.players:
            if player.chips > 0:
                self.interface.show_message(player.name + " wins! Pot prize: " + str(self.pot.chips))

        self.interface.pause()
        self.interface.close()

def main():
    num_players = int(input("Enter number of players, 3 or more: "))
    choice = input("Enter T for text or G for graphics: ")

    if choice.upper() == "G":
        interface = GraphicsInterface()
    else:
        interface = TextInterface()

    game = LCRGame(num_players, interface)
    game.play_game()

main()
