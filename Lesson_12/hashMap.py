class HashMap():
	def __init__(self,size):
		self.size = size
		self.l = [None] * self.size

	def key_to_cell(self,key):
		return ord(key) % self.size

	def set(self,key,value):
		cell_of_key = self.key_to_cell(key)


		if self.l[cell_of_key] == None:
			print("first tuple in cell, no colision")
			self.l[cell_of_key] = [(key,value)]

		else:
			print("encountring hash colision")
			self.l[cell_of_key].append((key,value))

	def get(self,key):
		cell_of_key = self.key_to_cell(key)

		if self.l[cell_of_key] == None:
			return(None)

		elif len(self.l[cell_of_key]) == 1:
			return self.l[cell_of_key][0][1]

		else:
			print("finding the value between the keys in the hash colision")
			for colision_tuple in self.l[cell_of_key]:
				if colision_tuple[0] == key:
					return colision_tuple[1]

	def exists(self,key):
		cell_of_key = self.key_to_cell(key)

		if self.l[cell_of_key] == None:
			return False

		else:
			for colision_tuple in self.l[cell_of_key]:
				if colision_tuple[0] == key:
					return True
		return False
		

		

		

