from click.core import Context
from flask import Flask,render_template
from flask_mysqldb import MySQL
from flask import request


app=Flask(__name__)

app.config['MYSQL_HOST']='bhjecoipc6kd7aixmfxg-mysql.services.clever-cloud.com'
app.config['MYSQL_USER']='uajri3l438stpxax'
app.config['MYSQL_PASSWORD']='8ib2R16UXJFszi2pTIVe'
app.config['MYSQL_DB']='bhjecoipc6kd7aixmfxg'

mysql=MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
     cursor = mysql.connection.cursor()
     cursor.execute('select id,user,name,lastname from Alumnos')
     data=cursor.fetchall()
     cursor.close()
     context = {
        'data':data
      }
    
     return render_template('index.html',**context)

@app.route('/asistencia.html', methods=['GET', 'POST'])
def asistencia():   
    if request.method == 'POST':
        if request.form['btn']:
            id=request.form['btn']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT *FROM Asistencia WHERE id_alumno ='%s'" %(id))
    data=cursor.fetchall()
    cursor.close()

    context = {
        'data':data
    }
    
    
    return render_template('asistencia.html',**context)


app.run(debug=True,port=4000)