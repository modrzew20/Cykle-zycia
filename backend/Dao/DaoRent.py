from backend.Dao.Dao import Dao
from backend.Dao.DaoMethods import create_connection, create_table
import copy


class DaoRent(Dao):
    def __init__(self, db_file):
        self.db_file = db_file
        conn = create_connection(self.db_file)
        sql_create_room_table = """ CREATE TABLE IF NOT EXISTS rents (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                beginRent timestamp,
                                endRent timestamp,
                                clientPesel TEXT,
                                roomId INTEGER,
                                accessType INTEGER,
                                price DOUBLE ,
                                FOREIGN KEY (clientPesel) REFERENCES clients(pesel),
                                FOREIGN KEY (roomId) REFERENCES rooms(Id)
                                ); """
        create_table(conn, sql_create_room_table)
        conn.close()

    def write(self, rent):
        conn = create_connection(self.db_file)
        cur = conn.cursor()

        sql = """ INSERT INTO rents(beginRent, endRent, clientPesel, roomId, accessType, price)
                VALUES (?,?,?,?,?,?) """

        from backend.src.AccessType import Exclusive, VIP, Standard
        accessType = 0
        if type(rent.accessType) == Exclusive:
            accessType = 1
        elif type(rent.accessType) == VIP:
            accessType = 2
        elif type(rent.accessType) == Standard:
            accessType = 3

        cur.execute(sql, (rent.beginRent.date(), rent.endRent.date(),
                          rent.client.pesel, rent.room.id, accessType,rent.price))
        conn.commit()
        conn.close()

    def read(self):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM rents")
        result = []
        rows = cur.fetchall()
        r = [0] * 7
        for row in rows:
            for j in range(7):
                r[j] = row[j]
            result.append(copy.deepcopy(r))
        conn.close()
        return result

    def sum_all_rent(self, pesel):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("SELECT SUM (price) FROM rents WHERE clientPesel = ?", (pesel,))
        result = cur.fetchone()
        conn.close()
        return result[0]



    def endRent(self, date, id, price):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        sql = """UPDATE rents
                        SET price = ? ,endRent = ?
                        WHERE id = ?"""

        cur.execute(sql, [price, date.date(), id])
        conn.commit()
        conn.close()

        pass

    def delete(self, Id):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("DELETE FROM rents WHERE id = ?", (Id,))
        conn.commit()
        conn.close()

    def readOne(self, Id):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM rents WHERE id = ?", (Id,))
        row = cur.fetchall()[0]
        from backend.src.Rent import Rent
        # (self, Id, beginRent, endRent, client, room, accessType):
        rent = Rent(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
        conn.close()
        return rent
