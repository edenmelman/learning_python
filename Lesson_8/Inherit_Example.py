class Animal:
	def __init__(self, name, color):
		self.name = name + " the animal"
		self.color = color

	def greet(self):
		print("my name is {}".format(self.name))
		self._speak()

	def _speak(self):
		print("")

class Cow(Animal):
	def __init__(self, name):
		super().__init__(name, "black&white")
		self.name += " the cow" 


	def _speak(self):
		print("Moooooo")


cloe = Cow(name="Cloe")
cloe.greet()