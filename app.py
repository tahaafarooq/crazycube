from flask import Flask, request, render_template, abort

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass


@app.route('/register', methods=['GET', 'POST'])
def register():
    pass


@app.route('/game', methods=['GET', 'POST'])
def game():
    pass


@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    pass
