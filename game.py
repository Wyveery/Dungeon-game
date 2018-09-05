import random

# TODO: wir wollen truhe mit schlüssel

legende = {"_" : "Boden",
           "k" : "Käse",
           "d" : "Diamant",
           "b" : "Burger",
           "M" : "Monster",
           "$" : "Gold",
           "h" : "Heiltrank",
           "§" : "Schlüssel",
           "t" : "Truhe",
           "#" : "Mauer",
           "<" : "Stiege rauf",
           ">" : "Stiege runter",
           }
           
level1 = """
##################################################
#>______________________________________________1#
#________________________________________________#
#_________________M______________________________#
##################################################"""


level2 = """
##################################################
#>_____________________B________________________2#
#________________________________________________#
#_________________M______________________________#
##################################################"""

level3 = """
##################################################
#<_____________________________D________________3#
#>__________________D____________________________#
#_______________________________M________________#
##################################################"""




class Monster():
    
    number = 0
    zoo = []
    
    def __init__(self,x,y=0,z=0):
        self.x = x
        self.y = y
        self.z = z
        self.char = "M"
        self.number = Monster.number
        Monster.number += 1
        Monster.zoo.append(self)
        self.hp = random.randint(10,20)
        self.attack = 0.7
        self.defense = 0.25
        self.overwrite()
        self.mindamage = 1       
        self.maxdamage = 10
        self.aggro = 80
        
    def overwrite(self):
        pass
        
    def move(self, player):
        # moving toward player?
        dx = 0 
        dy = 0
        distance = ((self.x-player.x)**2 + (self.y-player.y)**2)**0.5
        if distance < self.aggro:
            if self.x < player.x:
              dx = 1
            elif self.x > player.x:
                dx = -1
            if self.y < player.y:
                dy = 1
            elif self.y > player.y:
                dy = -1
            return dx, dy
        else:
            return self.ai()
    
    def ai(self):
        # random movement
        dx = random.choice((-1,0,0,0,1))
        dy = random.choice((-1,0,0,0,1))
        return dx, dy
 
            
        
class Player(Monster):
    
    def overwrite(self):
        self.char = "@"
        self.hp = 1000
        self.attack = 9
        self.defense = 9
        self.gold = 0
        self.keys = 0
        self.hunger = -10000
        self.mindamage = 100
        self.maxdamage = 1000
        self.prinzessin = 0

class Dragon(Monster):
    
    def overwrite(self):
        self.char = "D"
        self.hp = random.randint(200,300)
        self.defense = 0
        self.attack = 0
        self.mindamage = 0
        self.maxdamage = 0
        self.aggro = 9
        

        
class Bat(Monster):
    
    def overwrite(self):
        self.char = "B"
        self.hp = random.randint(50,80)
        self.defense = 0
        self.attack = 0
        self.mindamage = 0
        self.maxdamage = 0
        self.aggro = 9


class Goblin(Monster):
    
    def overwrite(self):
        self.char = "G"
        self.hp = random.randint(150,200)
        self.defense = 0
        self.attack = 0
        self.mindamage = 0
        self.maxdamage = 0
        self.aggro = 0

class Schlange(Monster):
    
    def overwrite(self):
        self.char = "S"
        self.hp = random.randint(50,100)
        self.defense = 0
        self.attack = 0
        self.mindamage = 0
        self.maxdamage = 0
        self.aggro = 9
        

        
class Topolino(Monster):
    
    def overwrite(self):
        self.char = "T"
        self.hp = random.randint(200,250)
        self.defense = 0
        self.attack = 0
        self.mindamage = 0
        self.maxdamage = 0
        self.aggro = 9
        

def strike (a, d):
    namea = a.__class__.__name__
    named = d.__class__.__name__
    print("{}  schlägt auf {}!".format(namea,named))
    r1 = random.random()
    if r1 > a.attack:
        print("{} stellt sich beim dumm an und haut daneben".format(namea))
        return
    r2 = random.random()
    if r2 < d.defense:
        print("{} schaff es meisterhaft auszuweichen".format(named))
        return
    damage = random.randint(a.mindamage, a.maxdamage)
    d.hp -= damage
    print("Treffer!{} erleidet {} Schaden und hat noch {} hp übrig.".format(named, damage, d.hp ))


def battle(a,d):
    print("---- Strike ----")
    strike(a,d)
    if d.hp > 0:
        print("---- Counterstrike! ----")
        strike(d,a)
gold = 0

