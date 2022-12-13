from program.controller.commands.editors.edit_command import IEditor
from program.model.model import Model


class Print(IEditor):
    def doMe(self, selected_file):
        Model().showStudents(selected_file)
