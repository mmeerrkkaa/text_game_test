
class ChestEvents:

	def __init__(self, chest_resourses: list):
		self.chest_resourses = chest_resourses
		self.open = False


	def get_resourses(self):
		return self.chest_resourses

	def open_chest(self):
		self.open = True
		return self.chest_resourses
