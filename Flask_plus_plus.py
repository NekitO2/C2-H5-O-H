from flask import Flask

app = Flask(__name__)

@app.route('/1')

def first():
    return '<h1>First page</h1><p>Привет,</p>'
@app.route('/2')

def second():
    return '<h1>Second page</h1><p>человек!</p>'
@app.route('/3')

def third():
    return '<h1>Third page</h1><p>Ты</p>'
@app.route('/4')

def fourth():
    return '<h1>Fourth page</h1><p>же</p>'
@app.route('/5')

def fifth():
    return '<h1>Fifth page</h1><p>человек,</p>'
@app.route('/6')

def sixth():
    return '<h1>Sixth page</h1><p>верно?</p>'

@app.route('/7')

def seventh():
    return '<h1>Seventh page</h1><p>......</p>'

app.run()