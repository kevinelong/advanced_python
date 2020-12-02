from flask import Flask, make_response
import sqlite3
import json
app = Flask(__name__)

style = """
<style>
    body{
        background: green;
    }
</style>
"""

@app.route('/')
def index():
    return f"{style}" + open("webserver2_template.html", "r").read()

@app.route('/pets/')
def pets():
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM Pets")
    data = cur.fetchall()
    names = []
    for d in data:
        names.append(f"<b>{d[1]}</b>")
    html = "<br>".join(names)
    return f"{html}"

@app.route('/data/')
def data():
    con = sqlite3.connect('test.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM Pets")
    data = cur.fetchall()
    response = make_response(json.dumps(data, indent=4))
    response.headers['Content-Type'] = 'application/json'
    return response
app.run()