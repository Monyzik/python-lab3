import pytest

from src.exceptions import EmptyException
from src.structures.queue import Queue


def test_queue():
    queue = Queue()
    assert queue.is_empty() == True
    queue.enqueue(1)
    assert queue.is_empty() == False
    assert queue.dequeue() == 1
    queue = Queue(2, 3, 3, 4, 5)
    queue.enqueue(1)
    assert queue.front() == 2
    assert queue.dequeue() == 2
    assert queue.front() == 3
    assert queue.dequeue() == 3
    assert Queue(1, 2, 3) != Queue(2, 3, 4)


def test_queue_empty_error():
    queue = Queue()
    with pytest.raises(EmptyException):
        queue.dequeue()
    with pytest.raises(EmptyException):
        queue.front()
