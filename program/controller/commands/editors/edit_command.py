from abc import abstractmethod

class IEditor:
    @abstractmethod
    def doMe(self, selected_file: str):
        pass
