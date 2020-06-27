from data_structures import Stack, StackFullError, BoundedStack
import pytest

def test_stack():
	stack = Stack()
	stack.push(3)
	stack.push(2)
	assert stack.peek() == 2
	assert stack.pop() == 2
	assert stack.pop() == 3
	assert stack.is_empty()

def test_bounded_stack():
	stack = BoundedStack(size=2)
	stack.push(3)
	assert not stack.is_full()

	stack.push(2)
	assert stack.is_full()

	with pytest.raises(StackFullError):
		stack.push(6)

	assert stack.peek() == 2
	assert stack.pop() == 2
	assert stack.pop() == 3
	assert stack.is_empty()