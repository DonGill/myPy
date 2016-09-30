from flask import render_template
from app import app, db

@app.route('/')
@app.route('/index')
def index():
   
    return render_template('index.html',
                           title='dongill.pythonanywhere.com',
                           )

