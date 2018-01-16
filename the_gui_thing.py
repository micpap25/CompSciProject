import random
from battle import Screen_Battle
from project_object_yeeet import Characters,Room,Player
from character_make import CharList
import tkinter
import time
class Room_GUI(tkinter.Frame):
    def __init__(self,master):#,Charachters,Room,Loot_crate):
        super(Room_GUI,self).__init__(master)
        #self.room=Room
        #self.characters=Charachters
        #self.loot_crate=Loot_crate
        c = CharList("All_DA_Characters.txt")
        self.chars = c.load_chars()
        self.select_character()
        self.grid()
        # self.alerts()
    def select_character(self):
        c = CharList("All_DA_Characters.txt")
        self.chars = c.load_chars()
        self.character = tkinter.StringVar()
        for widget in self.winfo_children():
            widget.destroy()
        self.character.set(None)
        self.hp = tkinter.Label(self, text="Hit Points")
        self.hp.grid(row=0, column=2, sticky=tkinter.W)
        self.dex = tkinter.Label(self, text="Dexterity")
        self.dex.grid(row=0, column=3, sticky=tkinter.W)
        self.str = tkinter.Label(self, text="Strength")
        self.str.grid(row=0, column=4, sticky=tkinter.W)
        row = 1

        for c in self.chars:
            cho_button = tkinter.Radiobutton(self, text=c.name, variable=self.character, value=row - 1)
            cho_button.grid(row=row, column=0, sticky=tkinter.W)
            imageSmall = tkinter.PhotoImage(file="images/" + c.pic)
            w = tkinter.Label(self, image=imageSmall)
            w.photo = imageSmall
            w.grid(row=row, column=1, sticky=tkinter.W)
            cre_hp = tkinter.Label(self, text=c.hp)
            cre_hp.grid(row=row, column=2, sticky=tkinter.W)
            cre_dex = tkinter.Label(self, text=c.speed)
            cre_dex.grid(row=row, column=3, sticky=tkinter.W)
            cre_str = tkinter.Label(self, text=c.attck)
            cre_str.grid(row=row, column=4, sticky=tkinter.W)
            row += 1
        nxt_bttn = tkinter.Button(self, text="Next", command=self.move_on)
        nxt_bttn.grid(row=10, column=4, sticky=tkinter.W)


    def move_on(self):
        self.cho = int(self.character.get())

        self.player = Player(self.chars[self.cho])

        for widget in self.winfo_children():
            widget.destroy()
        self.Room_widgets()
        self.moveButton()
        self.grid()
        self.items()
    def Room_widgets(self):
        self.imageSmall = tkinter.PhotoImage(file="Images\dungeon.png")
        self.w = tkinter.Label(self,
                          image=self.imageSmall,
                          )
        self.w.photo = self.imageSmall
        self.w.grid(row = 1, column = 1, columnspan = 2, sticky = tkinter.W)
        self.searchButton()
    def moveButton(self):
        p = random.randrange(0, 3)
        self.direction = tkinter.StringVar()
        self.direction.set(tkinter.NONE)
        self.disclaimer=tkinter.Label(self,text="you will automatically be moved east if you don't enter a field").grid(row=5,column=1,columnspan=5)
        self.north = tkinter.Radiobutton(self, text="North", variable=self.direction, value="N")

        if p <= 0:
            self.north.grid(row=0, column=2, sticky=tkinter.W)
        self.west = tkinter.Radiobutton(self, text="West", variable=self.direction, value="W")

        if p <= 1:
            self.west.grid(row=1, column=0, sticky=tkinter.W)
        self.south = tkinter.Radiobutton(self, text="South", variable=self.direction, value="S")

        if p <= 2:
            self.south.grid(row=2, column=2, sticky=tkinter.W)
        self.east = tkinter.Radiobutton(self, text="East", variable=self.direction, value="E")

        if p <= 3:
            self.east.grid(row=1, column=3, sticky=tkinter.W)

        self.move_bttn = tkinter.Button(self, text="Move", command=self.moving)
        self.move_bttn.grid(row=2, column=3, sticky=tkinter.W)
    def moving(self):
        self.player.event += 5
        self.imageSmall = tkinter.PhotoImage(file="Images\dungeon.png")
        self.w = tkinter.Label(self,image = self.imageSmall,)
        self.w.photo = self.imageSmall
        self.w.grid(row=1, column=1, columnspan=2, sticky=tkinter.W)
        self.east.destroy()
        self.south.destroy()
        self.west.destroy()
        self.north.destroy()
        self.searchButton()
        if self.player.hp>0:
            Room(self.player)
        if self.player.hp>0:
            self.moveButton()
        if self.player.hp<=0:
            for widget in self.winfo_children():
                widget.destroy()
            self.p = tkinter.Label(self, text="You Lose")
            self.p.grid()
            self.replay = tkinter.Button(self, text="replay?", command=self.select_character)
            self.replay.grid()
    def searchButton(self):
        self.search_bttn = tkinter.Button(self, text = "Search", command = self.searching)
        self.search_bttn.grid(row = 2, column = 0, sticky = tkinter.W)
    def searching(self):
        self.search_bttn.destroy()
        p = self.player.search()
        self.l = tkinter.Label(self, text=p)
        self.l.grid(row=6,column=0,columnspan=5)
        root.after(3000,self.l_destroy)
        if self.player.hp>0:
            Room(self.player)
        self.items()
        if self.player.hp<=0:
            for widget in self.winfo_children():
                widget.destroy()
            self.p = tkinter.Label(self,text="You Lose")
            self.p.grid()
            self.replay=tkinter.Button(self,text="replay?",command=self.select_character)
            self.replay.grid()
    def l_destroy(self):
        self.l.destroy()

    def items(self):
        self.info = ""
        self.menuVar = tkinter.StringVar()
        self.list = self.player.inventory
        if len(self.list) > 0:
            self.menuVar.set(self.list[0])
            self.show = tkinter.OptionMenu(self, self.menuVar, *self.list)
            self.show.grid(row=4, column=0, sticky=tkinter.W)
            self.useItem = tkinter.Button(self, text="Use item", command=self.using)
            self.useItem.grid(row=4, column=1, sticky=tkinter.W)
            self.information = tkinter.Label(self, text=self.show)
            self.information.grid(row=5, column=0, sticky=tkinter.W)

    def using(self):
        self.menuVar.get()
        self.info = self.player.use_item(str(self.menuVar))
#hi
root=tkinter.Tk()
root.title("HI")
app=Room_GUI(root)
root.mainloop()

#HI

