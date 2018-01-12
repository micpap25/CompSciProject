import tkinter
import random
class Screen_Battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, call_on_next):
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
        
    def create_widgets (self):
        tkinter.Label(self, text="you").grid()
        imageSmall = tkinter.PhotoImage(file="images/" + self.player1.small_image)
        w = tkinter.Label(self,
                          image=imageSmall,
                          )
        w.photo = imageSmall
        w.grid(row=1, column=0)
        tkinter.Label(self, text="VS", font=30).grid(row=1, column=1)
        tkinter.Label(self, text="enemy").grid(row=0, column=2)
        imageSmall = tkinter.PhotoImage(file="images/" + self.player2.small_image)
        w = tkinter.Label(self,
                          image=imageSmall,
                          )
        w.photo = imageSmall

        w.grid(row=1, column=2)
        tkinter.Label(self, text="health: " + str(self.player1.hit_points)+"/"+ str(self.player1_max_hp)).grid(row=2, column=0)
        tkinter.Label(self, text="health: " + str(self.player2.hit_points) + "/" + str(self.player2_max_hp)).grid(row=2,column=2)
        self.next = tkinter.Button(self, text="Attack", command=self.attack_clicked, bg="red")
        self.next.grid(row=5, column=4)


        self.end=tkinter.Button(self,text="END",command=self.exit_clicked)
        '''
        This method creates all of the widgets for the battle page.
        '''
        #
        # TO DO
        #
        
    def attack_clicked(self):
        battle=random.randrange(0,1)
        if battle ==0:
            self.player1.attack(self.player2)
            self.player2.attack(self.player1)
        if battle == 1:
            self.player2.attack(self.player1)
            self.player1.attack(self.player2)
        if self.player1.hit_points<=0 or self.player2.hit_points<=0:
            if self.player1.hit_points<=0 and self.player2.hit_points<=0:
                tkinter.Label(self,text="It is a tie", font=30).grid(column=1)
                self.end.grid(column=3)
                self.next.destroy()
            elif self.player2.hit_points<=0:
                tkinter.Label(self,text="DEAD",font=30).grid(row=1,column=2)
                tkinter.Label(self,text="You win", font=30).grid(column=1)
                self.end.grid(column=3)
                self.next.destroy()
            elif self.player1.hit_points <=0:
                tkinter.Label(self, text="DEAD", font=30).grid(row=1, column=0)
                tkinter.Label(self, text="You lose", font=30).grid(column=1)
                self.end.grid(column=3)
                self.next.destroy()

        tkinter.Label(self, text="health: " + str(self.player1.hit_points) + "/" + str(self.player1_max_hp)).grid(row=2,column=0)
        tkinter.Label(self, text="health: " + str(self.player2.hit_points) + "/" + str(self.player2_max_hp)).grid(row=2,column=2)
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
  
            
            
            
            