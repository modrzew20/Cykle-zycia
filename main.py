from datetime import datetime

from backend.src.Client import Client
from backend.src.ClientType import *
from backend.Dao.DaoClient import DaoClient
from backend.Dao.DaoRent import DaoRent
from backend.src.GuestHouse import GuestHouse
from backend.Dao.DaoRoom import DaoRoom
from backend.src.Rent import Rent

if __name__ == "__main__":
    dbr = DaoRoom("backend/database.sqlite")
    g = GuestHouse(2,2,15.0,2,2,True,False)
    #dbr.write(g)
    result = dbr.read()
    for row in result:
        print(row)
    dbc = DaoClient("backend/database.sqlite")
    c = Client("Jan", "3-4234", "13334423", "Lodz", "Piotrkowska", "25", Silver())
    # dbc.write(c)
    result = dbc.read()
    for row in result:
        print(row)

    db = DaoRent("backend/database.sqlite")
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
