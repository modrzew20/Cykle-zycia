from abc import ABC


class Room(ABC):
    def __init__(self, Id, beds, price):
        self.id = Id
        self.beds = beds
        self.price = price

    def getId(self):
        return self.id

    def getBeds(self):
        return self.beds

    def getPrice(self):
        return self.price