import uuid
from datetime import datetime


class Rent:
    def __init__(self, Id, beginRent, endRent, client, room, accessType):
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

    def endRent(self):
        self.endRent = datetime.now()
        self.room.available = True
        return self.room.getPrice() * self.getRentDays()

    def getRentDays(self):
        result_date = datetime.now() - self.beginRent
        return result_date.date().day
