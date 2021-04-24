from datetime import datetime

from backend.src.AccessType import Standard
from backend.src.Client import Client
from backend.src.ClientType import *
from backend.Dao.DaoClient import DaoClient
from backend.Dao.DaoRent import DaoRent
from backend.src.GuestHouse import GuestHouse
from backend.Dao.DaoRoom import DaoRoom
from backend.src.Rent import Rent

if __name__ == "__main__":
    dbr = DaoRoom("backend/database.sqlite")
    g = GuestHouse(2, 2, 15.0, 2, 2, True, False, False)
    # dbr.write(g)
    result = dbr.read()
    for row in result:
        print(row)
    dbc = DaoClient("backend/database.sqlite")
    c = Client("Jan", "Kowalski", "13334423", "Lodz", "Piotrkowska", "25", Silver())
    # dbc.write(c)
    result = dbc.read()
    for row in result:
        print(row)

    db = DaoRent("backend/database.sqlite")
    print(g.getId())
    at = Standard()
    r = Rent(None, datetime(2020, 4, 1), datetime(2120, 4, 1), c, g, at)
    r2 = Rent(2, datetime(2019, 4, 1), datetime.now(), c, g, at)
    # db.write(r)
    db.endRent(datetime(2002, 4, 1), 2)
    rent = db.readOneRent(2)

    print("Room id: ", rent.Id)
    print("this is rnet", rent)
