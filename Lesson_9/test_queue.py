from data_structures import Stack, Queue

def test_queue():
	stack = Stack()
	stack.push(3)
	stack.push(2)
	assert stack.peek() == 2
	assert stack.pop() == 2
	assert stack.pop() == 3
	assert stack.is_empty()