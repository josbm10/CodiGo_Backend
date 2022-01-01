import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox
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
        root.title("REGISTRO")
        #setting window size
        width=240
        height=300
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
        GLabel_254["text"] = "Usuario"
        GLabel_254.place(x=20,y=50,width=70,height=25)

        GButton_652=tk.Button(root)
        GButton_652["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_652["font"] = ft
        GButton_652["fg"] = "#000000"
        GButton_652["justify"] = "center"
        GButton_652["text"] = "Enviar"
        GButton_652.place(x=80,y=250,width=80,height=25)
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
        GLabel_455.place(x=20,y=100,width=70,height=25)

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
        GLabel_249["text"] = "REGISTRO ALUMNO NUEVO"
        GLabel_249.place(x=30,y=10,width=180,height=25)

        GLabel_955=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_955["font"] = ft
        GLabel_955["fg"] = "#333333"
        GLabel_955["justify"] = "center"
        GLabel_955["text"] = "Nombre"
        GLabel_955.place(x=20,y=150,width=70,height=25)

        GLineEdit_107=tk.Entry(root)
        GLineEdit_107["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_107["font"] = ft
        GLineEdit_107["fg"] = "#333333"
        GLineEdit_107["justify"] = "center"
        GLineEdit_107["text"] = ""
        GLineEdit_107.place(x=110,y=150,width=120,height=25)

        GLineEdit_81=tk.Entry(root)
        GLineEdit_81["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_81["font"] = ft
        GLineEdit_81["fg"] = "#333333"
        GLineEdit_81["justify"] = "center"
        GLineEdit_81["text"] = ""
        GLineEdit_81.place(x=110,y=200,width=120,height=25)

        GLabel_77=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_77["font"] = ft
        GLabel_77["fg"] = "#333333"
        GLabel_77["justify"] = "center"
        GLabel_77["text"] = "Apellido"
        GLabel_77.place(x=20,y=200,width=70,height=25)
        
        self.user = GLineEdit_436
        self.password = GLineEdit_513
        self.name = GLineEdit_107
        self.lastname = GLineEdit_81
    
    def ejecutarSql(self,sql,parametros = ()):
        mycursor = mydb.cursor()
        mycursor.execute(sql,parametros)
        mydb.commit()
        #resultado = mycursor.fetchall()
        #return resultado

    def GButton_652_command(self):
        sqlInsertar = "insert into Alumnos(user,password,name,lastname) values(%s,%s,%s,%s)"
        parametros = (self.user.get(),self.password.get(),self.name.get(),self.lastname.get())
        print(sqlInsertar)
        print(parametros)
        self.ejecutarSql(sqlInsertar,parametros)
        messagebox.showinfo("Registro Exitoso", "Alumno registrado con Exito")
        self.user.delete(0, 'end')
        self.password.delete(0, 'end')
        self.name.delete(0, 'end')
        self.lastname.delete(0, 'end')

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
