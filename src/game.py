from board import Board
from dice import Dice
from player import Player


class Game:
    def __init__(self):
        self.players = []
        self.board = Board()
        self.dice = Dice()

    def play(self):
        self.add_players()
        while True:
            for player in self.players:
                self.take_turn(player)
                if self.board.is_winner(player):
                    print(f"{player.name} Wins!!")
                    return

    def add_players(self):
        while True:
            if name := input("Add player: "):
                if self.is_duplicate_player(name):
                    print(f"{name}: already existing player")
                else:
                    player = Player(name)
                    self.players.append(player)
                    print(f"Players: {', '.join(p.name for p in self.players)}")
            else:
                break

    def is_duplicate_player(self, name):
        return any(player.name == name for player in self.players)

    def take_turn(self, player):
        input(f"{player.name}'s turn. Press Enter to roll the dice...")
        roll = self.dice.roll()
        print(f"{player.name} rolls {roll[0]},{roll[1]}. ", end="")
        self.board.move_player(player, sum(roll), self.players)
