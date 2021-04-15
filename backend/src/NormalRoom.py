from backend.src.Room import Room


class NormalRoom(Room):
    def __init__(self, Id,available , beds, price, privateBathroom):
        self.privateBathroom = privateBathroom
        super().__init__(Id,available , beds, price)

    def __str__(self) -> str:
        return "NormalRoom, id: " + str(self.id) + " beds: " \
               + str(self.beds) + " price: " + str(self.price) + " Private bathroom " + str(self.privateBathroom)
