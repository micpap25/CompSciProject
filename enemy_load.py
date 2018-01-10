#HI
from project_object_yeeet import Characters
class EnemyList(object):
    def __init__(self, file_name):
        self.file_name = file_name
    def load_chars(self):
        self.enemy_list = []

        text_file = open(self.file_name, "r")

        for line in text_file:
            line = line.strip()
            my_fields = line.split(",")
            enemy = Characters(my_fields[0], int(my_fields[1]), int(my_fields[2]), int(my_fields[3]), my_fields[4])
            self.enemy_list.append(enemy)
        return self.enemy_list