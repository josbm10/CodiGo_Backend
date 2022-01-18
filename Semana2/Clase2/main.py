from flask import Flask,request,render_template
import requests

app = Flask(__name__)

URL='https://api.github.com/users/josbm10'

data=requests.get(URL)
context=data.json()
print(context)


lstproducto=['laptop','radio','televisor']
@app.route('/index')
def index():
    nombre=request.args.get('nombre','no hay nombre')
    
    context={
        'nombre':nombre,
        'productos':lstproducto
    }
    return render_template('index.html',**context)
@app.route('/portafolio')
def portafolio():

    return render_template('portafolio.html')

@app.route('/')
def home():

    return render_template('home.html',**context)

@app.route('/about')
def about():

    return render_template('about.html')

@app.route('/contact')
def contact():

    return render_template('contact.html')

if __name__ == '__main':
    app.run(debug = True,port=5001)