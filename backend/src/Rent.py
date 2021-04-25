import uuid
from datetime import datetime


class Rent:
    def __init__(self, Id, beginRent, endRent, client, room, accessType, price):
        self.beginRent = beginRent
        self.endRent = endRent
        self.client = client
        self.room = room
        self.Id = None
        if Id is not None:
            self.Id = Id
        else:
            self.Id = uuid.uuid4()
        self.accessType = accessType
        self.price = price

    def getCost(self):
        result_date = (datetime.strptime(self.endRent, '%Y-%m-%d') - datetime.strptime(self.beginRent, '%Y-%m-%d')).days
        if result_date == 0: result_date = 1
        return self.room.getPrice() * result_date