def game(): 
    hero = Player(1,3,0)
    #level1 = list("________M_h__B_t__§______k__G_k___S___S___k___t___T___M__B___G__S___§__k__M__B___T_§__M_______d_M__b__k_S_ D_t__b_d")
    
    # ---- dungeon vorbereiten ----
    dungeon = []
    for z, a in enumerate((level1, level2, level3)):
        level = []
        for y, b in enumerate(a.splitlines()):
            line = []
            for x, c in enumerate(b):                
                char = c 
                if c == "M":
                    char = "_" # Boden
                    Monster(x,y,z)
                elif c == "B":
                    char = "_" 
                    Monster(x,y,z)
                elif c == "S":
                    char = "_" 
                    Monster(x,y,z)
                elif c == "T":
                    char = "_" 
                    Monster(x,y,z)
                elif c == "D":
                    char = "_" 
                    Monster(x,y,z)
                elif c == "D":
                    char = "_" 
                    Monster(x,y,z)
                elif c == "G":
                    char = "_" 
                    Monster(x,y,z)
                line.append(char)
            level.append(line)
        dungeon.append(level)
    # dungeon ist fertig
   
   
   
    # --- Grafik engine --- 
        
    while hero.hp>0 and hero.hunger < 200:
        #...
        for y,line in enumerate(dungeon[hero.z]):
            for x, char in enumerate(line):
                for m in Monster.zoo:
                    if m.z != hero.z or m.hp <1:
                        continue
                    if m.x == x and m.y == y:
                        print(m.char, end="")
                        break
            else:
                print(char, end = "")
            print() # zeilenende
        print()       # dungeon ende
        command = input("hp: {} gold: {} hunger: {} Prinzessin: {} keys {} >>>".format(hero.hp,hero.gold,hero.hunger,hero.prinzessin,hero.keys))
        
        dx = 0
        dy = 0
        if command == "a":
            #hx -= 1
            dx = -1
        if command == "d":
            #hx += 1 
            dx = 1
        if command == "aa":
            #hx -= 2
            dx = -2 
            hero.hunger += 2
        if command == "dd":
            #hx += 2
            dx = 2
            hero.hunger += 2
        if command == "w":
            dy -= 1
        if command == "s":
            dy += 1
        if command == "rauf" or command == "<":
            hero.z -= 1
            continue 
        if command == "runter" or command == ">":
            hero.z += 1
            continue
        if command == "exit":
            break
        if command == "hilfe" or command == "help":
            for z in legende:
                print(z, legende[z])
        # --- Monster? ---
        for m in Monster.zoo:
            if m.number == 0:
                continue # player ist Moster number 0
            if m.hp < 1:
                continue
            if m.z != hero.z:
                continue
            if m.x == hero.x + dx and m.y == heo.y +dy:
                dx = 0
                dy = 0
                battle(hero, m)
                break

        # --- bewegung ---
        hero.x += dx
        hero.y += dy
        # --- Monster bewegung ---
        for m in Monster.zoo:
            if m.number == 0 or m.hp < 1 or m.z != hero.z:
                continue
            dx, dy = m.move(hero)
            # versucht Monster in ein anderes Monster zu laufen?
            for m2 in Monster.zoo:
                if m2.number == m.number or m2.hp < 1 or m2.z != hero.z:
                    continue
                if m.x + dx == m2.x and m.y + dy == m2.y:
                    dx = 0
                    dy = 0
                    if m2.number == 0:
                        battle(m, m2)
            m.x += dx # das Monster bewegt sich!
            m.y += dy
        # ----food clock ----
        hero.hunger += 1
        # ----items ----
        if dungeon [hero.z][hero.y][hero.x]== "§":
            dungeon [hero.z][hero.y][hero.x] = "_"
            print("Ohh..Eine Schlüssel! Aber wo ist die Truhe!")
            hero.keys += 1
        # --- käse ---
        if dungeon[hero.z][hero.y][hero.x] == "k":
            dungeon [hero.z][hero.y][hero.x]== "_"
            print("mmmmmm,ein guter Käse, wie lecker!")
            hero.hunger -= random.randint(3,8)
        # --- Prinzessin ---
        if dungeon [hero.z][hero.y][hero.x]== "P":
            dungeon [hero.z][hero.y][hero.x]= "_"
            print("m,eine gute Prinzessin!")
            hero.prinzessin += 1
        #---- gold ----
        if dungeon [hero.z][hero.y][hero.x]== "$":
            dungeon [hero.z][hero.y][hero.x]= "_"
            print("oho, ein Haufen Gold!")
            hero.gold += random.randint(10,20)
        # ---- diamant ----
        if dungeon [hero.z][hero.y][hero.x]== "d":
            dungeon [hero.z][hero.y][hero.x]= "_"
            print("oho, ein Haufen Diamant!")
            hero.gold += random.randint(40,50)
        # ----- burger ----
        if dungeon [hero.z][hero.y][hero.x]== "b":
            dungeon [hero.z][hero.y][hero.x]= "_"
            print("mmmmmm,ein Haufen Burger, wie lecker!")
            hero.hunger -= random.randint(12,15)
        # ----- heiltrank ----
        if dungeon [hero.z][hero.y][hero.x]== "h":
            dungeon [hero.z][hero.y][hero.x]= "_"
            print("ein Heiltrank!")
            hero.hp += random.randint(20,25)
        # ---- truhe -----
        if dungeon [hero.z][hero.y][hero.x]== "t":
            if hero.keys < 1:
                print("Eine Truhe. Aber leider hast du keinen Schlüssel")
            else:
                print("Du öffnest die Truhe mit einem Schlüssel")
                hero.keys -= 1
                dungeon[hero.x] = "_"
                belohnung = random.choice("$hdkp") #gold,heiltrank,käse
                menge = random.randint(20,80)
                print("In der Truhe findest Du {} stück {}!".format(menge, belohnung))
                if belohnung == "$":
                    hero.gold += menge 
                if belohnung == "h":
                    hero.hp += menge 
                if belohnung == "p":
                    hero.hunger += menge
    
    # ---game over---
    print("** Game Over **")
    if hero.hunger >= 100:
        print("nächstes Mal mehr essen")
    if hero.hp <= 0:
        print("nächstes Mal besser kämpfen")
        
    # --- Auswertung ---
    print("Du hast folgende Monster besiegt:")
    menge = 0 
    friedhof = {}
    for m in Monster.zoo:
        if m.number == 0:
            continue
        if m.hp > 0:
            continue
        menge += 1
        if m.__class__.__name__ in friedhof:
            friedhof[m.__class__.__name__] += 1
        else:
            friedhof[m.__class__.__name__] = 1
    for name in friedhof:
        print(name, friedhof[name])
    print("Insgesamt hast Du {} Monster besiegt".format(menge)) 
    
if __name__ == "__main__":      
    game()      
    
