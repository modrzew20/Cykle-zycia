import uuid
from datetime import datetime


class Rent:
    def __init__(self, Id, beginRent, endRent, client, room):
        self.beginRent = beginRent
        self.endRent = endRent
        self.client = client
        self.room = room
        self.Id = None
        if Id is not None:
            self.Id = Id
        else:
            self.Id = uuid.uuid4()

    def setEndRent(self):
        self.endRent = datetime.now()

    def getRentDays(self):
        result_date = datetime.now() - self.beginRent
        return result_date.date().day
