from program.controller.commands.editors.edit_command import IEditor
from program.model.model import Model


class Sort(IEditor):
    def doMe(self, selected_file):
        Model().sortStudents(selected_file)
