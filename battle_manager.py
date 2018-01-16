import tkinter

#
# No changes are required in this file.
#

from screen_battle import Screen_Battle
from screen_prepare_to_battle import Screen_prepare_to_battle
from characters import CharacterList
class Battle_Manager (object):
    
    def __init__ (self,player,computer):
        '''
        Initializes a new battle manager by loading the list of characters from the file and
        by initializing tkinter.
        '''
        self.computer=computer
        self.player=player
        self.root = tkinter.Tk()
        self.onclose_character_selector()
#hi
    def onclose_character_selector (self):
        ''' This method is called when the Screen_character_selector closes. 
            selected_char should contain the index in the list of the character selected by the user. 
            The method manages the assignment of the player and computer objects and then starts the 
            Prepare for Battle page.
            '''
        self.root.title ("The Combatants!")
        
        # Creates the "Prepare to Battle" frame
        self.prepare = Screen_prepare_to_battle(self.root, self.player, self.computer, self.onclose_prepare_to_battle)
    
    def onclose_prepare_to_battle (self):
        ''' 
        This method is called when the user presses button on the Prepare to Battle screen.
        The method closes the current window and creates the battle window.
        '''
        # Destroy the "Prepare to Battle" frame.
        self.prepare.destroy()

        # Retitle the main frame.
        self.root.title ("Battle!")
    
        # Create the Battle frame
        self.battle_screen = Screen_Battle(self.root, self.player, self.computer, self.onclose_battle)
    def onclose_battle (self):
        ''' This method is called after the battle is over.  This method causes the program to exit. '''
        self.root.destroy()

    