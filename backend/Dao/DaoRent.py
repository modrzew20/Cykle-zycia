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
                                FOREIGN KEY (clientPesel) REFERENCES clients(pesel),
                                FOREIGN KEY (roomId) REFERENCES rooms(Id)
                                ); """
        create_table(conn, sql_create_room_table)
        conn.close()

    def write(self, rent):
        conn = create_connection(self.db_file)
        cur = conn.cursor()

        sql = """ INSERT INTO rents(beginRent, endRent, clientPesel, roomId, accessType)
                VALUES (?,?,?,?,?) """

        # print(rentIdEdited)
        from backend.src.AccessType import Exclusive, VIP, Standard
        accessType = 0
        if isinstance(rent.accessType, Exclusive):
            accessType = 1
        elif isinstance(rent.accessType, VIP):
            accessType = 2
        elif isinstance(rent.accessType, Standard):
            accessType = 3

        cur.execute(sql, (rent.beginRent.date(), rent.endRent.date(),
                          rent.client.pesel, rent.room.getId(), accessType))
        conn.commit()
        conn.close()

    def read(self):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM rents")
        result = []
        rows = cur.fetchall()
        r = [0] * 6
        for row in rows:
            for j in range(6):
                r[j] = row[j]
            result.append(copy.deepcopy(r))
        conn.close()
        return result

    def endRent(self, endRent, Id):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        sql = """UPDATE rents
                        SET endRent = ?
                        WHERE id = ?"""

        cur.execute(sql, [endRent, Id])
        conn.commit()
        conn.close()

        pass

    def delete(self, Id):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("DELETE FROM rents WHERE id = ?", (Id,))
        conn.commit()
        conn.close()

    def readOneRent(self, Id):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM rents WHERE id = ?", (Id,))
        row = cur.fetchall()[0]
        from backend.src.Rent import Rent
        # (self, Id, beginRent, endRent, client, room, accessType):
        rent = Rent(row[0], row[1], row[2], row[3], row[4], row[5])
        conn.close()
        return rent
