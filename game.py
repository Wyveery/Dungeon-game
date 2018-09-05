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
		   "t" : "e"
	        }
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
		
	def overwrite(self):
		pass
		
class Player(Monster):
	
	def overwrite(self):
		self.char = "@"
		self.hp = 100
		self.attack = 0.9
		self.defense = 0.4
		self.gold = 0
		self.keys = 0
		self.hunger = -1000
		
		self.mindamage = 12
		self.maxdamage = 18
		self.prinzessin = 0

class Dragon(Monster):
	
	def overwrite(self):
		self.char = "D"
		self.hp = random.randint(200,300)
		self.defense = 0.05
		self.attack = 0.5
		self.mindamage = 2
		self.maxdamage = 4
		
class Bat(Monster):
	
	def overwrite(self):
		self.char = "B"
		self.hp = random.randint(10,20)
		self.defense = 0.6
		self.attack = 0.3
		self.mindamage = 10
		self.maxdamage = 10

class Goblin(Monster):
	
	def overwrite(self):
		self.char = "G"
		self.hp = random.randint(20,25)
		self.defense = 0.01
		self.attack = 0.5
		self.mindamage = 5
		self.maxdamage = 10

class Schlange(Monster):
	
	def overwrite(self):
		self.char = "S"
		self.hp = random.randint(2,4)
		self.defense = 0.4
		self.attack = 0.7
		self.mindamage = 25
		self.maxdamage = 35
		
class Topolino(Monster):
	
	def overwrite(self):
		self.char = "T"
		self.hp = random.randint(15,25)
		self.defense = 0.4
		self.attack = 0.4
		self.mindamage = 5
		self.maxdamage = 10
			
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
	hero = Player(0,0,0)
	level1 = list("pp_hh_ M_h__t____S__$__§_k__TT____T_t_S___M__B_____S___§__k__M__BB__§__M__$_d_M__b__k_SS t_D b_d")
	
	# ---- dungeon vorbereiten ----
	dungeon = []
	
	for x, char in enumerate(level1):
		if char == "M":
			dungeon.append("_")
			Monster(x)
		elif char == "D":
			dungeon.append("_")
			Dragon(x)
		elif char == "B":
			dungeon.append("_")
			Bat(x)
		elif char == "T":
			dungeon.append("_")
			Topolino(x)
		elif char == "G":
			dungeon.append("_")
			Goblin(x)
		elif char == "S":
			dungeon.append("_")
			Schlange(x)
		# ... noch mehr monster...
		else:
			dungeon.append(char)
				
	# --- Grafik engine ---	
		
	while hero.hp>0 and hero.hunger < 200:
		for x, char in enumerate(dungeon):
			for m in Monster.zoo:
				if m.x == x and m.hp > 0:
					print(m.char, end="")
					break
			else:
				print(char,end="")
			
		print()
		command = input("hp: {} gold: {} hunger: {} Prinzessin: {} keys {} >>>".format(hero.hp,hero.gold,hero.hunger,hero.prinzessin,hero.keys))
		
		dx = 0
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
		if command == "exit":
			break
		# --- Monster? ---
		for m in Monster.zoo:
			if m.number == 0:
				continue # player ist Moster number 0
			if m.hp < 1:
				continue
			if m.x == hero.x + dx:
				dx = 0
				battle(hero, m)
				break
		# --- bewegung ---
		hero.x += dx
		# ----food clock ----
		hero.hunger += 1
		# ----items ----
		if dungeon[hero.x] == "§":
			dungeon[hero.x] = "_"
			print("Ohh..Eine Schlüssel! Aber wo ist die Truhe!")
			hero.keys += 1
		# --- käse ---
		if dungeon[hero.x] == "k":
			dungeon[hero.x] = "_"
			print("mmmmmm,ein guter Käse, wie lecker!")
			hero.hunger -= random.randint(3,8)
		# --- Prinzessin ---
		if dungeon[hero.x] == "P":
			dungeon[hero.x] = "_"
			print("m,eine gute Prinzessin!")
			hero.prinzessin += 1
		#---- gold ----
		if dungeon[hero.x] == "$":
			dungeon[hero.x] = "_"
			print("oho, ein Haufen Gold!")
			hero.gold += random.randint(10,20)
		# ---- diamant ----
		if dungeon[hero.x] == "d":
			dungeon[hero.x] = "_"
			print("oho, ein Haufen Diamant!")
			hero.gold += random.randint(40,50)
		# ----- burger ----
		if dungeon[hero.x] == "b":
			dungeon[hero.x] = "_"
			print("mmmmmm,ein Haufen Burger, wie lecker!")
			hero.hunger -= random.randint(12,15)
		# ----- heiltrank ----
		if dungeon[hero.x] == "h":
			dungeon[hero.x] = "_"
			print("ein Heiltrank!")
			hero.hp += random.randint(20,25)
		# ---- truhe -----
		if dungeon [hero.x] == "t":
			if hero.keys < 1:
				print("Eine Truhe. Aber leider hast du keinen Schlüssel")
			else:
				print("Du öffnest die Truhe mit einem Schlüssel")
				hero.keys -= 1
				dungeon[hero.x] = "_"
				belohnung = random.choice("$hdkp") #gold,heiltrank,käse
				menge = random.randint(200,400)
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
	
