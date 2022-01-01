from click.core import Context
from flask import Flask,render_template
from flask_mysqldb import MySQL


app=Flask(__name__)

app.config['MYSQL_HOST']='bhjecoipc6kd7aixmfxg-mysql.services.clever-cloud.com'
app.config['MYSQL_USER']='uajri3l438stpxax'
app.config['MYSQL_PASSWORD']='8ib2R16UXJFszi2pTIVe'
app.config['MYSQL_DB']='bhjecoipc6kd7aixmfxg'

mysql=MySQL(app)

@app.route('/')
def index():
    cursor = mysql.connection.cursor()
    cursor.execute('select id,sistema,procesador,memoria from Computadoras')
    data=cursor.fetchall()
    cursor.close()
    print(data)
    
    context = {
        'data':data
    }
    
    return render_template('index.html',**context)

app.run(debug=True,port=4000)