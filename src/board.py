class Board:
    def __init__(self):
        self.spaces = 63
        self.goose_spaces = [5, 9, 14, 18, 23, 27]


    def is_winner(self, player):
        return player.position == self.spaces

    def move_player(self, player, steps, players):
        """
        Moves the player on the board based on the number of steps.

        Args:
            player (Player): The player to move.
            steps (int): The number of steps to move the player.
            players (list): The list of all players in the game.
        """
        prev_position = player.position
        player.position += steps

        if player.position == 6: # The Bridge
            print(f"{player.name} moves from {prev_position} to The Bridge. {player.name} jumps to 12")
            player.position = 12 # The Goose
        elif player.position in self.goose_spaces:
            self.move_player_goose(player, prev_position)
        elif player.position > self.spaces: # Bounce
            player.position = self.spaces - (player.position - self.spaces)
            print(f"{player.name} moves from {prev_position} to 63. {player.name} bounces! {player.name} returns to {player.position}")
        else:
            self.prank(player, prev_position, players)

    def move_player_goose(self, player, prev_position):
        """
        Moves the player when landing on a goose space.

        Args:
            player (Player): The player to move.
            prev_position (int): The previous position of the player.
        """
        print(f"{player.name} moves from {prev_position} to {player.position}, The Goose. ", end="")