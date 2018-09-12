import random

# TODO: box with key

legende = {"." : "floor", 
           "f" : "food",
           "M" : "Monster",
           "$" : "Gold",
           "h" : "healing potion",
           "k" : "key",
           "b" : "box",
           "*" : "flower",
           "#" : "wall",
           "<" : "Stair up",
           ">" : "Stair down",
           }

level1 = """
###################################
#>.......#........M......P.......1#
#....*...d..f............M........#
#k.......#........M...............#
###################################"""

level2 = """
###################################
#<...............B...............2#
#>................................#
#..............M..................#
###################################"""

level3 = """
###################################
#<......#..d.......d.............3#
#>......####.......#..........D...#
#......M..k........#.............k#
###################################"""





            
class Monster():
    number = 0
    zoo = []
    
    def __init__(self, x, y=0, z=0):
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
        self.mindamage = 1
        self.maxdamage = 3
        self.aggro = 3
        self.overwrite()
        
        
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
        self.hp = 250
        self.attack = 0.88
        self.defense = 0.33
        self.gold = 0
        self.keys = 0
        self.hunger = 0
        self.mindamage = 1
        self.maxdamage = 10
        self.flowers = 0
        self.happyend = False
        
        
class Dragon(Monster):
    
    def overwrite(self):
        self.char = "D"
        self.hp = random.randint(300,500)
        self.defense = 0.05
        self.attack = 0.5
        self.mindamage = 10
        self.maxdamage = 20
        self.aggro = 2
    
class Princess(Monster):
    
    def overwrite(self):
        self.char = "P"
        self.attack = 0.1
        self.mindamage = 1
        self.maxdamage = 1
        self.aggro = 2
        self.defense = 0.1
        
    def ai(self):
        # random movement
        dx = random.choice((-1,0,0,0,0,0,0,0,0,0,0,1))
        dy = random.choice((-1,0,0,0,0,0,0,0,0,0,0,1))
        return dx, dy
        
        
class Bat(Monster):
    
    def overwrite(self):
        self.char = "B"
        self.hp = random.randint(2, 7)
        self.defense = 0.6
        self.attack = 0.3
        self.mindamage = 0
        self.maxdamage = 3
        self.aggro = 5
    
    def ai(self):
        # random movement
        dx = random.choice((-2,-1,0,1,2))
        dy = random.choice((-2,-1,0,1,2))
        return dx, dy
        
  
        
def strike(a, d):
    namea = a.__class__.__name__
    named = d.__class__.__name__
    if named == "Princess":
        if a.flowers < 1:
            a.hp -= 1
            print("The princess hits you because you are not a gentleman.You need a flower!")
            return
        else:
            a.flowers -= 1
            print("You win!")
            a.happyend = True
            return
    print("{} is hitting {}!".format(namea, named))
    r1 = random.random()
    if r1 > a.attack:
        print("{} fails to attack".format(
              namea))
        return
    r2 = random.random()
    if r2 < d.defense:
        print("{} dodges the attack".format(
              named))
        return
    damage = random.randint(a.mindamage, a.maxdamage)
    d.hp -= damage
    print("Hit! {} takes {} damage and has  {} hp left.".format(
          named, damage, d.hp))
    if d.hp <= 0:
        print("{} wins vs  {}".format(namea, named))
 

def battle(a, d):
    print("---- Strike! -----")
    strike(a, d)
    if d.hp > 0:
        print("----Counterstrike! -----")
        strike( d, a)

