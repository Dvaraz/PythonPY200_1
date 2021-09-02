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

        # TODO установить значение следующего узла с помощью метода set_next
        self.next_ = None
        self.set_next(next_)

    def __repr__(self) -> str:
        return f"Node({self.value}, {self.next})"

    def is_valid(self, node: Any) -> None:
        # TODO метод проверки корректности связываемого узла
        if not isinstance(node, Node, self.next_):
            return TypeError

    def set_next(self, next_: Optional["Node"] = None) -> None:
        # TODO метод должен проверять корректность узла и устанавливать значение атрибуту next
        if not isinstance(next_, Node):
            return TypeError
        else:
            self.next_ = next_


if __name__ == '__main__':
    # TODO
    node_1 = Node(1)
    node_2 = Node(2)
    node_1 = node_2.next_
