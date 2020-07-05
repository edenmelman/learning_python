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
		self.lifo = Stack()
		self.fifo = Stack()

	def enqueue(self,item):
		self.lifo.push(item)
		
	def dequeue(self):
		while self.lifo.is_empty() == False:
			self.fifo.push(self.lifo.pop())

		print(self.fifo.pop())

		while self.fifo.is_empty() == False:
			self.lifo.push(self.fifo.pop())

	def front(self):
		while self.lifo.is_empty() == False:
			self.fifo.push(self.lifo.pop())
		print(self.fifo.peek())
		return self.fifo.peek()
		

		while self.fifo.is_empty() == False:
			self.lifo.push(self.fifo.pop())

	def rear(self):
		print(self.lifo.peek())

numQueue = Queue()
numQueue.enqueue(2)
numQueue.enqueue(4)
numQueue.enqueue(5)
numQueue.rear()
numQueue.front()
numQueue.dequeue()
numQueue.front()