def game():
    hero = Player(1,3,0)
    # ---- dungeon prepare ----
    dungeon = []
    for z, a in enumerate((level1, level2, level3)):
        level = []
        for y, b in enumerate(a.splitlines()):
            line = []
            for x, c in enumerate(b):
                char = c
                if c == "M":
                    char = "." # floor
                    Monster(x,y,z)
                elif c == "B":
                    char = "." 
                    Bat(x,y,z)
                elif c == "P":
                    char = "."
                    Princess(x,y,z)
                elif c == "D":
                    char = "."
                    Dragon(x,y,z)
                if char == ".":
                    # floor mit casualcheese?
                    # cheese chancs  20% -> 0.2
                    if random.random() < 0.05:
                        char = "f"
                    if random.random() < 0.:
                        char = "$"   
                line.append(char)
            level.append(line)
        dungeon.append(level)
    # dungeon is ready
                

    # --- Graphic engine----
    while hero.hp>0 and hero.hunger < 100 and not hero.happyend:
        # ...
        for y, line in enumerate(dungeon[hero.z]):
            for x, char in enumerate(line):
                for m in Monster.zoo:
                    if m.z != hero.z or m.hp <1:
                        continue
                    if m.x == x and m.y ==y:
                        print(m.char, end="")
                        break
                else:
                    print(char, end="")
            print() # line-end
        print()     # dungeon end
        command = input("hp: {} gold: {} hunger: {} keys: {} flowers: {} >>>".format(
                         hero.hp, hero.gold, hero.hunger, hero.keys, hero.flowers))
        dx = 0
        dy = 0
        if command == "a":
            dx = -1
        if command == "d":
            dx = 1
        if command == "w":
            dy = -1
        if command == "s":
            dy = 1
        # treppen
        if command == "up" or command == "<":
            if hero.z == 0:
                print("you are at the highest floor already")
            elif dungeon[hero.z][hero.y][hero.x] == "<":
                hero.z -= 1
                continue
            else:
                print("you must find a stair up (<)")
        
        if command == "down" or command == ">":
            if hero.z == len(dungeon)-1:
                print("you are at the lowest floor already")
            elif dungeon[hero.z][hero.y][hero.x] == ">":
                hero.z += 1
                continue
            else:
                print("you must find a stair down(>)")
        
        if command == "exit" or command == "quit" or command == "i don´t want to play any more":
            break
        if command == "help" or command == "?":
            for z in legende:
                print(z, "........", legende[z])    
        # --- Monster? ---
        for m in Monster.zoo:
            if m.number == 0:
                continue  # player ist Monster number 0
            if m.hp < 1:
                continue
            if m.z != hero.z:
                continue 
            if m.x == hero.x + dx and m.y == hero.y + dy:
                dx = 0
                dy = 0
                battle(hero, m)
                break
        # --- wall ? ----
        if dungeon[hero.z][hero.y+dy][hero.x+dx] == "#":
            print("ouch, a wall!")
            dx = 0
            dy = 0
        # ---- door ? ----
        if dungeon[hero.z][hero.y+dy][hero.x+dx] == "d":
            if hero.keys < 1:
                print("closed door: find a key (k)!")
                dx = 0
                dy = 0
            else:
                hero.keys -= 1
                print("you heroically used a key to open the door")
                dungeon[hero.z][hero.y+dy][hero.x+dx] = "."
        # --- moving-hero ---
        hero.x += dx
        hero.y += dy
        # ---- moving-monsters----
        for m in Monster.zoo:
            if m.number ==0 or m.hp <1 or m.z != hero.z:
                continue
            dx, dy = m.move(hero)
            # tries the monster to escape the dungeon?
            dest = "."
            try:
                dest = dungeon[hero.z][m.y+dy][m.x+dx]
            except:
                dx = 0
                dy = 0
            if dest in "#d":   # wall or door?
                dx = 0
                dy = 0
            # tries monster to run into other monster?
            for m2 in Monster.zoo:
                if m2.number == m.number or m2.hp <1 or m2.z != hero.z:
                    continue
                if m.x + dx == m2.x and m.y + dy == m2.y:
                    dx = 0
                    dy = 0
                    if m2.number == 0:
                        battle(m, m2)
            m.x += dx # the monster moves!
            m.y += dy
        # ----food clock ----
        hero.hunger += 1
        # ----- items -----
        # --- cheese ---
        if dungeon[hero.z][hero.y][hero.x] == "f":
            dungeon[hero.z][hero.y][hero.x] = "."   
            print("yummi cheese,")
            hero.hunger -= random.randint(3,8) 
        # --- flowers ---
        if dungeon[hero.z][hero.y][hero.x] == "*":
            dungeon[hero.z][hero.y][hero.x] = "."   
            print("oh, a flower! I need to find a princess!")
            hero.flowers += 1 
        #---gold---
        if dungeon[hero.z][hero.y][hero.x] == "$":
            dungeon[hero.z][hero.y][hero.x] = "."
            print("oho, I am rich!")
            hero.gold += random.randint(10,20)
        # --- healing potion ----
        if dungeon[hero.z][hero.y][hero.x] == "h":
            dungeon[hero.z][hero.y][hero.x] = "."
            print("a healing potion")
            hero.hp += random.randint(20,25)
        # ---- key----
        if dungeon[hero.z][hero.y][hero.x] == "k":
            dungeon[hero.z][hero.y][hero.x] = "." 
            print("oh, a key")
            hero.keys += 1
        # --- box ----
        if dungeon[hero.z][hero.y][hero.x] == "b":
            if hero.keys < 1:
                print("a locked box, where is the key?")
            else:
                print("you open the box with a key")
                hero.keys -= 1
                dungeon[hero.x] = "."
                bounty = random.choice("$hf") # gold, healing potion, food
                amount = random.randint(10,25)
                print("Hurra, In the box you find {} pieces of {}!".format(
                      menge, legende[bounty]))
                if bounty == "$":
                    hero.gold += amount
                if bounty == "h":
                    hero.hp += amount
                if bounty == "f":
                    hero.hunger -= amount
    
    # --- game over ---
    print("*-*-*-*-*-*- Game Over -*-*-*-*-*-*-*-*")
    if hero.hunger >= 100:
        print("the next time eat more cheese!")
    if hero.hp < 1:
        print("the next time fight better!")
   
    # --- score ----
    print("you killed those monsters:")
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
    print(" total kills: {} ".format(menge))
    if hero.happyend and not hero.hunger < 0 and not hero.hunger > 199:
            print("* - * - * - * - * - * - * - * - * - * - * ")
            print("The Princessin accept the flower and she married the hero") 
            print("You win!")
            print("* - * - * - * - * - * - * - * - * - * - * ")
if __name__ == "__main__":
    game()                
                
        
        
            
