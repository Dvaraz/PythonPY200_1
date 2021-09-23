from typing import Iterator, Tuple, Hashable, Any


class MyDict(dict):  # TODO Наследование от класса dict
    def __iter__(self):
        return iter(self.items())


if __name__ == "__main__":
    my_dict = MyDict({
        1: "a",
        2: "b",
        3: "c"
    })
    for key, value in my_dict:
        print(key, value)
