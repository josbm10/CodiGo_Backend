import os
from flask import Flask,render_template

app=Flask(__name__)

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred =credentials.Certificate("firebasetoken.json")
firebase_admin.initialize_app(cred)

db=firestore.client()

@app.route('/')
def home():
    context={
        'nombre':'Leonel Briceño',
        'imagen':'https://4.bp.blogspot.com/-4wFittXkWic/WcUV9ZWrWYI/AAAAAAAASfo/FUZHGHDzS2khH11OgMIjL_SzdYTCQqHAACLcBGAs/s1600/POSTER%2BDE%2BPERFIL%2BDE%2BDARTH%2BVADER%2BEN%2BSTAR%2BWARS%2BROGUE%2BONE.png',
        'bio':'Programador'
    }
    return render_template('home.html',**context)

@app.route('/portafolio')
def portafolio():
    colProyectos=db.collection('proyecto')
    docProyectos=colProyectos.get()
    lstProyecto=[]
    for doc in docProyectos:
        print(doc.to_dict())
        dicProyecto=doc.to_dict()
        lstProyecto.append(dicProyecto)
        
        context={
            'proyectos':lstProyecto
        }
        
    return render_template('portafolio.html',**context)
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__=='__main__':
    app.run(debug=True,port=5000)
    
