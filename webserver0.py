from flask import Flask, redirect, request, session

app = Flask(__name__)
app.secret_key = b'kevinelong'


@app.route('/')
def index():
    return '''
Hi!
<form method="POST" action="/login/">
    <input name="username" placeholder="username">
    <input name="password" type="password" placeholder="password">
    <input type="submit" value="Login">
</form>
    '''


@app.route('/login/', methods=['POST'])
def login():
    username = request.form['username']

    print(f"RECEIVED: {username}")
    return f'''
    WELCOME {username}!!!
<br>
    <a href="http://google.com"> 
        Go to google
    </a>
<br>
    <a href="/secure/?username={username}"> 
        Go to secure
    </a>


    '''


# @app.route('/secure/*')
# def secure():
#     username = request.form['username']
#     print(f"RECEIVED: {username}")
#     return f'''
#     SECRET STUFF for {username}!!!
#     '''


app.run()
