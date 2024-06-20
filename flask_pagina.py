from flask import Flask, render_template, redirect, url_for
from lookup import Engine

app = Flask(__name__)
engine = Engine()

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/function_one')
def Player():
    result = engine.PlayerLookup()
    return redirect(url_for('home', result=result))

@app.route('/function_two')
def Brawler():
    result = engine.BrawlerLookup()
    return redirect(url_for('home', result=result))

@app.route('/function_three')
def Ranking():
    result = engine.rankingLookup()
    return redirect(url_for('home', result=result))

if __name__ == '__main__':
    app.run(debug=True)