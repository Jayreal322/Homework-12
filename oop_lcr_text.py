import random

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

class LCRGame:
    def __init__(self, num_players):
        self.players = []
        for i in range(num_players):
            self.players.append(Player("Player " + str(i + 1)))

        self.pot = Pot()
        self.die = Die()
        self.current = 0

    def active_players(self):
        count = 0
        for player in self.players:
            if player.chips > 0:
                count = count + 1
        return count

    def play_turn(self):
        player = self.players[self.current]
        print()
        print(player.name, "turn. Chips:", player.chips)

        dice_count = player.chips
        if dice_count > 3:
            dice_count = 3

        if dice_count == 0:
            print(player.name, "has no chips and skips.")
        else:
            for i in range(dice_count):
                roll = self.die.roll()
                print("Rolled:", roll)

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

    def show_status(self):
        for player in self.players:
            print(player.name, "chips:", player.chips)
        print("Center pot:", self.pot.chips)

    def play_game(self):
        while self.active_players() > 1:
            self.play_turn()
            self.show_status()

        for player in self.players:
            if player.chips > 0:
                print()
                print(player.name, "wins!")
                print("Center pot prize:", self.pot.chips)

def main():
    num_players = int(input("Enter number of players, 3 or more: "))
    game = LCRGame(num_players)
    game.play_game()

main()
