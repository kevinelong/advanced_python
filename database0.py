import sqlite3
try:
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.executescript("""DROP TABLE IF EXISTS Pets;
            CREATE TABLE Pets(Id INT, Name TEXT, Price INT); 
            INSERT INTO Pets VALUES(1, 'Cat', 400);
            INSERT INTO Pets VALUES(2, 'Dog', 600);""")
    pets = ((3, 'Rabbit', 200),
            (4, 'Bird', 60),
            (5, 'Goat', 500))
    cur.executemany("INSERT INTO Pets VALUES(?, ?, ?)", pets)
    con.commit()

    cur.execute("SELECT * FROM Pets")
    data = cur.fetchall()
    for row in data:
        print(row)
except sqlite3.Error as e:
    if con:
        con.rollback()
finally:
    if con:
        con.close()

# SELECT quantity, price, product, (quantity * price) AS extended FROM orders