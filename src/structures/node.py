class Node:
    def __init__(self, value, _next, _previous) -> None:
        """
        Инициализация элемента двусвязного списка
        :param value: значение элемента
        :param _next: следующий элемент стека
        :param _previous: предыдущий элемент стека
        """
        self.value = value
        self.next: Node | None = _next
        self.previous: Node | None = _previous

    def __str__(self) -> str:
        return str(self.value)

    def __repr__(self) -> str:
        return f"next = {self.next}, previous = {self.previous}, value = {self.value}"
