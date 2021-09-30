from collections.abc import MutableSequence
from typing import Any, Optional, Iterator, Iterable
from node import Node, DoubleLinkedNode


class LinkedList(MutableSequence):
    """
    Create Linked list
    """
    NODE = Node

    def __init__(self, data: Iterable = None):
        self.len = 0
        self.head = None
        self.tail = None

        if data:
            for value in data:
                self.append(value)

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, value):
        self._head = value

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, value):
        self._tail = value

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional["Node"] = None):
        """
        Link Nodes
        @param left_node: current node
        @param right_node: next node
        @return:
        """
        left_node.next = right_node

    def step_by_step(self, index: int) -> NODE:
        """
        Searching element by index
        @param index: index of item
        @return: Node
        """
        if not isinstance(index, int):
            raise ValueError

        if not 0 <= index < self.len:
            raise IndexError
        current_node = self.head

        for _ in range(index):
            current_node = current_node.next

        return current_node

    def append(self, value):
        """
        Append node to LinkedList
        @param value: from data
        @return: None
        """
        append_node = self.NODE(value)

        if not self.head:
            self.head = self.tail = append_node
        else:
            self.linked_nodes(self.tail, append_node)
            self.tail = append_node

        self.len += 1

    def to_list(self) -> list:
        return [i for i in self]

    def __getitem__(self, item) -> Any:
        node = self.step_by_step(item)
        return node.value

    def __repr__(self):
        return f"{self.__class__.__name__}{self.to_list()}"

    def __str__(self):
        return f"{self.to_list()}"

    def __delitem__(self, index):
        print("del called")
        if not isinstance(index, int):
            raise TypeError()

        if not 0 <= index < self.len:  # для for
            raise IndexError("Index out of range")

        current_node = self.step_by_step(index)

        if index + 1 != self.len and index != 0:
            prev_node = self.step_by_step(index - 1)
            self.linked_nodes(prev_node, current_node.next)
            self.len -= 1
        elif index == 0 and self.len == 1:
            self.clear()
        elif index == 0:
            next_node = self.step_by_step(index + 1)
            self.head = next_node
            self.len -= 1
        else:
            prev_node = self.step_by_step(index - 1)
            self.linked_nodes(prev_node, None)
            self.len -= 1

    def __len__(self):
        return self.len

    def __setitem__(self, key, value):
        node = self.step_by_step(key)
        node.value = value

    def __iter__(self):
        current_node = self.head

        for i in range(self.len):
            yield current_node.value
            current_node = current_node.next

    def __contains__(self, item):
        return True if item in self.to_list() else False

    def insert(self, index: int, value) -> None:
        insert_node = self.NODE(value)
        right_index = index

        if index == 0:
            right_node = self.step_by_step(right_index)
            self.head = insert_node
            self.linked_nodes(insert_node, right_node)
        elif index >= self.len:
            self.linked_nodes(self.step_by_step(self.len - 1), insert_node)
        else:
            right_node = self.step_by_step(right_index)
            left_node = self.step_by_step(right_index - 1)
            self.head = self.step_by_step(0)
            self.linked_nodes(left_node, insert_node)
            self.linked_nodes(insert_node, right_node)
        self.len += 1

    def clear(self) -> None:
        self.head = None
        self.tail = None
        self.len = 0

    def pop(self, index: int = 0) -> Node:
        item = self.step_by_step(index)
        self.__delitem__(index)
        return item


class DoubleLinkedList(LinkedList):
    """
    Create DoubleLinkedList
    """

    NODE = DoubleLinkedNode

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional["Node"] = None):
        """
        Link nodes
        @param left_node: Prev node for right node
        @param right_node: Next node for left node
        @return:
        """
        left_node.next = right_node
        right_node.prev = left_node


if __name__ == "__main__":
    ll = LinkedList([1, 2, 3, 4, 5])
    print(ll)
    ll[1] = 100
    ll.__delitem__(2)
    ll.insert(100, "wow")
    print(ll.__repr__())
    print(ll.len)
    print("wow" in ll)
    print("-" * 20)
    a = ll.pop(1)
    print(ll)
    print(a.__repr__())
    ll_2 = DoubleLinkedList([1, 2, 3, 4, 5])
    print(ll_2.tail.__repr__())
    # print(ll_2)
    # ll_2[1] = 100
    # ll_2.__delitem__(2)
    # ll_2.insert(100, "wow")
    # print(ll_2.__repr__())
    # print(ll_2)
    # ll.clear()
    # print(ll)
    # ll_2.clear()
    # print(ll_2)