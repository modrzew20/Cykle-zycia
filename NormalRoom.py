from Room import Room


class NormalRoom(Room):
    def __init__(self, Id, beds, price, privateBathroom):
        self.privateBathroom = privateBathroom
        super().__init__(Id, beds, price)
