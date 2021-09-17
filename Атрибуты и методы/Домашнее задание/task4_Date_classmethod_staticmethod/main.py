class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year: int):
        """Проверяет, является ли год високосным"""
        if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
            # print(f"{year} is not leap")
            return False
        else:
            # print(f"{year} is leap")
            return True

    @classmethod
    def get_max_day(cls, month: int, year: int):
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if cls.is_leap_year(year):
            return cls.DAY_OF_MONTH[1][month - 1]
        else:
            return cls.DAY_OF_MONTH[0][month - 1]

    @staticmethod
    def is_valid_date(day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if not isinstance(year, int) or not isinstance(month, int) or not isinstance(day, int):
            raise TypeError


if __name__ == "__main__":
    date = Date(12, 7, 2001)
    print(date.get_max_day(2, 2021))
    print(date.is_leap_year(2001))
    pass
