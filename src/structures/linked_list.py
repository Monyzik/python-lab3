from typing import TypeVar

from src.exceptions import EmptyException
from src.structures.node import Node

T = TypeVar('T')


class LinkedList:
    def __init__(self, *args) -> None:
        """
        Инициализация стека, если на входе есть args, то заполняем ими стек
        :param args: Аргументы которые заполняют стек
        """
        self.start: Node | None = None
        self.end: Node | None = None
        self.len = 0
        if args:
            self.start = self.end = Node(args[0], None, None)
            self.len = len(args)
            for i in range(1, len(args)):
                tmp: Node = Node(args[i], None, self.end)
                self.end.next = tmp
                self.end = tmp

    def __len__(self) -> int:
        return self.len

    def __str__(self) -> str:
        if self.start is None:
            return ""
        current: Node | None = self.start
        result: list[str] = [str(self.start.value)]
        while current.next:
            current = current.next
            result.append(str(current.value))
        return ' '.join(result)

    def __repr__(self) -> str:
        return self.__str__()

    def __eq__(self, other: "LinkedList") -> bool:
        return self.__str__() == other.__str__()

    def push_back(self, item: T) -> None:
        """
        Добавляет элемент в конец списка
        :param item: значение добавленного элемента
        :return: Ничего не возвращает
        """
        tmp: Node = Node(item, None, self.end)
        if self.end:
            self.end.next = tmp
        else:
            self.start = tmp
        self.end = tmp
        self.len += 1

    def push_front(self, item: T) -> None:
        """
        Добавляет элемент в начало списка
        :param item: значение добавленного элемента
        :return: Ничего не возвращает
        """
        tmp: Node = Node(item, self.start, None)
        if self.start:
            self.start.previous = tmp
        else:
            self.end = tmp
        self.start = tmp
        self.len += 1

    def pop_back(self) -> T:
        """
        Удаление элемента из конца списка.
        :return: Возвращает удаленный элемент.
        """
        if self.end is None:
            raise EmptyException(self.pop_back, self.__class__)
        self.end = self.end.previous
        if self.end is not None:
            self.end.next = None
        if self.end is None:
            self.start = None
        self.len -= 1

    def pop_front(self) -> T:
        """
        Удаление элемента из начала списка.
        :return: Возвращает удаленный элемент.
        """
        if self.start is None:
            raise EmptyException(self.pop_front, self.__class__)
        self.start = self.start.next
        if self.start is not None:
            self.start.previous = None
        if self.start is None:
            self.end = None
        self.len -= 1

    def back(self) -> T:
        """
        Берет последний элемент списка.
        :return: Возвращает последний элемент списка.
        """
        if self.end is None:
            raise EmptyException(self.back, self.__class__)
        return self.end.value

    def front(self) -> T:
        """
        :return: Возвращает элемент из начала списка
        """
        if self.start is None:
            raise EmptyException(self.front, self.__class__)
        return self.start.value

    def is_empty(self) -> bool:
        """
        :return: Возвращает пустой ли список.
        """
        return self.__len__() == 0
