from typing import Any, Optional
import weakref


class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Initialize Node.
        @param value: Node value, can by any.
        @param next_: Next node, if exist.
        """
        self.value = value
        self.next = next_

    @classmethod
    def _is_valid(cls, node: Any) -> None:
        """
        Check if node is valid
        @param node: Node, can be any.
        @return: None
        """
        if not isinstance(node, (cls, type(None))):
            raise TypeError

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, value: Optional["Node"]):
        self._is_valid(value)
        self._next = value

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.value}, {self._next}"

    def __str__(self) -> str:
        return f"{self.value}"


class DoubleLinkedNode(Node):
    def __init__(self, value: Any, next_: Optional["Node"] = None, prev: Optional["Node"] = None):
        """
        Initialize DoubleLinkedNode.

        @param value: Node value, can be any.
        @param next_: Next node if exist.
        @param prev: Prev node if exist.
        """
        super().__init__(value, next_)
        self.prev = prev

    def __repr__(self):
        return super().__repr__() + f",DoubleLinkedNode{self._prev()})"

    @property
    def prev(self):
        return None if self._prev is None else self._prev()

    @prev.setter
    def prev(self, value):
        self._is_valid(value)
        self._prev = None if value is None else weakref.ref(value)


if __name__ == "__main__":
    node_1 = Node(1)
    print(node_1.__repr__())

    node_2 = DoubleLinkedNode(2)
    print(node_2.__repr__())