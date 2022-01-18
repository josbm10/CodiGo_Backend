from flask import render_template
# importamos la funcion create_app desde la aplicaion app
from app import create_app

app=create_app()

@app.route('/')
def index():
    return render_template('index.html')