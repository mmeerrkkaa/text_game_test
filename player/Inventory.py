class Inventory:
	def __init__(self):
		self.items = {}

	def add_item(self, item_name: str, count: int = 1):
		""" Добавляет предмет в инвентарь если его нету. Если есть, то добавляет к существующему """
		if item_name in self.items:
			self.items[item_name]["count"] += count
		else:
			self.items[item_name] = {"count": count}

	def remove_item(self, item_name: str, count: int = 1):
		""" Убирает предмет из инвентаря если он есть. Если нет, то выдает ошибку """
		if item_name in self.items:
			if self.items[item_name]["count"] > count:
				self.items[item_name]["count"] -= count
			else:
				del self.items[item_name]
		else:
			raise Exception("Предмета нет в инвентаре")

	def get_item(self, item_name: str):
		""" Возвращает предмет из инвентаря. Если его нет, то выдает ошибку """
		if item_name in self.items:
			return self.items[item_name]
		else:
			raise Exception("Предмета нет в инвентаре")

	def get_items(self):
		return self.items




