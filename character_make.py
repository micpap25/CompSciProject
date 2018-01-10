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
            character = Characters(my_fields[0], int(my_fields[1]), int(my_fields[2]), int(my_fields[3]), my_fields[4])
            self.character_list.append(character)
        return self.character_list