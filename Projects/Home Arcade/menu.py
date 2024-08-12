from games_data import games_database

class Menu:
    def __init__(self, game_system):
        self.game_system = game_system
        self.menu_states = [
            {"title": "Play Game", "action": self.play_game},
            {"title": "Toggle System Power", "action": ""},
            {"title": "View Game Reports", "action": ""},
            {"title": "View Game Database", "action": ""},
            {"title": "Edit Game Database", "action": ""}
        ]


    def play_game(self):
        game_title = input("Enter the title of the game you want to play: ").lower()
        game_exists = any(game["title"].lower() == game_title for game in games_database)
        if game_exists:
            self.game_system.play_game(game_title)
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


    def run(self):
        while True:
            self.display_menu()
            choice = self.get_user_choice()
            self.menu_states[choice - 1]["action"]()
