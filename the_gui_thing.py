from project_object_yeeet import Characters,Room,Loot_crate
import tkinter
class Room_GUI(tkinter.Frame):
    def __init__(self,master,Charachters,Room,Loot_crate,small_image):
        super(Room_GUI,self).__init__(master)
        self.room=Room
        self.characters=Charachters
        self.loot_crate=Loot_crate

        self.small_image=small_image
        self.Room_widgets()
        self.alerts()
    def Room_widgets(self):
        imageSmall = tkinter.PhotoImage(file="images/" + "dungeon_floor.jpg")
        w = tkinter.Label(self,
                          image=imageSmall,
                          )
        w.photo = imageSmall
root=tkinter.Tk()
root.title=("HI")
root.mainloop()

