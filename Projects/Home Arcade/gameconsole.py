from games_data import games_database
from prettytable import PrettyTable

class GameConsole:
    def __init__(self):
        self.power_state_on = False

    def get_games_list(self) -> PrettyTable:
        table = PrettyTable()
        table.align = "l"
        table.field_names = ["Title", "Platform", "Release Year", "Meta"]

        for game in games_database:
            table.add_row([
                game["title"],
                game["platform"],
                game["release_year"],
                ", ".join(game["slugs"])
            ])

        return table

    def play_game(self, game_title):
        print(f"Playing {game_title}.")
