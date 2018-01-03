from project_object_yeeet import Characters,Room,Loot_crate
import tkinter
class Room_GUI(tkinter.Frame):
    def __init__(self,master,Charachters,Room,Loot_crate):
        super(Room_GUI,self).__init__(master)
        self.room=Room
        self.characters=Charachters
        self.loot_crate=Loot_crate
        self.Room_widgets()
        self.alerts()
    def Room_widgets(self):

    def alerts(self):

