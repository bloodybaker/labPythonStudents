from program.controller.commands.editors.edit_command import IEditor
from program.model.model import Model

class Search(IEditor):
    def doMe(self, selected_file):
        Model().searchStudent(selected_file)