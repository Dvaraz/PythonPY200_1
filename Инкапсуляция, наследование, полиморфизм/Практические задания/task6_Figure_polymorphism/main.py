class TriangleCalculator:

    @classmethod
    def area(cls, *args):
        if len(args) == 2:
            cls._area_height(*args)
        if len(args) == 3:
            cls._area_by_angle(*args)

    @staticmethod
    def _area_by_angle(a, b, angle):
        ...

    @staticmethod
    def _area_height(a, h):
        ...
