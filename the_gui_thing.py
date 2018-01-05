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
        self.moveButton()
        self.grid()
        #self.alerts()
    def Room_widgets(self):
        imageSmall = tkinter.PhotoImage(file="Images\dungeon.png")
        w = tkinter.Label(self,
                          image=imageSmall,
                          )
        w.photo = imageSmall
        w.grid(row = 1, column = 1, columnspan = 2, sticky = tkinter.W)
    def moveButton(self):
        self.direction = tkinter.StringVar()
        self.direction.set(tkinter.NONE)
        #To move, choose a radiobutton then press the movebutton.
        # It passes it off to move in project_objects which changes position
        #We can place the move button above the image, and the radiobuttons in their corresponding places around it.
        self.north = tkinter.Radiobutton(self, text="North", variable=self.direction, value="N")
        self.north.grid(row = 0, column = 2, sticky = tkinter.W)
        self.west = tkinter.Radiobutton(self, text="West", variable=self.direction, value="W")
        self.west.grid(row = 1, column = 0, sticky = tkinter.W)
        self.south = tkinter.Radiobutton(self, text="South", variable=self.direction, value="S")
        self.south.grid( row = 2, column = 2, sticky = tkinter.W)
        self.east = tkinter.Radiobutton(self, text="East", variable=self.direction, value="E")
        self.east.grid(row = 1, column = 3, sticky = tkinter.W)
        self.move_bttn = tkinter.Button(self, text = "Move", command = self.moving)
        self.move_bttn.grid(row = 2, column = 3, sticky = tkinter.W)
    def moving(self):
        Characters.moveAround('"fill in whatever the player is"', self.direction)
    def searchButton(self):
        self.search_bttn = tkinter.Button(self, text = "Search", command = self.searching)
        self.search_bttn.grid(row = 2, column = 0, sticky = tkinter.W)
    def searching(self):
        Characters.search("fill in whatever the player is")



root=tkinter.Tk()
root.title("HI")
app=Room_GUI(root)
root.mainloop()

