from project_object_yeeet import Characters,Loot_crate,Room
from character_make import CharList
import tkinter
class Room_GUI(tkinter.Frame):
    def __init__(self,master):#,Charachters,Room,Loot_crate):
        super(Room_GUI,self).__init__(master)
        #self.room=Room
        #self.characters=Charachters
        #self.loot_crate=Loot_crate

        #self.small_image=small_image
        c = CharList("All_DA_Characters.txt")
        self.chars = c.load_chars()
        self.select_character()
        self.grid()
        #self.alerts()
    def select_character(self):
        self.character = tkinter.StringVar()
        self.character.set(None)
        self.hp = tkinter.Label(self, text="Hit Points").grid(row=0, column=2, sticky=tkinter.W)
        self.dex = tkinter.Label(self, text="Dexterity").grid(row=0, column=3, sticky=tkinter.W)
        self.str = tkinter.Label(self, text="Strength").grid(row=0, column=4, sticky=tkinter.W)
        row = 1
        for c in self.chars:
            cho_button = tkinter.Radiobutton(self, text=c.name, variable=self.character, value=row - 1)
            cho_button.grid(row=row, column=0, sticky=tkinter.W)
            cre_hp = tkinter.Label(self, text=c.hp).grid(row=row, column=2, sticky=tkinter.W)
            cre_dex = tkinter.Label(self, text=c.speed).grid(row=row, column=3, sticky=tkinter.W)
            cre_str = tkinter.Label(self, text=c.attck).grid(row=row, column=4, sticky=tkinter.W)
            row += 1
        nxt_bttn = tkinter.Button(self, text="Next", command=self.move_on)
        nxt_bttn.grid(row=10, column=4, sticky=tkinter.W)
    def move_on(self):
        self.cho = self.character
        self.player = self.chars[self.cho]
        for widget in self.winfo_children():
            widget.destoy()
        self.Room_widgets()
        self.moveButton()
    def Room_widgets(self):
        tkinter.Label()
        imageSmall = tkinter.PhotoImage(file="Images\dungeon_floor.jpg")
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
        self.direction = tkinter.StringVar()
        self.direction.set(tkinter.NONE)
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
        Characters.moveAround(self.player, self.direction)
    def searchButton(self):
        self.search_bttn = tkinter.Button(self, text = "Search", command = self.searching)
    def searching(self):
        Characters.search(self.player)



root=tkinter.Tk()
root.title("HI")
app=Room_GUI(root)
root.mainloop()

