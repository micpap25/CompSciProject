#all objects
import random
class Characters(object):
    def __init__(self,name,hp,attck,speed, picture):
      #we can make inventory a list

      self.hp=hp
      self.attck=attck
      self.speed=speed
      self.name=name
      self.pic=picture


    def attack(self, enemy):
        total_dex = self.speed + enemy.speed
        hit_attempt = random.randrange(0, total_dex)
        if (hit_attempt <= self.speed):
            damage = random.randrange(0, self.attck)
            enemy.hit_points -= damage
            result = self.name + " hits " + enemy.name + " causing " + str(damage) + " damage."
            return result
        else:
            result = self.name + " misses " + enemy.name + "."

            return result
            #insert generic attack sequence

    def die(self):
        if self.hp<=0:
            print("I'm sorry, I couldn't make it....(dies) ")

#hi
class Player(Characters):
    def __init__(self,master):
        super(Characters,self).__init__(master)
        self.in_battle = False
        self.event = 0
        self.inventory = []

    def s_attack(self, enemy):
        total_dex = self.speed + enemy.speed
        hit_attempt = random.randrange(0, total_dex)
        if (hit_attempt <= self.speed) and "Light sword" in self.inventory:
            damage = random.randrange(0, self.attck)
            damage=damage*2
            enemy.hit_points -= damage
            result = self.name + " hits " + enemy.name + " causing " + str(damage) + " damage."
            return result

        elif (hit_attempt <= self.speed) and "Light sword" not in self.inventory:
            damage = random.randrange(0, self.attck)
            enemy.hit_points -= damage
            result = self.name + " hits " + enemy.name + " causing " + str(damage) + " damage."
            return result
        else:
            result = self.name + " misses " + enemy.name + "."

            return result

    def search(self):
        if self.in_battle==True:
            update="You cannot search for loot in battle! Are you crazy?"
            return update
        else:
            luck=random.randint(1,15)
            #now we can make 1-5 empty, 6-12 loot of increasing value(6-8 low) (9-11 middle)(12-godlike), and 13-15......TRAPS!!!(insert evil laugh)
            if luck in [1,2,3,4,5]:
                self.event+=10
                update="It was empty"
                return update
                #empty chest
            elif luck in [6,7,8,9,10,11,12]:
                self.event+=10
                if luck in [6,7]:
                    self.inventory.append("Potion")
                    update="You found a potion, it will heal 20 hp! It can even overheal!"
                    return update
                elif luck in [8]:
                    self.attck+=10
                    update="You found a potion of attack! You gain 10 attck!"
                    return update
                elif luck in [9]:
                    self.speed+=10
                    update="You found a potion of speed! You gain 10 speed!"
                    return update
                elif luck in [10, 11]:
                    self.inventory.append("Wand of Defence")
                    update="You found a wand of defence. It negates any damage! (One use)"
                    return update
                elif luck in [12]:
                    self.inventory.append("Light sword!")
                    update="Finnaly! You found the light sword! It multiplies your damage by 2!(passive)"
                    return update

            elif luck in [13,14,15]:
                if luck==13:
                    trap=20
                    self.event += trap
                    update='You triggered a trap! A siren wails.'
                    return update
                elif luck==14:
                    trap=25
                    self.event += trap
                    update="You triggered a trap! A door glows bright red."
                    return update
                elif luck==15:
                    trap=0
                    self.event+=trap
                    self.hp-=25
                    update='Ouch! You stepped on a spike!'
                    return update

    def use_item(self, item):
        if item in self.inventory:
            if item=="Potion":
                self.inventory.remove("Potion")
                self.hp+=20
                update='You healed 20 damage, your health is now'+str(self.hp)
                return update

        else:
            update="You don't have that item."
            return update




#includes bosses and bogies
class Room(object):
  def __init__(self,doors,you,charlist,loot=0,vertPos=0,horiPos=0):
      self.doors=doors
      self.you=you
      self.loot=loot
      self.library=charlist
      self.vertPos=vertPos
      self.horiPos=horiPos

class charlist(object):
    def __init__(self,file):
        self.dict={}
        self.file=file
    def read(self):
        filename=open(self.file,"r")
        for l in filename:
            l.strip()
            p = l.split(", ")
            self.dict[p[0]]= p
#



# do we really need to make loot_crate an object? We can just make lists of treasure that get added to the players inventory
'''class Loot_crate(object):
  def __init(self, loot):
      self.loot=loot'''

  
#a box with potions and stuff
