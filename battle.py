from tkinter import *
#hio
class Screen_Battle(Frame):
    def __init__(self, master, player1, player2, call_on_next):
        super(Screen_Battle, self).__init__(master)

        # Save references to the two player objects
        self.player1 = player1
        self.player2 = player2

        # Store the maximum number of hit points which are needed on the screen display.
        self.player1_max_hp = player1.hit_points
        self.player2_max_hp = player2.hit_points

        # Save the method reference to which we return control after this page Exits.
        self.call_on_selected = call_on_next

        self.create_widgets()
        self.grid()

    def create_widgets(self):
        a = Label(text='You')
        a.grid(row=0, column=0, sticky=W, columnspan=2)

        imageSmall = PhotoImage(file="images/" + self.player1.large_image)
        w = Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=1, column=0, sticky=W, columnspan=2)

        self.hp1 = Label(text='HP-' + str(self.player1.hit_points) + '/' + str(self.player1_max_hp))
        self.hp1.grid(row=2, column=0, sticky=W, columnspan=2)
        self.victor = Label(text='')
        self.victor.grid(row=7, column=2, columnspan=2)

        b = Label(text='Computer')
        b.grid(row=0, column=3, sticky=E, columnspan=2)

        mageSmall = PhotoImage(file="images/" + self.player2.large_image)
        w = Label(self, image=mageSmall)
        w.photo = mageSmall
        w.grid(row=1, column=3, sticky=E, columnspan=2)

        self.hp2 = Label(text='HP-' + str(self.player2.hit_points) + "/" + str(self.player2_max_hp))
        self.hp2.grid(row=2, column=3, sticky=E, columnspan=2)

        self.update = Label(text='')
        self.update.grid(row=6, column=2, columnspan=2)

        self.attack = Button(text="Attack", command=self.attack_clicked)
        self.attack.grid(row=5, column=2, columnspan=2)

        self.exit = Button(text="", command=self.exit_clicked)

        '''
        This method creates all of the widgets for the battle page.
        '''
        #
        # TO DO
        #

    def attack_clicked(self):
        self.attack1 = self.player1.attack(self.player2)
        self.attack2 = self.player2.attack(self.player1)
        '''This is the problem I don't know how to display the damage'''
        self.update["text"] = self.attack1 + '\n' + self.attack2

        self.hp1["text"] = 'HP:' + str(self.player1.hit_points) + '/' + str(self.player1_max_hp)
        self.hp2["text"] = 'HP:' + str(self.player2.hit_points) + '/' + str(self.player2_max_hp)

        if self.player1.hit_points <= 0 or self.player2.hit_points <= 0:
            self.attack.destroy()
            self.exit["text"] = "Exit"
            self.exit.grid(row=5, column=2, columnspan=2)
            if self.player1.hit_points <= 0:
                self.victor["text"] = str(self.player2.name) + ' is victorious!'
            else:
                self.victor["text"] = str(self.player1.name) + ' is victorious!'

        ''' This method is called when the user presses the "Attack" button.

            This method does the following:
            1) Calls the character.attack method for both the player and the computer.
            2) Updates the labels on the top right with the result of the attacks.
            3) Determines if there is a victor.
            4) If there is a victor, removes that Attack button and replaces it with an Exit button.     
        '''
        #
        # TO DO
        #

    def exit_clicked(self):
        ''' This method is called when the Exit button is clicked.
            It passes control back to the callback method. '''
        self.call_on_selected()




