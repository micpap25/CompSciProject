#all objects
import random
class Characters(object):
  def __init__(self,hp,attck,speed,weapon,inventory, in_battle=False, event=0):
      #we can make inventory a list
      self.hp=hp
      self.attck=attck
      self.speed=speed
      self.weapon=weapon
      self.inventory=inventory
      self.in_battle=in_battle
      self.event=event

    def attack(self):
        if self.in_battle==False:
            update="You can not attack if you are not in battle!"
        else:
            #insert generic attack sequence

    def search(self):
        if self.in_battle==True:
            update="You cannot search for loot in battle! Are you crazy?"
        else:
            luck=random.randint(1,15)
            #now we can make 1-5 empty, 6-12 loot of increasing value(6-8 low) (9-11 middle)(12-godlike), and 13-15......TRAPS!!!(insert evil laugh)
            if luck in [1,2,3,4,5]:
                self.event+=10
                #empty chest
            elif luck in [6,7,8,9,10,11,12]:
                self.event+=10

            elif luck in [13,14,15]:
                if luck==13:
                    trap=20
                    self.event += trap
                elif luck==14:
                    trap=25
                    self.event += trap
                elif luck==15:
                    trap=0
                    self.event+=trap
                #TRAAAAAPPPSSSS!!! YAYAYAYAYYAYAY

    def move(self):
        if self.in_battle==False:
            #sooooo, hoz dis gonna work?

#includes bosses and bogies
class Room(object):
  def __init__(self,doors,you,loot=0,bogies=0,bos=0):
      self.doors=doors
      self.you=you
      self.loot=loot
      self.bogies=bogies
      self.boss=bos

#includes all charachters and loot as well as doors


#do we really need to make loot_crate an object? We can just make lists of treasure that get added to the players inventory
class loot_crate(object):
  def __init(self, loot):
      self.loot=loot

  
#a box with potions and stuff
