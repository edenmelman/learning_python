class House:

	def __init__(self, size, balagan_level, color, construction_year):
		self.size = size
		self.balagan_level = max(balagan_level,0)
		self.color = color
		self.construction_year = construction_year

	def organize(self):
		self.balagan_level = max(0,self.balagan_level - 1)

	def repaint(self,new_color):
		self.color = new_color

	def make_over(self):
		self.repaint("white")
		self.organize()

	def calc_value(self):
		return self.size / (self.balagan_level + 1) + self.construction_year

melmans_house = House(size=70, balagan_level=4, color="red", construction_year=1990)

print(melmans_house.calc_value())

melmans_house.make_over()

print(melmans_house.calc_value())