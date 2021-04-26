from abc import ABC


class Room(ABC):
    def __init__(self,  Id,available, beds, price):
        self.available = available
        self.id = Id
        self.beds = beds
        self.price = price

    