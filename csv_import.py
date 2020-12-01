import csv
import sqlite3

f = open("Pets.csv", "r")
r = csv.reader(f)

con = sqlite3.connect('test.db')
cur = con.cursor()

cur.executemany("INSERT INTO Pets VALUES(?, ?, ?)", r)
con.commit()
