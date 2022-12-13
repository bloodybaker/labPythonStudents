import os


class Menus:
    def printMainMenu(self):
        main_menu = dict(enumerate(os.listdir(os.getcwd() + "/files")))
        for key in main_menu:
            print(key + 1, " - ", main_menu[key])
        return main_menu

    def printOptions(self):
        print("1. Show students")
        print("2. Add student")
        print("3. Remove student")
        print("4. Update student")
        print("5. Sort students")
        print("6. Search student")

    def suggestion(self):
        print("Select an option: ")
