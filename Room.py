from abc import ABC


class Room(ABC):
    def __init__(self, Id, beds, price):
        self.id = Id
        self.beds = beds
        self.price = price
