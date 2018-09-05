
import random

def kampf():
	print("ein Monster versperrt deinen Weg!")
	print("Du bekämfst das Monster")
	print("Piff!Paff! Autch!")
	# 10% chance 
	if random.random() < 0.1:
		print("du besiegst das Monster")
		return 0
	else:
		print("Das Monster verletz dich!")
		schaden = random.randint(1,10)
		return schaden
gold = 0
hero = "@"
dungeon = list("...M.d...M.h...k.d.M..$.d..M.h.b..k.d.")
hx = 0
hunger = 0
gold = 0
hp = 100

while True:
	for x, char in enumerate(dungeon):
		if x == hx:
			print(hero, end="")
		else:
			print(char, end="")
	print()
	command = input("hp: {} gold: {} hunger: {} >>>".format(hp,gold,hunger))
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
		hunger += 2
	if command == "dd":
		#hx += 2
		dx = 2
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
	
		
	
