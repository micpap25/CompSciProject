#all objects
class characters(object):
  def __init__(self,hp,attck,speed,weapon,inventory):
      #we can make inventory a list
      self.hp=hp
      self.attck=attck
      self.speed=speed
      self.weapon=weapon
      self.inventory=inventory
#includes bosses and bogies
class room(object):
  def __init__(self,doors,you,loot=0,bogies=0,bos=0):
      self.doors=doors
      self.you=you
      self.loot=loot
      self.bogies=bogies
      self.boss=boss
#includes all charachters and loot as well as doors

class loot_crate(object):
  def __init(self, loot):
      self.loot=loot
  
#a box with potions and stuff
