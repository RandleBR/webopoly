from bottle import route, run, template, get, post, request, static_file

from JewelMonopoly import addGamePiece



@route('/')
def server_static():
    return static_file('index.html', root='./public')

@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)

@get('/login') # or @route('/login')
def login():
    return '''
        <form action="/ticket" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''
@get('/gamepiece')
@post('/gamepiece')
@post('/newgamepiece') 
def do_gamepiece():
    ticket = request.forms.get('gamepiece')
    return addGamePiece(ticket)

@route('/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='./public')

run(host='localhost', port=8080)

