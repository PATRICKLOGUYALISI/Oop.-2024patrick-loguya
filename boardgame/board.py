class BoardGame:
    def __init__(self, name, min_players, max_players):
        self.name = name
        self.min_players = min_players
        self.max_players = max_players

    def display_info(self):
        return f"Board Game: {self.name}, Players: {self.min_players}-{self.max_players}"

    def is_playable(self, players):
        return self.min_players <= players <= self.max_players

# Example usage
game1 = BoardGame("Catan", 3, 4)
print(game1.display_info())
print(game1.is_playable(4))
