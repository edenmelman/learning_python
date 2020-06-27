class Stack:
	def __init__(self):
		self._l = []

	def push(self, item):
		self._l.append(item)

	def pop(self):
		return self._l.pop()

	def peek(self):
		return self._l[-1]

	def is_empty(self):
		return not self._l

class BoundedStack(Stack):
	def __init__(self, size):
		super().__init__()
		self.size = size

	def push(self,item):
		if len(self._l) < self.size:
			return super().push(item)
		raise StackFullError("Can't add item to a full stack")

	def is_full(self):
		return len(self._l) == self.size
			


class StackFullError(Exception):
	pass