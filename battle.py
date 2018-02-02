import tkinter
import random
import winsound


class Screen_Battle(tkinter.Frame):
    def __init__(self, master, player1, player2, call_on_next, ):
        super(Screen_Battle, self).__init__(master)
        # Make a variable so that max HP is set up only once
        # Save references to the two player object
        self.player1 = player1
        self.player2 = player2
        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hp  # Need to fix these, max HP is going down to current HP
        self.player2_max_hp = player2.hp

        # Save the method reference to which we return control after this page Exits.
        self.call_on_selected = call_on_next
        self.item()
        self.create_widgets()
        self.grid()

    def create_widgets(self):
        tkinter.Label(self, text="you").grid(row=0)
        imageSmall = tkinter.PhotoImage(file="images2/" + self.player1.pic, master=self)
        w = tkinter.Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=1, column=0)
        tkinter.Label(self, text="VS", font=30).grid(row=1, column=1)
        tkinter.Label(self, text="enemy").grid(row=0, column=2)
        imageSmall = tkinter.PhotoImage(file="images2/" + self.player2.pic, master=self)
        w = tkinter.Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=1, column=2)
        tkinter.Label(self, text="health: " + str(self.player1.hp) + "/" + str(self.player1_max_hp)).grid(row=2,
                                                                                                          column=0)
        tkinter.Label(self, text="health: " + str(self.player2.hp) + "/" + str(self.player2_max_hp)).grid(row=2,
                                                                                                          column=2)
        self.next = tkinter.Button(self, text="Attack", command=self.attack_clicked, bg="red")
        self.end = tkinter.Button(self, text="END", command=self.exit_clicked)
        self.next.grid(row=5, column=4)

    #
    def item(self):
        self.menuVar = tkinter.StringVar()
        self.list = self.player1.inventory
        if len(self.list) > 0:
            self.menuVar.set(self.list[0])
            self.show = tkinter.OptionMenu(self, self.menuVar, *self.list)
            self.show.grid(row=6, column=0, sticky=tkinter.W)
            self.useItem = tkinter.Button(self, text="Use item", command=self.using)
            self.useItem.grid(row=6, column=1, sticky=tkinter.W)
            self.information = tkinter.Text(self, wrap=tkinter.WORD, width=15, height=5)
            self.information.grid(row=7, column=0, sticky=tkinter.W)

    def using(self):
        k = self.menuVar.get()
        info = self.player1.use_item(str(k))
        self.information.delete(0.0, tkinter.END)
        self.information.insert(0.0, info)
        self.list = self.player1.inventory

        '''
        This method creates all of the widgets for the battle page.
        '''
        #
        # TO DO
        #

    def attack_clicked(self):
        battle = random.randrange(0, 1)
        if battle == 0:
            self.player1.s_attack(self.player2)
            self.player2.attack(self.player1)
        if battle == 1:
            self.player2.attack(self.player1)
            self.player1.s_attack(self.player2)
        if self.player1.hp <= 0 or self.player2.hp <= 0:
            if self.player1.hp <= 0 and self.player2.hp <= 0:
                tkinter.Label(self, text="It is a tie", font=30).grid(column=1)
                self.end.grid(column=3)
                self.next.destroy()
            elif self.player2.hp <= 0:
                tkinter.Label(self, text="DEAD", font=30).grid(row=1, column=2)
                tkinter.Label(self, text="You win", font=30).grid(column=1)
                p = self.player1.search1()
                self.item()
                self.l = tkinter.Label(self, text=p)
                self.l.grid(columnspan=5)
                self.end.grid(column=3)
                self.player1.event -= 5
                self.next.destroy()
            elif self.player1.hp <= 0:
                tkinter.Label(self, text="DEAD", font=30).grid(row=1, column=0)
                tkinter.Label(self, text="You lose", font=30).grid(column=1)
                self.end.grid(column=3)
                self.next.destroy()

        tkinter.Label(self, text="health: " + str(self.player1.hp) + "/" + str(self.player1_max_hp)).grid(row=2,
                                                                                                          column=0)
        tkinter.Label(self, text="health: " + str(self.player2.hp) + "/" + str(self.player2_max_hp)).grid(row=2,
                                                                                                          column=2)
        self.item()
        ''' This method is called when the user presses the "Attack" button.

            This method does the following:
            1) Calls the character.attack method for both the player and the computer.
            2) Updates the labels on the top right with the result of the attacks.
            3) Determines if there is a victor.
            4) If there is a victor, removes that Attack button and replaces it with an Exit button.     
        '''
        #
        # TO DO1
        #

    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked.
            It passes control back to the callback method. '''
        winsound.PlaySound(None, winsound.SND_ASYNC)
        self.call_on_selected()
