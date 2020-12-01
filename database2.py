import sqlite3


class Model:
    def __init__(self, db, table, fields, field_objects):
        self.db = db
        self.table = table
        self.fields = fields
        self.field_objects = field_objects

    def create(self, values):
        safe_values = []
        for v in values:
            safe_values.append(f"'{v}'")

        sql = f"INSERT INTO {self.table} ({','.join(self.fields)}) VALUES( {','.join(safe_values)});"
        self.db.cursor.execute(sql)
        self.db.connection.commit()

    def read(self, custom_sql=""):
        self.db.cursor.execute(custom_sql if custom_sql else f"SELECT * FROM {self.table}")
        return self.db.cursor.fetchall()


class MyDatabase:

    def __init__(self, database_name='test.db'):
        # connect to db get cursor
        self.connection = sqlite3.connect(database_name)
        self.cursor = self.connection.cursor()

    def create_table(self, model: Model):
        self.cursor.executescript(f"DROP TABLE IF EXISTS {model.table};")
        field_text = []
        for f in model.field_objects:
            field_text.append(f"{f.name} {f.field_type}")
        sql = f"CREATE TABLE {model.table}({','.join(field_text)});"
        self.cursor.executescript(sql)
        self.connection.commit()


class Field:
    def __init__(self, name, field_type="TEXT", display_name=""):
        self.name = name
        self.field_type = field_type
        self.display_name=display_name


def display_data(data):
    output = []

    for row in data:
        print(row)
        output.append(f"ID={row[0]}, NAME={row[1]}, PRICE={row[2]}.")

    print("<br>\n".join(output))


db = MyDatabase('database_products.db')
products = Model(db, "products", ['ID', 'NAME', 'PRICE'], [
    Field('ID', "INT"),
    Field('NAME'),
    Field('PRICE')
])
db.create_table(products)
products.create([1, 'Pencil', 123])
products.create([2, 'Paper', 456])

orders = Model(db, "orders", ['ID', 'FK_PRODUCT_ID', 'QTY'], [
    Field('ID', "INT"),
    Field('FK_PRODUCT_ID', "INT"),
    Field('QTY')
])
db.create_table(orders)
orders.create([1, 1, 2])
orders.create([2, 2, 12])

data = products.read()
display_data(data)

print(orders.read())
print(orders.read(custom_sql="""
SELECT PRODUCTS.name, ORDERS.QTY, products.PRICE, ORDERS.QTY * products.PRICE AS ext
FROM ORDERS
    LEFT JOIN PRODUCTS
        ON orders.FK_PRODUCT_ID = products.ID;
"""))

print(orders.read(custom_sql="""
SELECT SUM(ORDERS.QTY * products.PRICE) AS total
FROM ORDERS
    LEFT JOIN PRODUCTS
        ON orders.FK_PRODUCT_ID = products.ID
"""))

db.connection.close()
"""
         DBSQL    HTTP/REST(METHODS/VERBS)
CREATE - INSERT - PUT
READ   - SELECT - GET
UPDATE - UPDATE - POST
DELETE - DELETE - DELETE

SELECT PRODUCTS.name, ORDERS.QTY, products.PRICE, ORDERS.QTY * products.PRICE AS ext
FROM ORDERS
    LEFT JOIN PRODUCTS
        ON orders.FK_PRODUCT_ID = products.ID;
        
SELECT SUM(ORDERS.QTY * products.PRICE) AS total
FROM ORDERS
    LEFT JOIN PRODUCTS
        ON orders.FK_PRODUCT_ID = products.ID

"""
