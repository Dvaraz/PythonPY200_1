# TODO  создать класс Glass
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


if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
