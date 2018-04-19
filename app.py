from flask import Flask , render_template , request , jsonify
from textblob import *
import random as rn 
app= Flask(__name__,template_folder='template')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process')
def blob():
    a=rn.random()*10
    b=(a+6*a)*a
    return render_template('result.html', state=b)

if __name__ == '__main__':
        app.run(debug=True)
