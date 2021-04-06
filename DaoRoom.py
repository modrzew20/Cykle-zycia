import sqlite3

from Dao import Dao
from Apartment import Apartment
from NormalRoom import NormalRoom
from GuestHouse import GuestHouse
from DaoMethods import create_connection, create_table


class DaoRoom(Dao):
    def __init__(self, db_file):
        self.db_file = db_file
        conn = create_connection(self.db_file)
        sql_create_room_table = """ CREATE TABLE IF NOT EXISTS rooms (
                                id integer PRIMARY KEY,
                                beds integer,
                                price double,
                                doubleBeds integer,
                                bathRooms integer,
                                kitchen integer,
                                swimmingPool integer,
                                roomType integer    
                                ); """
        create_table(conn, sql_create_room_table)
        conn.close()



    def write(self, room):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        if type(room) is Apartment:
            roomType = 1
            doubleBeds = room.doubleBeds
            bathRooms = room.bathRooms
            kitchen = 0
            swimmingPool = 0

        elif type(room) is NormalRoom:
            doubleBeds = 0
            kitchen = 0
            swimmingPool = 0

            if room.privateBathroom:
                bathRooms = 1
            else:
                bathRooms = 0
            roomType = 2

        elif type(room) is GuestHouse:
            roomType = 3
            doubleBeds = room.doubleBeds
            bathRooms = room.bathRooms
            if room.kitchen:
                kitchen = 1
            else:
                kitchen = 0

            if room.swimmingPool:
                swimmingPool = 1
            else:
                swimmingPool = 0
        else:
            raise TypeError("Wrong object type")

        sql = """ INSERT INTO rooms(id,beds,price,doubleBeds,bathRooms,kitchen,swimmingPool,roomType)
                VALUES (?,?,?,?,?,?,?,?) """

        cur.execute(sql, (room.id, room.beds, room.price, doubleBeds, bathRooms, kitchen, swimmingPool, roomType))
        conn.commit()
        conn.close()

    def read(self):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM rooms")
        result = []
        rows = cur.fetchall()
        for row in rows:
            if row[-1] == 1:    # Apartment
                result.append(Apartment(row[0], row[1], row[2], row[3], row[4]))
            elif row[-1] == 2:    # NormalRoom
                result.append(NormalRoom(row[0], row[1], row[2], False if row[3] == 0 else True))
            elif row[-1] == 3:  # GuestHouse
                result.append(GuestHouse(row[0], row[1], row[2], row[3], row[4], True if row[5] == 1 else False,
                                         True if row[6] else False))
        conn.close()
        return result

    def read_id(self, Id):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM rooms WHERE id = ?", (Id,))
        result = []
        rows = cur.fetchall()
        for row in rows:
            if row[-1] == 1:  # Apartment
                result.append(Apartment(row[0], row[1], row[2], row[3], row[4]))
            elif row[-1] == 2:  # NormalRoom
                result.append(NormalRoom(row[0], row[1], row[2], False if row[3] == 0 else True))
            elif row[-1] == 3:  # GuestHouse
                result.append(GuestHouse(row[0], row[1], row[2], row[3], row[4], True if row[5] == 1 else False,
                                         True if row[6] else False))
        conn.close()
        return result

    def delete(self, Id):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("DELETE FROM rooms WHERE id = ?", (Id,))
        conn.commit()
        conn.close()