import sqlite3
from datetime import date

from Client import Client
from Rent import Rent
from Dao import Dao
from DaoMethods import create_connection, create_table
from DaoClient import DaoClient
from DaoRoom import DaoRoom
from Room import Room


class DaoRent(Dao):
    def __init__(self, db_file):
        self.db_file = db_file
        conn = create_connection(self.db_file)
        sql_create_room_table = """ CREATE TABLE IF NOT EXISTS rents (
                                id BLOB PRIMARY KEY,
                                beginRent timestamp,
                                endRent timestamp,
                                clientPesel TEXT,
                                roomId INTEGER,
                                FOREIGN KEY (clientPesel) REFERENCES clients(pesel),
                                FOREIGN KEY (roomId) REFERENCES rooms(Id)
                                ); """
        create_table(conn, sql_create_room_table)
        conn.close()

    def write(self, rent):
        conn = create_connection(self.db_file)
        cur = conn.cursor()

        sql = """ INSERT INTO rents(id, beginRent, endRent, clientPesel, roomId)
                VALUES (?,?,?,?,?) """
        rentIdEdited = '"' + str(rent.Id) + '"'
        print(rentIdEdited)
        cur.execute(sql, (rentIdEdited, rent.beginRent.date(), rent.endRent.date(),
                          rent.client.pesel, rent.room.getId()))
        conn.commit()
        conn.close()

    def read(self):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM rents")
        result = []
        rows = cur.fetchall()
        for row in rows:
            dbc = DaoClient("database.sqlite")
            dbr = DaoRoom("database.sqlite")
            c = dbc.read_id(row[-2])
            r = dbr.read_id(row[-1])
            result.append(Rent(row[0], date.fromisoformat(row[1]), date.fromisoformat(row[2]), c, r))

        conn.close()
        return result

    def delete(self, Id):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("DELETE FROM rents WHERE id = ?", (Id,))
        conn.commit()
        conn.close()
