from copy import deepcopy
from typing import TypeVar, Callable, Any

T = TypeVar('T')


class BinaryHeap:
    def __init__(self, a: list[T], key: Callable[[T], Any]):
        self.size = len(a)
        self.heap = deepcopy(a)
        self.key = key
        self.build()

    def shift_down(self, i: int) -> None:
        while 2 * i + 1 < self.size:
            l = i * 2 + 1
            r = i * 2 + 2
            j = l
            if r < self.size and self.key(self.heap[r]) < self.key(self.heap[l]):
                j = r
            if self.key(self.heap[i]) <= self.key(self.heap[j]):
                break
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def extract(self):
        element = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.size -= 1
        self.heap.pop()
        self.shift_down(0)
        return element

    def build(self):
        for i in range(self.size // 2, -1, -1):
            self.shift_down(i)
