import pandas as pd
import io

from program.model.file_worker import FileWorker

class Model:

    file_worker = FileWorker()

    def addValue(self, file_path):
        path = self.file_worker.buildPath(file_path)
        df = pd.read_csv(path, sep=",", header=None)
        print(df.to_string(header=False))
        print("Enter data in format: Name,score")
        input_row = input()
        if self.checkRow(input_row):
            new_row = pd.read_csv(io.StringIO(input_row), sep=",", header=None)
            df = df.append(new_row, ignore_index=False)
            self.file_worker.saveChanges(path, df)
        else:
            print("Wrong input, try it again")
            self.addValue(file_path)

    def checkRow(self, input_row: str) -> bool:
        parts = input_row.split(",")
        if len(parts) > 2:
            return False
        if not isinstance(parts[0], str):
            return False
        if not isinstance(parts[1], (str, int)):
            return False
        return True


    def deleteValue(self, file_path):
        path = self.file_worker.buildPath(file_path)
        df = pd.read_csv(path, sep=",", header=None)
        print(df.to_string(header=False))
        print("Enter the index of element to remove:")
        input_index = 0
        try:
            input_index = int(input())
        except:
            print("Use number! Try it again.")
            self.deleteValue(file_path)
        df = df.drop(input_index)
        self.file_worker.saveChanges(path, df)

    def updateValue(self, file_path):
        path = self.file_worker.buildPath(file_path)
        df = pd.read_csv(path, sep=",", header=None)
        print(df.to_string(header=False))
        print("Enter the index of element to update:")
        input_index = 0
        try:
            input_index = int(input())
        except:
            print("Use number! Try it again.")
            self.updateValue(file_path)
        print("Enter data in format: Name,score")
        input_row = input()
        df.at[input_index, 0] = input_row.split(",")[0]
        df.at[input_index, 1] = input_row.split(",")[1]
        self.file_worker.saveChanges(path, df)

    def showStudents(self, file_path):
        path = self.file_worker.buildPath(file_path)
        df = pd.read_csv(path, sep=",", header=None)
        print(df.to_string(header=False))

    def sortStudents(self, file_path):
        path = self.file_worker.buildPath(file_path)
        df = pd.read_csv(path, sep=",", header=None)
        df = df.sort_values(1)
        print("=/=/= SORTED =\=\=")
        print(df.to_string(header=False))
        print("Do you want to save it? Enter y(Yes) to save or n(No) to discard this change:")
        dialog = input()
        if dialog.lower() == "y" or dialog.lower() == "yes":
            self.file_worker.saveChanges(path, df)

    def searchStudent(self, file_path):
        path = self.file_worker.buildPath(file_path)
        df = pd.read_csv(path, sep=",", header=None)
        print(df.to_string(header=False))
        print("Enter the part of name to search:")
        input_name = input()
        df = df.loc[df[0] == input_name]
        print("|==|==| Found " + str(df.size-1) + " rows |==|==|")
        print(df.to_string(header=False))
        print("|==|==|==|==|==|==|==|==|==|==|==|==|")