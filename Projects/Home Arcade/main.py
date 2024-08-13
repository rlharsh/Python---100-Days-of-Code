from gameconsole import GameConsole
from menu import Menu

my_console = GameConsole()
my_menu = Menu(my_console)

while not my_menu.exit_pending:
    my_menu.run()
