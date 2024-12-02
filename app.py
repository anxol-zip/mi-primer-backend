from operator import index

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('pages/index.html')

@app.route('/index.html')
def homeX():
    return render_template('pages/index.html')

@app.route('/sub-page/canva.html')
def canva():
    return render_template('pages/sub-page/canva.html')

@app.route('/sub-page/Web 1/index.html')
def web1():
    return render_template('pages/sub-page/Web 1/index.html')

@app.route('/sub-page/Web 1/secundarias/yo.html')
def web1yo():
    return render_template('pages/sub-page/Web 1/secundarias/yo.html')

@app.route('/sub-page/Web 1/secundarias/habilidades.html')
def web1habilidades():
    return render_template('pages/sub-page/Web 1/secundarias/habilidades.html')

@app.route('/sub-page/Web 1/secundarias/gustos.html')
def web1gustos():
    return render_template('pages/sub-page/Web 1/secundarias/gustos.html')

@app.route('/sub-page/GitHub/github.html')
def github():
    return render_template('pages/sub-page/GitHub/github.html')

@app.route('/sub-page/GitHub/magic.html')
def githubmagic():
    return render_template('pages/sub-page/GitHub/magic.html')

@app.route('/sub-page/var.html')
def var():
    return render_template('pages/sub-page/var.html')

@app.route('/sub-page/3D-Scan.html')
def scan():
    return render_template('pages/sub-page/3D-Scan.html')

@app.route('/sub-page/3D-Print.html')
def print():
    return render_template('pages/sub-page/3D-Print.html')

@app.route('/sub-page/Hangman/hangman.html')
def hangman():
    return render_template('pages/sub-page/Hangman/hangman.html')

@app.route('/sub-page/Hangman/pythonversion.html')
def hangmanpython():
    return render_template('pages/sub-page/Hangman/pythonversion.html')

@app.route('/sub-page/Hangman/troll.html')
def hangmantroll():
    return render_template('pages/sub-page/Hangman/troll.html')

@app.route('/sub-page/frameworks.html')
def frameworks():
    return render_template('pages/sub-page/frameworks.html')

@app.route('/sub-page/back-end.html')
def backend():
    return render_template('pages/sub-page/backend/back-end.html')

if __name__ == '__main__':
    app.run(debug=True)