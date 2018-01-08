#all objects
import random
class Player(object):
    def __init__(self,name,hp,attck,speed, picture, in_battle=False, event=0, horiPos = 0, vertPos = 0,):
      #we can make inventory a list

      self.hp=hp
      self.attck=attck
      self.speed=speed

      self.inventory=[]
      self.in_battle=in_battle
      self.event=event
      self.name=name
      self.horiPos = horiPos
      self.vertPos = vertPos
      self.picture=picture
      self.character_shape="Images\images.png"

    def attack(self, enemy):
        if self.in_battle==False:
            return "You can not attack if you are not in battle!"
        else:
            total_dex = self.speed + enemy.speed
            hit_attempt = random.randrange(0, total_dex)
            if (hit_attempt <= self.speed):
                damage = random.randrange(0, self.attck)
                enemy.hit_points -= damage
                result = self.name + " hits " + enemy.name + " causing " + str(damage) + " damage."
            else:
                result = self.name + " misses " + enemy.name + "."

            return result
            #insert generic attack sequence

    def die(self):
        if self.hp<=0:
            return ("I'm sorry, I couldn't beat it....(dies) ")


    def search(self):
        if self.in_battle==True:
            update="You cannot search for loot in battle! Are you crazy?"
            return update
        else:
            luck=random.randint(1,15)
            #now we can make 1-5 empty, 6-12 loot of increasing value(6-8 low) (9-11 middle)(12-godlike), and 13-15......TRAPS!!!(insert evil laugh)
            if luck in [1,2,3,4,5]:
                self.event+=10
                update="It was empty, better keep moving or something will come."
                return update
            elif luck in [6,7,8,9,10,11,12]:
                self.event+=10

            elif luck in [13,14,15]:
                if luck==13:
                    trap=20
                    self.event += trap
                    update="You triggered a trap! A bell sound rings through the air"
                    return update
                elif luck==14:
                    trap=25
                    self.event += trap
                    update="You triggered a trap! A sticky smell fills the air, you here a growl in the distance."
                    return update
                elif luck==15:
                    trap=10
                    self.event+=trap
                    self.hp-=30
                    update="You stepped on a spike! OUCH!"
                    return update


    def use_item(self):
        if self.in_battle==True:
            if "amor"


    def moveAround(self, direction):
        if direction == "N":
            self.vertPos += 1
        elif direction == "E":
            self.horiPos += 1
        elif direction == "S":
            self.vertPos -= 1
        elif direction == "W":
            self.horiPos-=1



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
class Loot_crate(object):
  def __init(self, loot):
      self.loot=loot

  
#a box with potions and stuff
