from backend.src.Client import Client
from backend.Dao.Dao import Dao
from backend.Dao.DaoMethods import create_connection, create_table
from backend.src.ClientType import *
import copy

class DaoClient(Dao):
    def __init__(self, db_file):
        self.db_file = db_file
        conn = create_connection(self.db_file)
        sql_create_room_table = """ CREATE TABLE IF NOT EXISTS clients (
                                firstName TEXT NOT NULL,
                                lastNamse TEXT NOT NULL,
                                pesel TEXT PRIMARY KEY,
                                city TEXT NOT NULL,
                                street TEXT NOT NULL,
                                num TEXT NOT NULL,
                                clientType integer 
                                ); """
        create_table(conn, sql_create_room_table)
        conn.close()

    def write(self, client):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        client_type = None
        if type(client.clientType) is Default:
            client_type = 1
        elif type(client.clientType) is Silver:
            client_type = 2
        elif type(client.clientType) is Gold:
            client_type = 3
        elif type(client.clientType) is Platinum:
            client_type = 4
        else:
            raise TypeError("Wrong object type")

        sql = """ INSERT INTO clients(firstName, lastNamse, pesel, city, street, num, clientType)
                VALUES (?,?,?,?,?,?,?) """

        cur.execute(sql, (client.firstName, client.lastName, client.pesel,
                          client.city, client.street, client.number, client_type))
        conn.commit()
        conn.close()

    def read(self):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM clients")
        result = []
        rows = cur.fetchall()
        client_type = None
        r= [0] * 7
        for row in rows:
            for j in range(7):
                if j == 6:
                    if row[6] == 1:    # Default
                        r[6] = "Default"
                    elif row[6] == 2:    # Silver
                        r[6] = "Silver"
                    elif row[6] == 3:  # Gold
                        r[6] = "Gold"
                    elif row[6] == 4:  # Platinum
                        r[6] = "Platinum"
                else:
                    r[j] = row[j]
            result.append(copy.deepcopy(r))
        conn.close()
        return result

    def read_id(self, pesel):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("SELECT * FROM clients WHERE pesel = ?", (pesel,))

        rows = cur.fetchall()
        if len(rows) == 0:
            conn.close()
            return False

        client_type = None
        for row in rows:
            if row[-1] == 1:  # Default
                client_type = Default()
            elif row[-1] == 2:  # Silver
                client_type = Silver()
            elif row[-1] == 3:  # Gold
                client_type = Gold()
            elif row[-1] == 3:  # Platinum
                client_type = Platinum()
            result = Client(row[1], row[2], row[3], row[4], row[5], row[6], client_type)

        conn.close()
        return result

    def delete(self, pesel):
        conn = create_connection(self.db_file)
        cur = conn.cursor()
        cur.execute("DELETE FROM clients WHERE pesel = ?", (pesel,))
        conn.commit()
        conn.close()