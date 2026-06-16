import random

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

class ShipCaptainCrewGame:
    def __init__(self, num_players):
        self.players = []
        for i in range(num_players):
            self.players.append(Player("Player " + str(i + 1)))

        self.cup = DiceCup()

    def take_turn(self, player):
        print()
        print(player.name, "turn")

        has_ship = False
        has_captain = False
        has_crew = False
        dice_left = 5
        cargo_score = 0

        for roll_num in range(1, 4):
            rolls = self.cup.roll(dice_left)
            print("Roll", roll_num, rolls)

            if has_ship == False and 6 in rolls:
                has_ship = True
                rolls.remove(6)
                dice_left = dice_left - 1
                print("Ship found!")

            if has_ship and has_captain == False and 5 in rolls:
                has_captain = True
                rolls.remove(5)
                dice_left = dice_left - 1
                print("Captain found!")

            if has_ship and has_captain and has_crew == False and 4 in rolls:
                has_crew = True
                rolls.remove(4)
                dice_left = dice_left - 1
                print("Crew found!")

            if has_ship and has_captain and has_crew:
                cargo_score = sum(rolls)
                dice_left = 2
                print("Cargo score:", cargo_score)

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
            print(player.name, "score:", player.score)

        high = max(scores)

        if scores.count(high) > 1:
            print("Tie. Tied players should play again.")
        else:
            winner = scores.index(high)
            print(self.players[winner].name, "wins!")

def main():
    num_players = int(input("Enter number of players: "))
    game = ShipCaptainCrewGame(num_players)
    game.play_game()

main()
