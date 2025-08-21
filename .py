from tkinter import *
from tkinter import messagebox
#------------------------------------------------------
# ventana principal
#------------------------------------------------------

ventana = Tk()
ventana.title("Todo de la vida de Soreth")
ventana.geometry("800x600")
ventana.config(bg="violet")
# abrir toplevel centigrados
def abrir_toplevel_ventana1():
    global toplevel_ventana1
    toplevel_ventana1 = Toplevel()
    toplevel_ventana1.title("Centigrados")
    toplevel_ventana1.resizable(False, False)
    toplevel_ventana1.geometry("300x200")
    toplevel_ventana1.config(bg="white")

def abrir_toplevel_ventana2():
    global toplevel_ventana2
    toplevel_ventana2 = Toplevel()
    toplevel_ventana2.title("Centigrados")
    toplevel_ventana2.resizable(False, False)
    toplevel_ventana2.geometry("300x200")
    toplevel_ventana2.config(bg="white")

def abrir_toplevel_ventana3():
    global toplevel_ventana3
    toplevel_ventana3 = Toplevel()
    toplevel_ventana3.title("Centigrados")
    toplevel_ventana3.resizable(False, False)
    toplevel_ventana3.geometry("300x200")
    toplevel_ventana3.config(bg="white")

def abrir_toplevel_ventana4():
    global toplevel_ventana4
    toplevel_ventana4 = Toplevel()
    toplevel_ventana4.title("Centigrados")
    toplevel_ventana4.resizable(False, False)
    toplevel_ventana4.geometry("300x200")
    toplevel_ventana4.config(bg="white")

def abrir_toplevel_ventana5():
    global toplevel_ventana5
    toplevel_ventana5 = Toplevel()
    toplevel_ventana5.title("Centigrados")
    toplevel_ventana5.resizable(False, False)
    toplevel_ventana5.geometry("300x200")
    toplevel_ventana5.config(bg="white")

def abrir_toplevel_ventana6():
    global toplevel_ventana6
    toplevel_ventana6 = Toplevel()
    toplevel_ventana6.title("Centigrados")
    toplevel_ventana6.resizable(False, False)
    toplevel_ventana6.geometry("300x200")
    toplevel_ventana6.config(bg="white")

def abrir_toplevel_ventana7():
    global toplevel_ventana6
    toplevel_ventana7 = Toplevel()
    toplevel_ventana7.title("Centigrados")
    toplevel_ventana7.resizable(False, False)
    toplevel_ventana7.geometry("300x200")
    toplevel_ventana7.config(bg="white")

def abrir_toplevel_ventana8():
    global toplevel_ventana3
    toplevel_ventana8 = Toplevel()
    toplevel_ventana8.title("Centigrados")
    toplevel_ventana8.resizable(False, False)
    toplevel_ventana8.geometry("300x200")
    toplevel_ventana8.config(bg="white")

# salir
def salir():
    messagebox.showinfo("Temperatura 1.0", "La app se va a cerrar")
    ventana.destroy()



# etiqueta para el titulode la app
titulo = Label(ventana,text="Soreth Flórez")
titulo.config(bg="pink", fg="white",font=("arial",16))
titulo.place(x=10,y=560)




#--------------------------------
# barra menu
#--------------------------------
barra_menu = Menu()
ventana.config(menu=barra_menu)


# boton para abrir Toplevel ventana1
bt_ventana1 = Button(ventana, text="Nacimiento", command=abrir_toplevel_ventana1)
bt_ventana1.place(x=10, y=190)

# boton para abrir Toplevel ventana2
bt_ventana1 = Button(ventana, text="Datos médicos", command=abrir_toplevel_ventana2)
bt_ventana1.place(x=10, y=230)

# boton para abrir Toplevel ventana3
bt_ventana3 = Button(ventana, text="Familia", command=abrir_toplevel_ventana3)
bt_ventana3.place(x=10, y=270)

# boton para abrir Toplevel ventana4
bt_ventana3 = Button(ventana, text="Familia", command=abrir_toplevel_ventana3)
bt_ventana3.place(x=10, y=310)

# boton para abrir Toplevel ventana5
bt_ventana3 = Button(ventana, text="Familia", command=abrir_toplevel_ventana3)
bt_ventana3.place(x=10, y=350)

# boton para abrir Toplevel ventana6
bt_ventana3 = Button(ventana, text="Familia", command=abrir_toplevel_ventana3)
bt_ventana3.place(x=10, y=390)

# boton para abrir Toplevel ventana7
bt_ventana3 = Button(ventana, text="Familia", command=abrir_toplevel_ventana3)
bt_ventana3.place(x=10, y=430)

# boton para abrir Toplevel ventana8
bt_ventana3 = Button(ventana, text="Familia", command=abrir_toplevel_ventana3)
bt_ventana3.place(x=10, y=470)

menu_convertir = Menu(tearoff=0)
menu_convertir.add_command(label="Opciones")
menu_convertir.add_separator()
menu_convertir.add_command(label="Borrar")


menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir", command=salir)


# boton para salir
bt_salir = Button(ventana,text="Salir", command=salir)
bt_salir.place(x=677, y=562, width=100, height=30)


ventana.mainloop()