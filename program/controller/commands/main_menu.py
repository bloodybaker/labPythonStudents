from program.controller.commands.command import ICommand
from program.view.menus import Menus


class MainMenu(ICommand):

    def execute(self):
        return Menus().printMainMenu()