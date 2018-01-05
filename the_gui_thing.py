from project_object_yeeet import Characters,Loot_crate,Room
import tkinter
class Room_GUI(tkinter.Frame):
    def __init__(self,master):#,Charachters,Room,Loot_crate):
        super(Room_GUI,self).__init__(master)
        #self.room=Room
        #self.characters=Charachters
        #self.loot_crate=Loot_crate

        #self.small_image=small_image
        self.Room_widgets()
        #self.alerts()
    def Room_widgets(self):
        imageSmall = tkinter.PhotoImage(file="Images\dungeon.png")
        w = tkinter.Label(self,
                          image=imageSmall,
                          )
        w.photo = imageSmall
        w.grid()
    def moveButton(self):
        self.direction = ""
        #To move, choose a radiobutton then press the movebutton.
        # It passes it off to move in project_objects which changes position
        #We can place the move button above the image, and the radiobuttons in their corresponding places around it.
        self.north = tkinter.Radiobutton(self, text="North", variable=self.direction, value="N")
        self.north.grid()
        self.west = tkinter.Radiobutton(self, text="West", variable=self.direction, value="W")
        self.west.grid()
        self.south = tkinter.Radiobutton(self, text="South", variable=self.direction, value="S")
        self.south.grid()
        self.east = tkinter.Radiobutton(self, text="East", variable=self.direction, value="E")
        self.east.grid()
        self.move_bttn = tkinter.Button(self, text = "Move", command = self.moving)
    def moving(self):
        Characters.moveAround('"fill in whatever the player is"', self.direction)



root=tkinter.Tk()
root.title("HI")
app=Room_GUI(root)
root.mainloop()

