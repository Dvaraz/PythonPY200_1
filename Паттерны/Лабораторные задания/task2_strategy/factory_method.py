from abc import ABC, abstractmethod

from drivers import IStructureDriver, SimpleFileDriver, JsonFileDriver


class DriverFactoryMethod(ABC):
    @classmethod
    @abstractmethod
    def get_driver(cls) -> IStructureDriver:
        ...


class SimpleFileFactoryMethod(DriverFactoryMethod):
    DEFAULT_NAME = 'untitled.txt'

    @classmethod
    def get_driver(cls) -> IStructureDriver:
        filename = input('Введите название текстового файла: (.txt)').strip()
        filename = filename or cls.DEFAULT_NAME
        if not filename.endswith('.txt'):
            filename = f'{filename}.txt'

        return SimpleFileDriver(filename)


# TODO реализовать класс JsonFileDriveFactoryMethod
class JsonFileDriverFactoryMethod(DriverFactoryMethod):
    DEFAULT_NAME = "new.json"

    @classmethod
    def get_driver(cls) -> IStructureDriver:
        file_name = input("Enter file name: (.json)").strip()
        file_name = file_name or cls.DEFAULT_NAME
        if not file_name.endswith(".json"):
            file_name = f"{file_name}.json"

        return JsonFileDriver(file_name)


if __name__ == '__main__':
    driver = SimpleFileFactoryMethod.get_driver()
    print(driver)
