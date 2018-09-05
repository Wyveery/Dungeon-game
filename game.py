import random

# TODO: truhe mit schlüssel

legende = {"." : "Boden",
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
###################################
#>..........#....................1#
#...........d....k................#
#§..........#...........M.........#
###################################"""

level2 = """
###################################
#<...............B...............2#
#>................................#
#..............M..................#
###################################"""

level3 = """
###################################
#<...............................3#
#>................D...............#
#.................................#
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


class Dragon(Monster):

    def overwrite(self):
        self.char = "D"
        self.hp = random.randint(200,250)
        self.defense = 0.05
        self.attack = 0.5
        self.mindamage = 10
        self.maxdamage = 20
        self.aggro = 2



class Bat(Monster):

    def overwrite(self):
        self.char = "B"
        self.hp = random.randint(2, 7)
        self.defense = 0.6
        self.attack = 0.3
        self.mindamage = 0
        self.maxdamage = 3
        self.aggro = 5



def strike(a, d):
    namea = a.__class__.__name__
    named = d.__class__.__name__
    print("{} schlägt auf {}!".format(namea, named))
    r1 = random.random()
    if r1 > a.attack:
        print("{} stellt sich dumm an und haut daneben".format(
              namea))
        return
    r2 = random.random()
    if r2 < d.defense:
        print("{} schaff es meisterhaft auszuweichen".format(
              named))
        return
    damage = random.randint(a.mindamage, a.maxdamage)
    d.hp -= damage
    print("Treffer! {} erleidet {} Schaden und hat noch {} hp übrig.".format(
          named, damage, d.hp))
    if d.hp <= 0:
        print("{} besiegt {}".format(namea, named))


def battle(a, d):
    print("---- Strike! -----")
    strike(a, d)
    if d.hp > 0:
        print("----Counterstrike! -----")
        strike( d, a)



def game():
    hero = Player(1,3,0)
    #level1 = "..k...t.....$..BB...kk...§...k....k.h.h.M..h.h.D"

    # ---- dungeon vorbereiten ----
    dungeon = []
    for z, a in enumerate((level1, level2, level3)):
        level = []
        for y, b in enumerate(a.splitlines()):
            line = []
            for x, c in enumerate(b):
                char = c
                if c == "M":
                    char = "." # Boden
                    Monster(x,y,z)
                elif c == "B":
                    char = "."
                    Bat(x,y,z)
                elif c == "D":
                    char = "."
                    Dragon(x,y,z)
                if char == ".":
                    # bodenplatte mit zufallskäse?
                    # käsewahrscheinlichkeit 20% -> 0.2
                    if random.random() < 0.03:
                        char = "k"
                    if random.random() < 0.05:
                        char = "h"
                line.append(char)
            level.append(line)
        dungeon.append(level)
    # dungeon ist fertig


    # --- Grafik engine ----
    while hero.hp>0 and hero.hunger < 150:
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
            print() # zeilenende
        print()     # dungeon ende
        command = input("hp: {} gold: {} hunger: {} keys: {} >>>".format(
                         hero.hp, hero.gold, hero.hunger, hero.keys))
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
        if command == "rauf" or command == "<":
            if hero.z == 0:
                print("du bist schon in der obersten Stock!")
            elif dungeon[hero.z][hero.y][hero.z] == "<":
                hero.z -= 1
                continue
            else:
                print("Du musst eine Stiege nach oben finden (<)")

        if command == "runter" or command == ">":
            if dungeon [hero.z][hero.y][hero.z] == ">":
                hero.z += 1
                continue
            else:
                print("Du musst eine Stiege nach unten finden (>)")

        if command == "exit" or command == "quit" or command == "ich will nicht mehr spielen":
            break
        if command == "hilfe" or command == "?":
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
        # --- wand ? ---
        if dungeon[hero.z][hero.y + dy][hero.x + dx] == "#":
            print("autsch, eine Wand!")
            dx = 0
            dy = 0
        # --- türe ---
        if dungeon[hero.z][hero.y + dy][hero.x + dx] == "d":
            if hero.keys < 1:
                print("verschlossene Türe. Finde Schlüssel(§)!")
                dx = 0
                dy = 0
            else:
                hero.keys -= 1
                dungeon[hero.z][hero.y + dy][hero.x + dx] = "."
                print("Türe heldenhaft aufgesperrt mit schlüssel")
        # --- bewegung ---
        hero.x += dx
        hero.y += dy
        # ---- Monster Bewegung ----
        for m in Monster.zoo:
            if m.number ==0 or m.hp <1 or m.z != hero.z:
                continue
            dx, dy = m.move(hero)
            # versucht Monster in Wand oder Türe zu laufen?
            if dungeon[hero.z][m.y + dy][m.x + dx] in "#d":
                dx = 0
                dy = 0
            # versucht Monster in ein anderes Monster zu laufen?
            for m2 in Monster.zoo:
                if m2.number == m.number or m2.hp <1 or m2.z != hero.z:
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
        # ----- items -----
        # --- käse ---
        if dungeon[hero.z][hero.y][hero.x] == "k":
            dungeon[hero.z][hero.y][hero.x] = "."
            print("mmmmmm, ein guter Käse, wie lecker!")
            hero.hunger -= random.randint(3,8)
        #---gold---
        if dungeon[hero.z][hero.y][hero.x] == "$":
            dungeon[hero.z][hero.y][hero.x] = "."
            print("oho, ein Haufen Gold, ich bin reich!")
            hero.gold += random.randint(10,20)
        # --- heiltrank ----
        if dungeon[hero.z][hero.y][hero.x] == "h":
            dungeon[hero.z][hero.y][hero.x] = "."
            print("ein Heiltrank!")
            hero.hp += random.randint(20,25)
        # ---- schlüssel ----
        if dungeon[hero.z][hero.y][hero.x] == "§":
            dungeon[hero.z][hero.y][hero.x] = "."
            print("oh ein Schlüssel! Aber wo ist die Truhe?")
            hero.keys += 1
        # --- truhe ----
        if dungeon[hero.z][hero.y][hero.x] == "t":
            if hero.keys < 1:
                print("eine Truhe. Aber leider hast du keinen Schlüssel")
            else:
                print("Du öffnest die Truhe mit einem Schlüssel")
                hero.keys -= 1
                dungeon[hero.x] = "."
                belohnung = random.choice("$hk") # gold, heiltrank, käse
                menge = random.randint(10,25)
                print("Hurra, In der Truhe findest Du {} stück {}!".format(
                      menge, legende[belohnung]))
                if belohnung == "$":
                    hero.gold += menge
                if belohnung == "h":
                    hero.hp += menge
                if belohnung == "k":
                    hero.hunger -= menge

    # --- game over ---
    print("*-*-*-*-*-*- Game Over -*-*-*-*-*-*-*-*")
    if hero.hunger >= 150:
        print("nächstes Mal mehr essen!")
    if hero.hp < 1:
        print("nächstes Mal besser kämpfen")

    # --- Auswertung ----
    print("Du hast folgende Monster besiegt")
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
    print(" insgesamt hast Du {} Monster besiegt".format(menge))


if __name__ == "__main__":
    game()




