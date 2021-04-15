from backend.src.Room import Room


class GuestHouse(Room):
    def __init__(self, Id,available , beds, price, doubleBeds, bathRooms, kitchen, swimmingPool):
        self.doubleBeds = doubleBeds
        self.bathRooms = bathRooms
        self.kitchen = kitchen
        self.swimmingPool = swimmingPool
        super().__init__(Id,available , beds, price)

    def __str__(self) -> str:
        return "Guest House, id: " + str(self.id) + " beds: " \
               + str(self.beds) + " price: " + str(self.price) \
               + " double beds: " + str(self.doubleBeds) + " bathrooms "\
               + str(self.bathRooms) + " kitchen: " + str(self.kitchen) + " swimming pool: " + str(self.swimmingPool)