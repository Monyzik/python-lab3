from src.structures.linked_list import LinkedList


class Queue(LinkedList):
    def enqueue(self, x: int) -> None:
        """
        Добавляет элемент в конец очереди.
        :param x: Элемент.
        :return: Ничего не возвращает.
        """
        super().push_back(x)

    def dequeue(self) -> int:
        """
        Удаляет элемент из начала очереди.
        :return: Возвращает удаленный элемент.
        """
        return super().pop_front()

    def front(self) -> int:
        """
        :return: Возвращает элемент из начала очереди
        """
        return super().front()
