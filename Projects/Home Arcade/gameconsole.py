from games_data import games_database
from prettytable import PrettyTable

class GameConsole:
    def __init__(self):
        self.power_state_on = False
        self.status_in_game = False
        self.status_current_game = ""

    def get_games_list(self) -> PrettyTable:
        table = PrettyTable()
        table.align = "l"
        table.field_names = ["Title", "Platform", "Release Year", "Meta", "Play Count"]

        for game in games_database:
            table.add_row([
                game["title"],
                game["platform"],
                game["release_year"],
                ", ".join(game["slugs"]),
                game["play_count"],
            ])
        return table


    def play_game(self, game_data: dict):
        if not self.power_state_on:
            print(f"Unable to load {game_data["title"]}, system is powered off.")
            return

        self.status_in_game = True
        self.status_current_game = game_data
        game_data["play_count"] += 1
        print(f"Playing '{game_data['title']}'. Play count: {game_data['play_count']}.")
        print(self.get_games_list())


    def stop_game(self):
        print(f"Attempting to remove {self.status_current_game["title"]}.")
        self.status_in_game = False
        self.status_current_game = None
        print("System game deck is now empty.")


    def toggle_system_power(self):
        self.power_state_on = not self.power_state_on
        print("System power has been turned on." if self.power_state_on else "System power has been turned off.")
