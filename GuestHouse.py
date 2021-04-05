from Room import Room


class GuestHouse(Room):
    def __init__(self, Id, beds, price, doubleBeds, bathRooms, kitchen, swimmingPool):
        self.doubleBeds = doubleBeds
        self.bathRooms = bathRooms
        self.kitchen = kitchen
        self.swimmingPool = swimmingPool
        super().__init__(Id, beds, price)
