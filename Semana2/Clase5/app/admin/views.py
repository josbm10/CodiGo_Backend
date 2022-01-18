#importamos render_template para renderizar plantillas de jinja2
from flask import render_template,flash,redirect,url_for,session

#importamos el init de admin
from . import admin

#importamos los formularios
from app.forms import LoginForm,ProyectoForm

########### FIREBASE ###############

import pyrebase

config = {
   "apiKey": "AIzaSyBxlOdTIwXQHjhYCy0cHpbUbS_NEDRakao",
  "authDomain": "portafolio-3139f.firebaseapp.com",
  "databaseURL": "https://portafolio-3139f-default-rtdb.firebaseio.com",
  "projectId": "portafolio-3139f",
  "storageBucket": "portafolio-3139f.appspot.com",
  "messagingSenderId": "172341673963",
  "appId": "1:172341673963:web:4ed52adb00b24ec19f63ae",
  "measurementId": "G-Y20FMQ7RWX"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
#####################################

############# FIRESTORE ##################################
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("firebasetoken.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
#########################################################


@admin.route('/login',methods=['GET','POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form':login_form
    }
    #CODIGO PARA REALIZAR EL LOGIN DE USUARIOS
    if login_form.validate_on_submit():
        #CAPTURAMOS VALORES DE USUARIO Y PASSWORD
        usuarioData = login_form.usuario.data
        passwordData = login_form.password.data
        print("DATOS DE LOGIN :")
        print("usuario : " + usuarioData)
        print("password: " + passwordData)
        
        #REALIZAMOS EL LOGIN DE USUARIO CON FIREBASE
        try:
            usuario = auth.sign_in_with_email_and_password(usuarioData,passwordData)
            session['token'] = usuario['idToken']
            return redirect(url_for('admin.proyectos'))
            #flash(auth.get_account_info(usuario['idToken']))
        except:
            flash("usuario o password invalidos")
    
    return render_template('admin/login.html',**context)

@admin.route('/proyectos',methods=['GET','POST'])
def proyectos():
    if('token' in session):
        
        colProyectos = db.collection('proyecto')
        proyecto_form = ProyectoForm()
        
        if proyecto_form.validate_on_submit():
            #CAPTURAMOS VALORES DE USUARIO Y PASSWORD
            nombreData = proyecto_form.nombre.data
            descripcionData = proyecto_form.descripcion.data
            urlData = proyecto_form.url.data
            
            #CREAR DICCIONARIO
            data = {
                'nombre': nombreData,
                'descripcion':descripcionData,
                'url':urlData
            }
            
            colProyectos.document().set(data)
        
        docProyectos = colProyectos.get()
        
        lstProyectos = []
        for doc in docProyectos:
            dicProyecto = doc.to_dict()
            lstProyectos.append(dicProyecto)
    
        print(lstProyectos)

        context = {
            'proyectos':lstProyectos,
            'proyecto_form':proyecto_form
        }
        
        return render_template('admin/proyectos.html',**context)
    else:
        return redirect(url_for('admin.login'))
    
@admin.route('/logout')
def logout():
    session.pop('token')
    return redirect(url_for('admin.login'))