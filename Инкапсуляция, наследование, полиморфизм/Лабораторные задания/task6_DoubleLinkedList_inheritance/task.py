from typing import Any, Iterable, Optional

from node import Node, DoubleLinkedNode


class LinkedList:
    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None
        self.tail = self.head

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError()

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next

        return current_node

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.next = right_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        return node.value

    def __setitem__(self, index: int, value: Any) -> None:
        """ Метод устанавливает значение узла по указанному индексу. """
        node = self.step_by_step_on_nodes(index)
        node.value = value

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self) -> str:
        return f"{self.to_list()}"

    # TODO реализовать getter и setter для head
    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value

    # TODO реализовать getter и setter для tail
    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, value):
        self._tail = value


    # TODO Реализовать класс DoubleLinkedList
class DoubleLinkedList(LinkedList):
    def __init__(self, data: Iterable = None):
        super().__init__(data)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = DoubleLinkedNode(value)
        prev_node = self.tail

        if self.head is None:
            self.head = self.tail = append_node
        elif self.len == 1:
            self.linked_nodes(self.tail, append_node)
            prev_node = self.tail
            self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node, prev_node)
            prev_node = self.tail
            self.tail = append_node
            self.tail.prev = prev_node

        self.len += 1

    @staticmethod
    def linked_nodes(center_node: DoubleLinkedNode, right_node: Optional[DoubleLinkedNode] = None, left_node: Optional[DoubleLinkedNode] = None) -> None:
        """
        Функция, которая связывает между собой два узла.
        :param left_node: Левый или предыдущий узел
        :param center_node: Центральный узел
        :param right_node: Правый или следующий узел
        """
        center_node.prev = left_node
        center_node.next = right_node


if __name__ == '__main__':

    linked_list = LinkedList([1, 2, 3, 4, 5])
    print(linked_list.__repr__())
    double_linked_list = DoubleLinkedList([1, 2, 3])
    print(double_linked_list)
    print(double_linked_list.__repr__())
    print(type(double_linked_list.head))
    print(type(double_linked_list.tail))