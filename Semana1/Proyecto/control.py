import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
from datetime import datetime
from time import strftime
import mysql.connector

mydb = mysql.connector.connect(
    host="bhjecoipc6kd7aixmfxg-mysql.services.clever-cloud.com",
    user="uajri3l438stpxax",
    password="8ib2R16UXJFszi2pTIVe",
    database="bhjecoipc6kd7aixmfxg"
)

class App:
    def __init__(self, root):
        #setting title
        root.title("CONTROL")
        #setting window size
        width=240
        height=200
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_254=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_254["font"] = ft
        GLabel_254["fg"] = "#333333"
        GLabel_254["justify"] = "center"
        GLabel_254["text"] = "ID"
        GLabel_254.place(x=10,y=50,width=70,height=25)

        GButton_652=tk.Button(root)
        GButton_652["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_652["font"] = ft
        GButton_652["fg"] = "#000000"
        GButton_652["justify"] = "center"
        GButton_652["text"] = "Enviar"
        GButton_652.place(x=80,y=160,width=80,height=25)
        GButton_652["command"] = self.GButton_652_command

        GLineEdit_436=tk.Entry(root)
        GLineEdit_436["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_436["font"] = ft
        GLineEdit_436["fg"] = "#333333"
        GLineEdit_436["justify"] = "center"
        GLineEdit_436["text"] = ""
        GLineEdit_436.place(x=110,y=50,width=120,height=25)

        GLabel_455=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_455["font"] = ft
        GLabel_455["fg"] = "#333333"
        GLabel_455["justify"] = "center"
        GLabel_455["text"] = "Contraseña"
        GLabel_455.place(x=10,y=100,width=70,height=25)

        GLineEdit_513=tk.Entry(root)
        GLineEdit_513["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_513["font"] = ft
        GLineEdit_513["fg"] = "#333333"
        GLineEdit_513["justify"] = "center"
        GLineEdit_513["text"] = ""
        GLineEdit_513.place(x=110,y=100,width=120,height=25)

        GLabel_249=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_249["font"] = ft
        GLabel_249["fg"] = "#333333"
        GLabel_249["justify"] = "center"
        GLabel_249["text"] = "CONTROL DE ASISTENCIA"
        GLabel_249.place(x=40,y=10,width=160,height=25)

        self.user = GLineEdit_436
        self.password = GLineEdit_513

         
    def GButton_652_command(self):
        
        mypassword_queue =[]
        sql_query = "SELECT *FROM Alumnos WHERE user ='%s' and password ='%s'" %(self.user.get(), self.password.get())
        mycursor = mydb.cursor()

        try:
            mycursor.execute(sql_query)
            myresults =mycursor.fetchall()
            for row in myresults:
                for x in row:
                    mypassword_queue.append(x)
        except:
            print('error occured')
        if (self.user.get() and self.password.get()) in mypassword_queue:
            now = datetime.now() 
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            sqlInsertar = "insert into Asistencia(id_alumno,fechas) values(%s,%s)"
            parametros = (mypassword_queue[0],dt_string)
            self.ejecutarSql(sqlInsertar,parametros)
            messagebox.showinfo("Asistencia Exitosa", "Asistencia registrada con Exito")
            
            self.user.delete(0, 'end')
            self.password.delete(0, 'end')
        else:
            messagebox.showerror("Asistencia Fallida", "Usuario o Contraseña Invalida")
            
            
    def ejecutarSql(self,sql,parametros = ()):
        mycursor = mydb.cursor()
        mycursor.execute(sql,parametros)
        mydb.commit()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
       