from datetime import datetime

from Client import Client
from ClientType import *
from DaoClient import DaoClient
from DaoRent import DaoRent
from GuestHouse import GuestHouse
from Apartment import Apartment
from NormalRoom import NormalRoom
from DaoRoom import DaoRoom
from Rent import Rent

if __name__ == "__main__":
    dbr = DaoRoom("database.sqlite")
    g = GuestHouse(2,2,15.0,2,2,True,False)
    # dbr.write(g)
    result = dbr.read()
    for row in result:
        print(row)
    dbc = DaoClient("database.sqlite")
    c = Client("Jan", "3-4234", "13334423", "Lodz", "Piotrkowska", "25", Silver())
    # dbc.write(c)
    result = dbc.read()
    for row in result:
        print(row)

    db = DaoRent("database.sqlite")
    print(g.getId())
    r = Rent(None, datetime(2020, 4, 1), datetime.now(), c, g)
    db.write(r)
    result = db.read()
    print(result)
    for row in result:
        print(row)
        print(row.client)
        print(row.beginRent)
        print(row.room)
