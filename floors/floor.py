


class Floor:
	def __init__(self, floor_number: int, type: str = "Враг", enemies_name: list = ['Гоблин'], items: list = ["Камень"]):
		self.type = type # Тип этажа. Враг, Магазин, Сундук
		self.floor_number = floor_number
		self.enemies_name = enemies_name
		self.items = {}
		for item in items:
			self.items[item] = {"chance": 100}

		self.visits = 0

	def start_floor(self):
		self.visits += 1
		if self.type == "Враг":
			# Запускаем бой
			pass
		elif self.type == "Магазин":
			# Запускаем магазин
			pass
		elif self.type == "Сундук":
			# Запускаем сундук
			pass
		else:
			raise Exception("Неверный тип этажа")

	


