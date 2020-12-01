import sqlite3


class MyDatabase:

    def __init__(self, database_name='test.db'):
        # connect to db get cursor
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.executescript("DROP TABLE IF EXISTS Pets;")
        self.cursor.executescript("CREATE TABLE Pets(Id INT, Name TEXT, Price INT);")
        self.connection.commit()


class Model:
    def __init__(self, db, table, fields):
        self.db = db
        self.table = table
        self.fields = fields

    def create(self, values):
        safe_values = []
        for v in values:
            safe_values.append(f"'{v}'")

        sql = f"INSERT INTO {self.table} ({','.join(self.fields)}) VALUES( {','.join(safe_values)});"
        self.db.cursor.execute(sql)

    def read(self):
        self.db.cursor.execute(f"SELECT * FROM {self.table}")
        return self.db.cursor.fetchall()


def display_pets(data):
    output = []

    for row in data:
        print(row)
        output.append(f"ID={row[0]}, NAME={row[1]}, PRICE={row[2]}.")

    print("<br>\n".join(output))


db = MyDatabase('test.db')
pets = Model(db, "pets", ['ID', 'NAME', 'PRICE'])

pets.create([1, 'Cat', 123])
pets.create([2, 'Dog', 456])

data = pets.read()

display_pets(data)

db.connection.close()
"""
         DBSQL    HTTP/REST(METHODS/VERBS)
CREATE - INSERT - PUT
READ   - SELECT - GET
UPDATE - UPDATE - POST
DELETE - DELETE - DELETE
"""
