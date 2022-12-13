from program.controller.commands.editors.edit_command import IEditor
from program.model.model import Model


class Update(IEditor):
    def doMe(self, selected_file):
        Model().updateValue(selected_file)