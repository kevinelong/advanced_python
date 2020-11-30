from flask import Flask, redirect, request, session

app = Flask(__name__)
app.secret_key = b'kevinelong'

@app.route('/', methods=['POST','GET'])
def index():
    if "username" in dict(request.form):
        username = request.form['username']
        print(f"RECEIVED: {username}")
        return f'''
        WELCOME {username}!!!
        '''
    else:
        return '''
    Hi!
    <form method="POST">
        <input name="username">
        <input name="password" type="password">
        <input type="submit">
    </form>
    '''



app.run()
