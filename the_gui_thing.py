import random
from battle import Screen_Battle
from project_object_yeeet import Characters,Room,Player,EnemyList
from character_make import CharList
import tkinter
import winsound
import time

class Room_GUI(tkinter.Frame):
    def __init__(self,master):
        super(Room_GUI,self).__init__(master)
        #self.room=Room
        #self.characters=Charachters
        #self.loot_crate=Loot_crate
        c = CharList("All_DA_Characters.txt")
        self.chars = c.load_chars()
        self.x = 0
        self.select_character()
        self.grid()
        # self.alerts()
    def select_character(self):
        c = CharList("All_DA_Characters.txt")
        self.chars = c.load_chars()
        self.character = tkinter.StringVar()
        winsound.PlaySound(None, winsound.SND_ASYNC)
        for widget in self.winfo_children():
            widget.destroy()
        self.da_boss=Characters(["DABoss", 150, 50, 65, "Da_boss.gif"])
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
            print(c.pic)
            imageSmall = tkinter.PhotoImage(file="images2/" + c.pic)
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
        createchar = tkinter.Button(self,text="custom character",command=self.makechar)
        createchar.grid()
        nxt_bttn = tkinter.Button(self, text="Next", command=self.move_on)
        nxt_bttn.grid(row=10, column= 4, sticky=tkinter.E)

    def move_on(self):
        self.cho = int(self.character.get())

        self.player = Player(self.chars[self.cho])

        for widget in self.winfo_children():
            widget.destroy()
        self.Room_widgets()
        self.moveButton()
        self.grid()
        self.searchButton()
        self.items()
    def Room_widgets(self):
        self.imageSmall = tkinter.PhotoImage(file="Images\dungeon.png")
        self.w = tkinter.Label(self,
                          image=self.imageSmall,
                          )
        self.w.photo = self.imageSmall
        self.w.grid(row = 1, column = 1, columnspan = 2, sticky = tkinter.W)
    def makechar(self):
        for widgets in self.winfo_children():
            widgets.destroy()
        tkinter.Label(self,text="Name").grid()
        tkinter.Label(self,text=" you have a total of 250 points to put in eh category but no category can exceed 120")
        tkinter.Label(self,text="Pick a name.").grid()
        self.n0= tkinter.Entry(self)
        self.n0.grid()
        tkinter.Label(self, text="Pick a number of health.").grid()
        self.n1=tkinter.Entry(self)
        self.n1.grid()
        tkinter.Label(self,text="Pick an attack.").grid()
        self.n2=tkinter.Entry(self)
        self.n2.grid()
        tkinter.Label(self, text="Pick a speed.").grid()
        self.n3=tkinter.Entry(self)
        self.n3.grid()
        hi = tkinter.Button(self,text=" confirm", command=self.makechar2)
        hi.grid()
    def makechar2(self):
        if int(self.n1.get()) + int(self.n2.get()) +int(self.n3.get()) >250 or int(self.n1.get())>120 or int(self.n2.get())>120 or int(self.n3.get())>120:
            self.p = tkinter.Label(self,text="you have exceeded your budget")
            self.p.grid()
            root.after(2000,self.p1)
            self.makechar()
        else:
            file=open("All_Da_characters.txt", "a+")
            file.write("\n" + self.n0.get() +  ", "+ self.n1.get()+", "+self.n2.get()+", " + self.n3.get()+", images.gif")
            file.close()
            for widgets in self.winfo_children():
                widgets.destroy()
            self.select_character()
    def p1(self):
        self.p.destroy()
    def moveButton(self):
        p = random.randrange(0, 3)

        self.direction = tkinter.StringVar()
        self.direction.set(tkinter.NONE)
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
        t = random.randrange(0,7)
        if t in [1, 2] and self.x > 0:
            self.merchant()
        self.x += 1
    def moving(self):
        self.player.event += 5
        self.imageSmall = tkinter.PhotoImage(file="images\dungeon.png")
        self.w = tkinter.Label(self,image = self.imageSmall,)
        self.w.photo = self.imageSmall
        self.w.grid(row=1, column=1, columnspan=2, sticky=tkinter.W)
        self.east.destroy()
        self.south.destroy()
        self.west.destroy()
        self.north.destroy()
        self.items()
        if self.search_bttn.winfo_exists()==0:
            self.searchButton()

        if self.da_boss.hp<=0 and self.player.hp>0:
            for widget in self.winfo_children():
                widget.destroy()
            self.p = tkinter.Label(self, text="YOU WIN!")
            self.p.grid()
            self.replay = tkinter.Button(self, text="replay?", command=self.select_character)
            self.replay.grid()
        if self.da_boss.hp>0 and self.player.hp>0:
            MyDialog(root, self.player,self.da_boss)
        if self.da_boss.hp > 0:
            self.moveButton()
        if self.player.hp<=0:

            for widget in self.winfo_children():
                widget.destroy()
            self.p = tkinter.Label(self, text="You Lose")
            self.p.grid()
            winsound.PlaySound('sound\Rick-Astley-Never-Gonna-Give-You-Up.wav', winsound.SND_ASYNC)
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
        self.items()
        if self.da_boss.hp<=0 and self.player.hp>0:
            for widget in self.winfo_children():
                widget.destroy()
            self.p = tkinter.Label(self, text="YOU WIN!")
            self.p.grid()
            self.replay = tkinter.Button(self, text="replay?", command=self.select_character)
            self.replay.grid()
        if self.da_boss.hp > 0 and self.player.hp > 0:
            MyDialog(root,self.player, self.da_boss)
        if self.player.hp<=0:
            for widget in self.winfo_children():
                widget.destroy()
            self.p = tkinter.Label(self,text="You Lose")
            self.p.grid()
            winsound.PlaySound('sound\Rick-Astley-Never-Gonna-Give-You-Up.wav', winsound.SND_ASYNC)
            self.replay=tkinter.Button(self,text="replay?",command=self.select_character)
            self.replay.grid()
    def l_destroy(self):
            self.l.destroy()
    def items(self):
        self.menuVar = tkinter.StringVar()
        self.list = self.player.inventory
        if len(self.list) > 0:
            self.menuVar.set(self.list[0])
            self.show = tkinter.OptionMenu(self, self.menuVar, *self.list)
            self.show.grid(row=4, column=0, sticky=tkinter.W)
            self.useItem = tkinter.Button(self, text="Use item", command=self.using)
            self.useItem.grid(row=4, column=1, sticky=tkinter.W)
            self.information = tkinter.Text(self, wrap = tkinter.WORD, width = 15, height = 5)
            self.information.grid(row=5, column=0, sticky=tkinter.W)

    def using(self):
        k = self.menuVar.get()
        info = self.player.use_item(str(k))
        self.information.delete(0.0, tkinter.END)
        self.information.insert(0.0, info)
        self.list = self.player.inventory
        self.show.destroy()
        self.show = tkinter.OptionMenu(self, self.menuVar, *self.list)
        self.show.grid(row=4, column=0, sticky=tkinter.W)
    def merchant(self):
        self.inventory = []
        r = ["Potion: 10 Gold", "Speed Potion: 15 Gold", "Strength Potion: 15 Gold", "Strange potion: 5 Gold"]
        for i in range(0, 4):
            random_index = random.randrange(0, len(r))
            self.inventory.append(r[random_index])
        self.player.money=10
        self.widgets1()
    def widgets1(self):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.menuVar1 = tkinter.StringVar()
        self.list = self.inventory
        tkinter.Label(self,text="you have"+str(self.player.money)+"gold coins").grid()
        if len(self.list) > 0:
            self.menuVar1.set(self.list[0])
            self.show = tkinter.OptionMenu(self, self.menuVar1, *self.list)
            self.show.grid(row=4, column=0, sticky=tkinter.W)
            self.useItem1 = tkinter.Button(self, text="buy item", command=self.buy)
            self.useItem1.grid(row=4, column=1, sticky=tkinter.W)
            self.information1 = tkinter.Text(self, wrap=tkinter.WORD, width=15, height=5)
            self.information1.grid(row=5, column=0, sticky=tkinter.W)
        self.exit = tkinter.Button(self,text="Exit",command=self.clear)
        self.exit.grid()
    def clear(self):
        for widgets in self.winfo_children():
            widgets.destroy()
        self.moving()
    def buy(self):
        self.choice = self.menuVar1.get()
        if self.choice == "Strange potion: 5 Gold" and self.player.money >= 5:
            self.player.inventory.append("Strange Potion")
            self.player.money -= 5
            w = "you now have a strange potion"
            self.information1.insert(0.0,w)
        if self.choice == "Potion: 10 Gold" and self.player.money >= 10:
            self.player.inventory.append("Potion")
            self.player.money -= 10
            w = "you now have a potion"
            self.information1.insert(0.0, w)
        if self.choice == "Speed Potion: 15 Gold" and self.player.money >= 15:
            self.player.speed += 10
            self.player.money -= 15
            w = "you now have a speed potion"
            self.information1.insert(0.0, w)
        if self.choice == "Strength Potion: 15 Gold" and self.player.money >= 15:
            self.player.attck += 10
            self.player.money -= 15
            w = "you now have a strength potion"
            self.information1.insert(0.0, w)

class MyDialog:

    def __init__(self, parent,player,da_boss):
        self.player=player
        Room(self.player,da_boss)

root=tkinter.Tk()
root.title("HI")
app=Room_GUI(root)
root.mainloop()

#HI1
