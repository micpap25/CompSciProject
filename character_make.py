#HI
from project_object_yeeet import Characters
class CharList(object):
    def __init__(self, file_name):
        self.file_name = file_name
    def load_chars(self):
        self.character_list = []

        text_file = open(self.file_name, "r")

        for line in text_file:
            line = line.strip()
            my_fields = line.split(", ")
            character = Characters(my_fields)
            self.character_list.append(character)
        return self.character_list