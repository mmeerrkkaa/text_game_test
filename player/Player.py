from player.Inventory import Inventory


class Player:

	def __init__(self, name):
		self.name = name

		self.max_health = 100
		self.health = self.max_health

		self.damage = 1
		self.defense = 1

		self.inventory = Inventory()

		self.lvl = 1
		self.exp = 0
		self.max_exp = 100

		self.money = 0

		self.floor = None

	def add_exp(self, exp: int) -> bool:
		""" Добавляет опыт игроку, если опыт достигает максимального, то игрок повышается на уровень """
		self.exp += exp
		if self.exp >= self.max_exp:
			self.exp -= self.max_exp
			self.lvl += 1
			self.max_exp *= 1.5
			self.max_health += 10
			self.health = self.max_health
			self.damage += 1
			self.defense += 1
			return True
		return False

	def add_lvl(self, lvl: int):
		""" Добавляет уровень игроку """
		self.lvl += lvl
		self.max_exp *= 1.5 * lvl
		self.max_health += 10 * lvl
		self.health = self.max_health
		self.damage += 1 * lvl
		self.defense += 1 * lvl

	def remove_lvl(self, lvl: int):
		""" Убирает уровень игроку """
		self.lvl -= lvl
		self.max_exp /= 1.5 * lvl
		self.max_health -= 10 * lvl
		self.health = self.max_health
		self.damage -= 1 * lvl
		self.defense -= 1 * lvl

	def add_money(self, money: int):
		self.money += money

	def remove_money(self, money):
		self.money -= money

	def use_item_heal_potion(self):
		"""Использует предмет из инвентаря - зелье восстановления здоровья"""
		item = self.inventory.get_item('heal_potion')		# возможно стоит heal_potion передавать на вход метода
		#Если метод get_item() выдаст ошибку не знаю что будет. Прервется ли выполнение метода и пойдет
		# отловка ошибок которая скажет игроку о том что у него нет такого предмета?
		self.health += self.max_health*0.2		# зелье лечения восстанавливает 20% общего запаса здоровья
		if self.health > self.max_health:
			self.health = self.max_health
		self.inventory.remove_item(item)

	def test_felix(self):
		self.health = self.health





