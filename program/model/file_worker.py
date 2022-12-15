import os

class FileWorker:
    def buildPath(self, file_path):
        return os.getcwd() + "/files/" + file_path

    def extract(self, menu):
        file_path = ""
        input_value = int(input())
        if input_value <= len(menu) and input_value > 0:
            file_path = list(menu.values())[input_value - 1]
        else:
            print("Input Error, try again.")
        return file_path

    def saveChanges(self, path, dataframe):
        print("============= SAVED =============")
        print(dataframe)
        print("============= SAVED =============")
        dataframe.to_csv(path, sep=',', encoding='utf-8', header=None, index=False)