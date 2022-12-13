from program.controller.commands.editors.add import Add
from program.controller.commands.editors.update import Update
from program.controller.commands.editors.delete import Delete
from program.controller.commands.editors.sort import Sort
from program.controller.commands.editors.search import Search
from program.controller.commands.editors.print import Print
from program.controller.commands.main_menu import MainMenu
from program.controller.commands.options import Options
from program.model.model import Model
from program.view.menus import Menus

class MainController:
    options = dict()

    def fillOptions(self):
        self.options[0] = Print()
        self.options[1] = Add()
        self.options[2] = Delete()
        self.options[3] = Update()
        self.options[4] = Sort()
        self.options[5] = Search()

    def chooseOption(self, selected_file):
        self.fillOptions()
        Menus().suggestion()
        choice = int(input())
        if choice > 0 and choice <= len(self.options):
            obj = list(self.options.values())[choice-1]
            obj.doMe(selected_file)
        else:
            self.chooseOption(selected_file)

    def selectFile(self):
       files = MainMenu().execute()
       Menus().suggestion()
       selected_file = Model().file_worker.extract(files)
       Options().execute()
       self.chooseOption(str(selected_file))


