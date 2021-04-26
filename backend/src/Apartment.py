from backend.src.Room import Room


class Apartment(Room):
    def __init__(self, Id, available, beds, price, doubleBeds, bathRooms):
        self.doubleBeds = doubleBeds
        self.bathRooms = bathRooms
        super().__init__(Id, available, beds, price)

    def __str__(self) -> str:
        return "Apartment, id: " + str(self.id) + " beds: " \
               + str(self.beds) + " price: " + str(self.price) \
               + " double beds: " + str(self.doubleBeds) + " bathrooms " + str(self.bathRooms)
