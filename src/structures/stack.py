from src.structures.linked_list import LinkedList


class Stack(LinkedList):
    def __init__(self, *args):
        self.minimum_list = LinkedList()
        for item in args:
            if self.minimum_list.is_empty() or self.minimum_list.back() > item:
                self.minimum_list.push_back(item)
            else:
                self.minimum_list.push_back(self.minimum_list.back())
        super().__init__(*args)

    def push(self, x: int) -> None:
        """
        Добавляет элемент в конец стека
        :param x: значение добавленного элемента
        :return: Ничего не возвращает
        """
        if self.minimum_list.is_empty() or self.minimum_list.back() > x:
            self.minimum_list.push_back(x)
        else:
            self.minimum_list.push_back(self.minimum_list.back())
        super().push_back(x)

    def pop(self) -> None:
        """
        Удаление элемента из конца стека
        :return: Ничего не возвращает
        """
        self.minimum_list.pop_back()
        return super().pop_back()

    def peek(self) -> int:
        """
        Взятие элемента с конца стека.
        :return: Возвращает искомый элемент
        """
        return super().back()

    def min(self) -> int:
        """
        Взятие элемента с наименьшим значением.
        :return: Возвращает искомый элемент
        """
        return self.minimum_list.back()
