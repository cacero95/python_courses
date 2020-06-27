import notes.Notes as model
import pathlib
import os
from io import open
BASE_DIR = str(pathlib.Path().absolute())

class Actions:
    
    def create(self, user):

        print("Lets create your note\n")
        title = input("Type the name of your note: ")
        if not os.path.isdir(f"{BASE_DIR}/assets"):
            os.mkdir(f"{BASE_DIR}/assets")
        new_file = f"{BASE_DIR}/assets/{title}.txt"
        file = open(new_file, "a+")
        file.close()

        note = model.Notes(user, title, f"/assets/{title}.txt")
        note_saved = note.save_note()
        print("Note saved succesfully") if note_saved[0] > 0 else print(f"An error was ocurred {note_saved[1]}")
    
    def catch_item(self, list_items):
        print("-----------------------------")
        item_select = input("Type the number of the file: ")
        print(f"code {BASE_DIR}{list_items[int(item_select)][0]}")
        os.system(f"notepad {BASE_DIR}{list_items[int(item_select)][0]}")

    def show(self, user):
        note = model.Notes(user, "", "")
        list_items = note.show_notes()
        if list_items[0] == True:
            print("-----------------------------")
            for item in range(len(list_items[1])):
                print(f"{item} - {list_items[1][item]}")
            self.catch_item(list_items[1])

    def remove_file(self, title):
        delete_file = f"{BASE_DIR}/assets/{title}.txt"
        if os.path.isfile(delete_file):
            os.remove(delete_file)
            print('deleted')

    def delete(self, user):

        title = input("\nType the name of the file to delete: ")
        note = model.Notes(user, title, "")
        delete = note.delete_notes()
        self.remove_file(title) if delete[0] > 0 else print(delete[1])
        
