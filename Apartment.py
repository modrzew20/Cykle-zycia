from Room import Room


class Apartment(Room):
    def __init__(self, Id, beds, price, doubleBeds, bathRooms):
        self.doubleBeds = doubleBeds
        self.bathRooms = bathRooms
        super().__init__(Id, beds, price)