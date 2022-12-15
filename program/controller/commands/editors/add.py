from program.controller.commands.editors.edit_command import IEditor
from program.model.model import Model

class Add(IEditor):
    def doMe(self, selected_file):
        Model().addValue(selected_file)
