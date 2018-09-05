import random

# TODO: wir wollen truhe mit schlüssel

legende = {"." : "Boden",
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
	
	def __init__(x,y=0,z=0):
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
		self.hp = 250
		self.attack = 0.88
		self.defense = 0.33
		self.gold = 0
		self.keys = 0
		self.hunger = 0
		self.mindamage = 5
		self.maxdamage = 10

class Dragon(Monster):
	
	def overwrite(self):
		self.char = "D"
		self.hp = random.randint(300,500)
		self.defense = 0.05
		self.attack = 0.5
		self.mindamage = 10
		self.maxdamage = 20

class Bat(Monster):
	
	def overwrite(self):
		self.char = "B"
		self.hp = random.randint(2,7)
		self.defense = 0.6
		self.attack = 0.3
		self.mindamage = 0
		self.maxdamage = 3

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
		self.attack = 0.6
		self.mindamage = 25
		self.maxdamage = 35
		
class Maus(Monster):
	
	def overwrite(self):
		self.char = "!"
		self.hp = random.randint(1,10)
			
def strike (a, d):
	namea = a.__class__.__name__
	named = d.__class__.__name__
	r1 = random.random()
	print("{} stellt sich beim dumm an und haut daneben".format(namea))
	return
	r2 = random.random()
	if r2 < d.defense:
		print("{} schaff es meisterhaft auszuweichen".format(named))
		return
		damage = random.randint(a.mindamage, a.maxdamage)
		s.hp -= damage
		print("Treffer!{} erleidet {} Schaden und hat noch {} hp übrig.".format(named, damage ))


def battle(a,d):
	print("---- Strike ----")
	strike(a,d)
	if d.hp > 0:
		print("---- Counterstrike! ----")
		strike(d,a)

def kampf():
	print("ein Monster versperrt deinen Weg!")
	print("Du bekämfst das Monster")
	print("Piff!Paff! Autch!")
	# 10% chance 
	if random.random() < 0.5:
		print("du besiegst das Monster")
		return 0
	else:
		print("Das Monster verletz dich!")
		schaden = random.randint(100,200)
		return schaden
gold = 0
def game():
	
	hero = "@"
	dungeon = list("...M...h...t..M...§..k.M....§..M..$.d..M..b..k.t.")
	hx = 0
	hunger = 0
	gold = 0
	hp = 800
	keys = 0


	while True:
		for x, char in enumerate(dungeon):
			if x == hx:
				print(hero, end="")
			else:
				print(char, end="")
		print()
		command = input("hp: {} gold: {} hunger: {} keys {} >>>".format(hp,gold,hunger,keys))
		dx = 0
		if command == "a":
			#hx -= 1
			dx = -1
		if command == "d":
			#hx += 1 
			dx = 1
		if command == "aaa":
			#hx -= 2
			dx = -3
			hunger += 2
		if command == "ddd":
			#hx += 2
			dx = 3
			hunger += 2
		# --- Monster? ---
		if dungeon[hx+dx] == "M":
			damage = kampf()
			if damage == 0:
				dungeon[hx+dx] =  "."
			else:
				hp -= damage
				dx = 0
		# --- bewegung ---
		hx += dx
		# ----food clock ----
		hunger += 1
		# ----items ----
		if dungeon[hx] == "§":
			dungeon[hx] = "."
			print("Ohh..Eine Schlüssel! Aber wo ist die Truhe!")
			keys += 80
		# --- käse ---
		if dungeon[hx] == "k":
			dungeon[hx] = "."
			print("mmmmmm,ein guter Käse, wie lecker!")
			hunger -= random.randint(3,8)
		#---- gold ----
		if dungeon[hx] == "$":
			dungeon[hx] = "."
			print("oho, ein Haufen Gold!")
			gold += random.randint(10,20)
		# ---- diamant ----
		if dungeon[hx] == "d":
			dungeon[hx] = "."
			print("oho, ein Haufen Diamant!")
			gold += random.randint(40,50)
		# ----- burger ----
		if dungeon[hx] == "b":
			dungeon[hx] = "."
			print("mmmmmm,ein Haufen Burger, wie lecker!")
			hunger -= random.randint(12,15)
		# ----- heiltrank ----
		if dungeon[hx] == "h":
			dungeon[hx] = "."
			print("ein Heiltrank!")
			hp += random.randint(20,25)
		# ---- truhe -----
		if dungeon [hx] == "t":
			if keys < 1:
				print("Eine Truhe. Aber leider hast du keinen Schlüssel")
			else:
				print("Du öffnest die Truhe mit einem Schlüssel")
				keys -= 1
				dungeon[hx] = "."
				belohnung = random.choice("$hdk") #gold,heiltrank,käse
				menge = random.randint(4000,8000)
				print("In der Truhe findest Du {} stück {}!".format(menge, belohnung))
				if belohnung == "$":
					gold += menge 
				if belohnung == "h":
					hp += menge 
				if belohnung == "k":
					hunger -= menge
				
if __name__ == "__main__":		
	game()		
	
