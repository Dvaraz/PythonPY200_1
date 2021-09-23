import json
from typing import Iterable
from abc import ABC, abstractmethod


class IStructureDriver(ABC):
    @abstractmethod
    def read(self) -> Iterable:
        """
        Считывает информацию из драйвера и возвращает её для объекта, использующего этот драйвер

        :return Последовательность элементов, считанная драйвером, для объекта
        """
        pass

    @abstractmethod
    def write(self, data: Iterable) -> None:
        """
        Получает информацию из объекта, использующего этот драйвер, и записывает её в драйвер

        :param data Последовательность элементов, полученная от объекта, для записи драйвером
        """
        pass


class SimpleFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> Iterable:
        with open(self.filename) as f:
            return [int(line) for line in f]

    def write(self, data: Iterable) -> None:
        with open(self.filename, "w") as f:
            for value in data:
                f.write(str(value))
                f.write('\n')

    def __repr__(self):
        return f"{self.__class__.__name__}(\"{self.filename}\")"


# TODO Реализовать класс JsonFileDriver
class JsonFileDriver(IStructureDriver):
    def __init__(self, filename):
        self.filename = filename

    def read(self) -> Iterable:
        with open(self.filename) as f:
            data = json.load(f)
            return data

    def write(self, data: Iterable) -> None:
        with open(self.filename, "w") as f:
            json_data = json.dumps(data)
            json.dump(json_data, f)


if __name__ == "__main__":
    write_data = [1, 2, (3, 4)]
    driver_1 = JsonFileDriver("test.json")
    driver_1.write(write_data)
    read_data = driver_1.read()
    print(read_data)

