from backend.Dao.Dao import Dao
from backend.src.Apartment import Apartment
from backend.src.NormalRoom import NormalRoom
from backend.src.GuestHouse import GuestHouse
from backend.Dao.DaoMethods import create_connection, create_table
import copy


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
                                roomType integer,
                                available integer 
                                ); """
        create_table(conn, sql_create_room_table)
        conn.close()

    def write(self, room):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        if type(room) is Apartment:
            roomType = 1
            doubleBeds = room.doubleBeds
            bathroom = room.bathRooms

            kitchen = 0
            swimmingPool = 0

        elif type(room) is NormalRoom:
            doubleBeds = 0
            kitchen = 0
            bathroom = room.privateBathroom
            swimmingPool = 0
            roomType = 2

        elif type(room) is GuestHouse:
            roomType = 3
            doubleBeds = room.doubleBeds
            bathroom = room.bathRooms
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


        sql = """ INSERT INTO rooms(id ,beds,price,doubleBeds,bathRooms,kitchen,swimmingPool,roomType,available)
                VALUES (?,?,?,?,?,?,?,?,?) """


        cur.execute(sql, (room.id,room.beds, room.price, doubleBeds, bathroom, kitchen, swimmingPool, roomType,room.available))
        conn.commit()
        conn.close()

    def read(self):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM rooms")

        result = []
        rows = cur.fetchall()
        r = [0] * 8
        for row in rows:
            if row[-2] == 1:  # Apartment
                r[0] = "Apartament"
            elif row[-2] == 2:  # NormalRoom
                r[0] = "Pokoj"
            elif row[-2] == 3:  # GuestHouse
                r[0] = "Dom letniskowy"
            for j in range(7):
                r[j+1] = row[j]
            result.append(copy.deepcopy(r))
        conn.close()
        return result

    def read_id(self, Id):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM rooms WHERE id = ?", (Id,))
        rows = cur.fetchall()
        if len(rows) == 0:
            conn.close()
            return False
     #  id, beds, price, doubleBeds, bathRooms, kitchen, swimmingPool, roomType, available
        for row in rows:
            if row[-2] == 1:  # Apartment
                result = Apartment(row[0],row[-1], row[1], row[2], row[3], row[4])
            elif row[-2] == 2:  # NormalRoom
                result = NormalRoom(row[0],row[-1],row[1], row[2],  False if row[3] == 0 else True)
            elif row[-2] == 3:  # GuestHouse
                result = GuestHouse(row[0],row[-1],  row[1],row[2],  row[3], row[4], True if row[5] == 1 else False,
                                    True if row[6] else False)
        conn.close()
        return result

    def read_available_room(self):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("SELECT id FROM rooms WHERE available == 0")
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append(str(row[0]))
        conn.close()
        return result

    def read_id_all_room(self):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("SELECT id FROM rooms")
        rows = cur.fetchall()
        result = []
        for row in rows:
            result.append(str(row[0]))
        conn.close()
        return result


    def delete(self, Id):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("DELETE FROM rooms WHERE id = ?", (Id,))
        conn.commit()
        conn.close()
