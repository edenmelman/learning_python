from queue_out_of_stacks_improved_shifts import Stack, Queue
import pytest

def test_queue():
	num_queue = Queue()
	num_queue.enqueue(1)
	num_queue.enqueue(2)
	num_queue.enqueue(3)
	assert num_queue.front() == 1
	assert num_queue.rear() == 3
	assert num_queue.dequeue() == 1
	assert num_queue.front() == 2
	num_queue.enqueue(4)
	num_queue.enqueue(5)
	assert num_queue.dequeue() == 2
	assert num_queue.dequeue() == 3
	assert num_queue.dequeue() == 4
	assert num_queue.rear() == 5