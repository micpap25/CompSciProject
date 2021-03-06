import tkinter
import winsound
class Screen_prepare_to_battle (tkinter.Frame):
    def __init__ (self, master, player1, player2, call_on_next):
        super(Screen_prepare_to_battle, self).__init__(master)

        # Save player character object references
        self.player1 = player1
        self.player2 = player2
        
        # Save the method reference to which we return control after the player hits "Next"
        self.call_on_selected = call_on_next
        winsound.PlaySound('sound\The-Decisive-Battle-Final-Fantasy-VI-Music-Extended.wav', winsound.SND_ASYNC)
        self.grid()
        self.create_widgets()
#hi11
    
    def create_widgets (self):
        tkinter.Label(self,text="you").grid()
        print(self.player1.pic)
        imageSmall = tkinter.PhotoImage(file="Images2\\" + str(self.player1.pic),master=self)
        w = tkinter.Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=1, column=0)
        tkinter.Label(self, text="VS",font=30).grid(row=1, column=1)
        tkinter.Label(self, text="enemy").grid(row=0,column=2)
        imageSmall = tkinter.PhotoImage(file="Images2/" + self.player2.pic,master=self)
        w = tkinter.Label(self, image=imageSmall)
        w.photo = imageSmall
        w.grid(row=1, column=2)
        row1 =2
        column1=0
        for i in [self.player1,self.player2]:
            tkinter.Label(self,text= "health: " + str(i.hp)).grid(row=row1,column=column1)
            row1 +=1
            tkinter.Label(self, text= "strength: "+ str(i.attck)).grid(row=row1,column=column1)
            row1 += 1
            tkinter.Label(self, text="dexterity: " + str(i.speed)).grid(row=row1,column=column1)
            column1+=2
            row1=2
        self.next = tkinter.Button(self, text="To battle", command=self.continue_clicked,bg="red")
        self.next.grid(row=5,column=4)

        '''
        This method creates all of the widgets the prepare to battle page.
        '''
        #
        # TO DO
        #
 
    def continue_clicked(self):
        ''' This method is called when the Battle button is clicked. 
            It passes control back to the callback method. '''
        self.call_on_selected()
            
