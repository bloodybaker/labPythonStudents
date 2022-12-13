from program.controller.commands.editors.edit_command import IEditor
from program.model.model import Model


class Delete(IEditor):
    def doMe(self, selected_file):
        Model().deleteValue(selected_file)