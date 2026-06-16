from graphics import *
import random
import time

class Die:
    def roll(self):
        return random.randint(1, 6)

class DiceCup:
    def __init__(self):
        self.dice = [Die(), Die(), Die(), Die(), Die()]

    def roll(self, number):
        rolls = []
        for i in range(number):
            rolls.append(self.dice[i].roll())
        return rolls

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0

class TextInterface:
    def show(self, message):
        print(message)

    def close(self):
        pass

class GraphicsInterface:
    def __init__(self):
        self.win = GraphWin("Ship Captain Crew", 500, 300)
        self.text = Text(Point(250, 150), "")
        self.text.draw(self.win)

    def show(self, message):
        self.text.setText(message)
        time.sleep(1)

    def close(self):
        self.win.getMouse()
        self.win.close()

class Game:
    def __init__(self, num_players, interface):
        self.players = []
        for i in range(num_players):
            self.players.append(Player("Player " + str(i + 1)))

        self.cup = DiceCup()
        self.interface = interface

    def take_turn(self, player):
        self.interface.show(player.name + " turn")

        has_ship = False
        has_captain = False
        has_crew = False
        dice_left = 5
        cargo_score = 0

        for roll_num in range(1, 4):
            rolls = self.cup.roll(dice_left)
            self.interface.show("Roll " + str(roll_num) + ": " + str(rolls))

            if has_ship == False and 6 in rolls:
                has_ship = True
                rolls.remove(6)
                dice_left = dice_left - 1

            if has_ship and has_captain == False and 5 in rolls:
                has_captain = True
                rolls.remove(5)
                dice_left = dice_left - 1

            if has_ship and has_captain and has_crew == False and 4 in rolls:
                has_crew = True
                rolls.remove(4)
                dice_left = dice_left - 1

            if has_ship and has_captain and has_crew:
                cargo_score = sum(rolls)
                dice_left = 2
                self.interface.show("Cargo score: " + str(cargo_score))

        if has_ship and has_captain and has_crew:
            player.score = cargo_score
        else:
            player.score = 0

    def play_game(self):
        for player in self.players:
            self.take_turn(player)

        scores = []
        for player in self.players:
            scores.append(player.score)

        high = max(scores)

        if scores.count(high) > 1:
            self.interface.show("Tie. Tied players play again.")
        else:
            winner = scores.index(high)
            self.interface.show(self.players[winner].name + " wins!")

        self.interface.close()

def main():
    num_players = int(input("Enter number of players: "))
    choice = input("Enter T for text or G for graphics: ")

    if choice.upper() == "G":
        interface = GraphicsInterface()
    else:
        interface = TextInterface()

    game = Game(num_players, interface)
    game.play_game()

main()
