#all objects
#IDIDIT1
import random
from battle_manager import Battle_Manager
import tkinter
import time
class Characters(object):
    def __init__(self,list1):
      #we can make inventory a list
      self.name = (list1[0])
      self.hp=int(list1[1])
      self.attck=int(list1[2])
      self.speed=int(list1[3])
      self.pic=(list1[4])


    def attack(self, enemy):
        total_dex = self.speed + enemy.speed
        hit_attempt = random.randrange(0, total_dex)
        if (hit_attempt <= self.speed):
            damage = random.randrange(0, self.attck)
            if (damage > enemy.hp) and ("Wand of Defence" in enemy.inventory):
                enemy.inventory.remove("Wand of Defence")
                result = enemy.name + " used the Wand of Defense! No damage is taken!"
                return result
            if (damage > enemy.hp) and ("mosnters stick" in enemy.inventory):
                enemy.inventory.remove("mosnters stick")
                result = enemy.name + " used the mosnters stick! No damage is taken!"
                return result
            else:
                enemy.hp -= damage
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
    def __init__(self,p):
        Characters.__init__(self,[p.name,p.hp,p.attck,p.speed,p.pic,])
        self.in_battle = False
        self.event = 0
        self.inventory = ["Potion", "Wand of Defence"]
        self.money=0
    def s_attack(self, enemy):
        total_dex = self.speed + enemy.speed
        hit_attempt = random.randrange(0, total_dex)
        if (hit_attempt <= self.speed) and "Light sword" in self.inventory:
            damage = random.randrange(0, self.attck)
            damage=damage*2
            enemy.hp -= damage
            result = self.name + " hits " + enemy.name + " causing " + str(damage) + " damage."
            return result

        elif (hit_attempt <= self.speed) and "Light sword" not in self.inventory:
            damage = random.randrange(0, self.attck)
            enemy.hp -= damage
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
                update="It was empty."
                return update
                #empty chest
            elif luck in [6,7,8,9,10,11,12]:
                self.event+=10
                if luck in [6,7]:
                    self.inventory.append("Potion")
                    update="You found a potion, it will heal 20 hp! It can even overheal!"
                    print(str(self.hp))
                    return update
                elif luck in [8]:
                    self.attck+=10
                    print(str(self.attck))
                    update="You found a potion of attack! You gain 10 attck!"
                    return update
                elif luck in [9]:
                    self.speed+=10
                    print(str(self.speed))
                    update="You found a potion of speed! You gain 10 speed!"
                    return update
                elif luck in [10, 11]:
                    self.inventory.append("Wand of Defence")
                    update="You found a wand of defence. It negates any damage! (One use)"
                    return update
                elif luck in [12]:
                    self.inventory.append("Light sword!")
                    update="Finally! You found the light sword! It multiplies your damage by 2!(passive)"
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
    def search1(self):
        if self.in_battle==True:
            update="You cannot search for loot in battle! Are you crazy?"
            return update
        else:
            luck=random.randint(1,14)
            #now we can make 1-5 empty, 6-12 loot of increasing value(6-8 low) (9-11 middle)(12-godlike), and 13-15......TRAPS!!!(insert evil laugh)
            if luck in [1,2,3,4,5]:
                update="the monster dropped nothing."
                return update
                #empty chest
            elif luck in [6,7,8,9,10,11,12,13,14]:
                if luck in [6,7]:
                    self.inventory.append("monster blood")
                    update="the monsters blood has healing properties it will heal you 20 hp!"
                    print(str(self.hp))
                    return update
                elif luck in [8]:
                    self.attck+=10
                    print(str(self.attck))
                    update="a strange sword on th monster increases your attack. You gain 10 attck!"
                    return update
                elif luck in [9]:
                    self.speed+=10
                    print(str(self.speed))
                    update="a strange relic on th monster increases your speed! You gain 10 speed!"
                    return update
                elif luck in [10, 11]:
                    self.inventory.append("mosnters stick")
                    update="the monster dropped a strange stick it casts a blue aura around you! (invincibilityy One use)"
                    return update
                elif luck in [12]:
                    self.inventory.append("Light sword!")
                    update="Finally! You found the light sword! It multiplies your damage by 2!(passive)"
                    return update
                elif luck in [13,14]:
                    p = random.randrange(1,10)
                    self.money+=p
                    update= "hey you found some shiny stuff maybe you can use it later"
                    return update

    def use_item(self, item):
        #might not be helpful
        self.update= ""
        if item=="Potion" or  item=="monster blood":
            if item == "Potion":
                self.inventory.remove("Potion")
            if item=="monster blood":
                self.inventory.remove("monster blood")
            self.hp+=20
            self.update='You healed 20 damage, your health is now'+str(self.hp)
        elif item=="Wand of Defence" or item=="monsters stick":
            self.update = "You should save that for battle."
        elif item == "Light sword!":
            self.update = "You swing the sword a little. It's pretty cool."
        elif item=="Strange Potion":
            x = random.randint(0,2)
            if x == 0:
                self.hp+=40
                self.update = 'You healed 40 damage, your health is now' + str(self.hp)
            elif x==1:
                self.hp-=35
                self.update="your stomach boils and churns its poison you lose 35 health your health is now"+str(self.hp)
            else:
                self.update= "nothing happened"
        return self.update

class EnemyList(object):
    def __init__(self, file_name):
        self.file_name = file_name
        self.load_chars()
    def load_chars(self):
        self.enemy_list = []

        text_file = open(self.file_name, "r")

        for line in text_file:
            line = line.strip()
            my_fields = line.split(", ")
            enemy = Characters(my_fields)
            self.enemy_list.append(enemy)

#includes bosses and bogies1
class Room(object):
  def __init__(self,you,da_boss,x,y,x1,y1):
      self.you=you
      self.library=EnemyList("All_DA_Enemies.txt")
      self.battle=Battle_Manager
      self.da_boss=da_boss
      self.x = x
      self.x1 = x1
      self.y1 = y1
      self.y = y
      self.spawn()
  def spawn(self):
        if self.x==self.x1 and self.y==self.y1:
            self.b = self.battle(self.you,self.da_boss)
        elif self.you.event > 40:
            self.battle(self.you, self.library.enemy_list[3])
        elif self.you.event > 30:
            self.battle(self.you, self.library.enemy_list[2])
        elif self.you.event>20:
            self.battle(self.you,self.library.enemy_list[1])
        elif self.you.event>10:
            self.battle(self.you,self.library.enemy_list[0])



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





# do we really need to make loot_crate an object? We can just make lists of treasure that get added to the players inventory
'''class Loot_crate(object):
  def __init(self, loot):
      self.loot=loot'''

  
#a box with potions and stuff

