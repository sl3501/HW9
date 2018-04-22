from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def quotations():
    server = 'My server' 
    return render_template('dailyQuote.html',  server=server)
