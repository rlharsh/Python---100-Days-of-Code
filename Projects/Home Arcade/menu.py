from games_data import games_database
from gameconsole import GameConsole

class Menu:
    def __init__(self, game_system: GameConsole):
        self.game_system = game_system
        self.exit_pending = False
        self.menu_states = [
            {"title": "Play/Stop Game", "action": self.play_game},
            {"title": "Toggle System Power", "action": self.toggle_system_power},
            {"title": "View Game Reports", "action": ""},
            {"title": "View Game Database", "action": ""},
            {"title": "Edit Game Database", "action": ""},
            {"title": "Quit", "action": self.exit_application}
        ]


    def exit_application(self):
        print(f"Kill signal received.")
        self.exit_pending = True


    def play_game(self):
        if self.game_system.status_in_game:
            self.game_system.stop_game()
            return
        game_title = input("Enter the title of the game you want to play: ").lower()
        game_data = next((game for game in games_database if game["title"].lower() == game_title.lower()), None)

        if game_data != None:
            self.game_system.play_game(game_data)
        else:
            print(f"Could not locate {game_title} in the game database.")


    def get_user_choice(self):
        while True:
            try:
                choice = int(input("Enter your choice: "))
                if 1 <= choice <= len(self.menu_states):
                    return choice
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")


    def display_menu(self):
        print("\nGame Console Menu:")
        for i, state in enumerate(self.menu_states, 1):
            print(f"{i}. {state["title"]}")


    def toggle_system_power(self):
        self.game_system.toggle_system_power()


    def run(self):
        while not self.exit_pending:
            self.display_menu()
            choice = self.get_user_choice()
            self.menu_states[choice - 1]["action"]()
