import pytest

from src.exceptions import EmptyException
from src.structures.stack import Stack


def test_stack():
    stack = Stack()
    assert stack.is_empty() == True
    stack.push(1)
    assert stack.is_empty() == False
    assert stack.pop() == 1
    stack = Stack(2, 2, 3, 4, 5)
    stack.push(1)
    assert stack.min() == 1
    assert stack.pop() == 1
    assert stack.min() == 2
    assert stack.pop() == 5
    stack.push(6)
    assert stack.min() == 2


def test_stack_empty_error():
    stack = Stack()
    with pytest.raises(EmptyException):
        stack.pop()
    with pytest.raises(EmptyException):
        stack.peek()
    with pytest.raises(EmptyException):
        stack.min()
