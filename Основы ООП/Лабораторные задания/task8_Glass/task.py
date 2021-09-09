# TODO Добавить методы add_water и remove_water
class Glass:

    def __init__(self, capacity_volume, occupied_volume):
        self.capacity_volume = None
        self.occupied_volume = None
        self.capacity_init(capacity_volume)
        self.occupied_init(occupied_volume)

    def capacity_init(self, capacity_volume):
        if not isinstance(capacity_volume, int):
            raise TypeError("Wrong Type")
        if capacity_volume < 0:
            raise ValueError("Wrong Value")
        self.capacity_volume = capacity_volume

    def occupied_init(self, occupied_volume):
        if not isinstance(occupied_volume, int):
            raise TypeError("Wrong Type")
        if occupied_volume > self.capacity_volume or occupied_volume < 0:
            raise ValueError("Wrong Value")
        self.occupied_volume = occupied_volume

    def add_water(self, water):
        if not isinstance(water, int):
            raise TypeError
        if (water + self.occupied_volume) > self.capacity_volume or water < 0:
            raise ValueError
        self.occupied_volume = self.occupied_volume + water

    def remove_water(self, remove_water):
        if not isinstance(remove_water, int):
            raise TypeError
        if (self.occupied_volume - remove_water) < 0:
            raise ValueError
        self.occupied_volume = self.occupied_volume - remove_water


if __name__ == '__main__':
    glass_1 = Glass(200, 100)
    print(glass_1.capacity_volume, glass_1.occupied_volume)
    glass_1.add_water(100)
    print(glass_1.capacity_volume, glass_1.occupied_volume)
    glass_1.remove_water(25)
    print(glass_1.capacity_volume, glass_1.occupied_volume)
    glass_1.remove_water(175)
    print(glass_1.capacity_volume, glass_1.occupied_volume)