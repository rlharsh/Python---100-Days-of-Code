from gameconsole import GameConsole
from menu import Menu

my_console = GameConsole()
my_menu = Menu(my_console)

while True:
    my_menu.run()
