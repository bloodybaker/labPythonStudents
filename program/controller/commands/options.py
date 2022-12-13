from program.controller.commands.command import ICommand
from program.view.menus import Menus


class Options(ICommand):
    def execute(self):
        Menus().printOptions()