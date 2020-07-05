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

class Queue:
	def __init__(self):
		self.stack_a = Stack()
		self.stack_b = Stack()

	def enqueue(self,item):
		self.stack_a.push(item)
		
	def dequeue(self):
		if self.stack_b.is_empty():
			while not self.stack_a.is_empty():
				self.stack_b.push(self.stack_a.pop())
		return self.stack_b.pop()
		
			
	def front(self):
		if self.stack_b.is_empty():
			while not self.stack_a.is_empty():
				self.stack_b.push(self.stack_a.pop())
		return self.stack_b.peek()
		

	def rear(self):
		if self.stack_a.is_empty():
			while not self.stack_b.is_empty():
				self.stack_a.push(self.stack_b.pop())
		return self.stack_a.peek()