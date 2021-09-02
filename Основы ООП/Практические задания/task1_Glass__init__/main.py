class Glass:
    def __init__(self, capacity_volume: [int, float], occupied_volume: [int, float]):
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError
        if capacity_volume <= 0:
            raise ValueError

        self.capacity_volume = capacity_volume

        if occupied_volume > capacity_volume or occupied_volume < 0:
            raise ValueError
        if not isinstance(occupied_volume, (int, float)):
            raise TypeError

        self.occupied_volume = occupied_volume


if __name__ == "__main__":
    glass1 = Glass(200, 150)
    glass2 = Glass(350, 200)

    # glass3 = Glass("100", "50")
    glass4 = Glass(1, -1)

