import uuid
from datetime import datetime


class Rent:
    def __init__(self, beginRent, endRent, rentCost, client, room):
        self.beginRent = beginRent
        self.endRent = endRent
        self.rentCost = rentCost
        self.client = client
        self.room = room
        self.id = uuid.uuid4()

    def setEndRent(self):
        self.endRent = datetime.now()

    def getRentDays(self):
        result_date = datetime.now() - self.beginRent
        return result_date.date().day
