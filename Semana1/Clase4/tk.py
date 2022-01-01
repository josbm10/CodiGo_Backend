from tkinter import *
from tkinter import messagebox


app=Tk()
app.title("APP")
app.geometry('235x60')

def saludar():
    messagebox.showinfo("title","hola "+ txtNombre.get())

# creamos un frame
frame=LabelFrame(app,text='Frame')
frame.grid(row=0,column=0,columnspan=3,pady=10)
lbNombre=Label(frame,text='Nombre')
lbNombre.grid(row=1,column=0)
txtNombre=Entry(frame)
txtNombre.grid(row=1,column=1)
btnSaludar=Button(frame,text='saludar',command=saludar)
btnSaludar.grid(row=1,column=2)


app.mainloop()