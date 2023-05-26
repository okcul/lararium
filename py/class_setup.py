from random import randint

# outline of turn based combat
# priority system based on status effects
# players go first, then enemies
# different effects that are taken into account at the end of either each set of turns or each rotation (both player and enemy turns combined)

class BasePiece: 
	def __init__(self, name : str, hp : list, atk : int, status : int):
		self.name = name
		self.hp = hp
		self.atk = atk
		self.status = status

	def __str__(self):
		match self.status: # checks for status id in order to print actual status name instead of the id
			case 0:
				status_str = "Fine"
			case 1:
				status_str = "Poisoned"
		return f"Name: {self.name} \nHP: {self.hp} \nAtk: {self.atk} \nStatus: {status_str}"
	
	def attack(self, enemy):
		if self.status != 0:
			modifier = randint(-3, 3)
			enemy.hp[0] -= (self.atk + modifier)
			return f"{enemy.name} has taken {self.atk + modifier} damage from {self.name}!"
		else:
			return 0 # code for action failed, turn not used
	

class Player(BasePiece):
	def __init__(self, name : str, hp : list, atk : int, status : int, inventory : list, buff : int, level : list):
		super(BasePiece, self).__init__()
		self.name = name
		self.hp = hp
		self.atk = atk
		self.status = status
		self.inventory = inventory
		self.buff = buff
		self.level = level # index 0 is actual level, index 1 is exp needed to level up, index 2 is current exp

	def inspect(self, enemy):
		print(enemy)
		return 0 # code for action succeeded, turn not used
	
	def use_item(self):
		if len(self.inventory) != 0: # checks if there's actually anything in the inventory
			while True: # to prevent player from losing turn when using an item not in their inventory
				used_item = input("What item to use?")
				if used_item not in self.inventory:
					print("You don't have this item!")
				else:
					match used_item:
						case 'potion':
							self.hp[0] += 20
							self.inventory.remove('potion')
							return f"{self.name} has healed themselves by 20 HP!"
		else:
			return 0 # code for action failed, turn not used


class Enemy(BasePiece):
	def __init__(self, name : str, hp : list, atk : int, status : int):
		super(BasePiece, self).__init__()
		self.name = name
		self.hp = hp
		self.atk = atk
		self.status = status
	
	def empty(self):
		pass
