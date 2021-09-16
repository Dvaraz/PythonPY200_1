from typing import Any, Optional


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value

        self.next = None
        self.set_next(next_)

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def set_next(self, next_: Optional["Node"] = None) -> None:
        self.is_valid(next_)
        self.next = next_


class LinkedList:
    def __init__(self, data=None):
        self.len = 0
        self.head: Optional[Node] = None
        
        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value):
        append_node = Node(value)

        if self.head is None:
            self.head = append_node
        else:
            last_index = self.len - 1
            last_node = self.step_by_step(last_index)

            self.link_nodes(last_node, append_node)

        self.len += 1

    @staticmethod
    def link_nodes(left_node: Node, right_node=None):
        left_node.set_next(right_node)

    def step_by_step(self, index: int, start: int = 0, end: int = None):

        if not 0 <= index < self.len:
            raise IndexError()

        # if start != 0:
        #     self.head = self.step_by_step(start)
        #     current_start = self.head
        current_node = self.head

        for _ in range(index):
            current_node = current_node.next

        return current_node

    def index(self, value, start: int = 0, end: int = None) -> int:
        list_ = self.to_list()
        index_count = 0
        for _ in list_[start:end]:
            if _ == value:
                return index_count
            index_count += 1

    def __getitem__(self, index):
        node = self.step_by_step(index)
        return node.value

    def __setitem__(self, index, value):
        node = self.step_by_step(index)
        node.value = value

    def to_list(self) -> list:
        return [linked_list_value for linked_list_value in self]

    def __repr__(self):
        return f"{self.__class__.__name__}({self.to_list()})"

    def __str__(self):
        return f"{self.to_list()}"


if __name__ == "__main__":
    asd = [1, 2, 3, 4, 5, 6, "wow", 7, 8]
    linked_list = LinkedList(asd)
    print(linked_list.index("wow"))

