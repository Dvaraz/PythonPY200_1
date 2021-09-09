# TODO class Date
class Date:

    def __init__(self, day, month, year):
        self.day = None
        self.day_init(day)
        self.month = None
        self.month_init(month)
        self. year = None
        self.year_init(year)

    def day_init(self, day):
        if not isinstance(day, int):
            raise TypeError
        if day > 31 or day < 0:
            raise ValueError
        self.day = day

    def month_init(self, month):
        if not isinstance(month, int):
            raise TypeError
        if month > 12 or month < 0:
            raise ValueError
        self.month = month

    def year_init(self, year):
        if not isinstance(year, int):
            raise TypeError
        self.year = year

    def __repr__(self) -> str:
        return f"{self.day}, {self.month}, {self.year}"

    def __str__(self) -> str:
        return f"{self.day}, {self.month}, {self.year}"
