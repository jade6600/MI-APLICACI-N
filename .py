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
    toplevel_ventana1.title("NACIMIENTO")
    toplevel_ventana1.resizable(False, False)
    toplevel_ventana1.geometry("400x300")
    toplevel_ventana1.config(bg="white")
    Label(toplevel_ventana1, text="Nací el 3 de Mayo del 2010(Acepto regalos)\nBucaramanga-Santander\nen el hosipital Universitario de Santander\n A las 2:15am", bg="white").pack(pady=50)


def abrir_toplevel_ventana2():
    global toplevel_ventana2
    toplevel_ventana2 = Toplevel()
    toplevel_ventana2.title("DATOS MÉDICOS")
    toplevel_ventana2.resizable(False, False)
    toplevel_ventana2.geometry("400x300")
    toplevel_ventana2.config(bg="white")
    Label(toplevel_ventana2, text="Tipo de sangre: A+\n EPS: Nueva EPS\nEstatura:1,61m\nPeso:No sea sapo ", bg="white").pack(pady=50)


def abrir_toplevel_ventana3():
    global toplevel_ventana3
    toplevel_ventana3 = Toplevel()
    toplevel_ventana3.title("FAMILIA")
    toplevel_ventana3.resizable(False, False)
    toplevel_ventana3.geometry("400x300")
    toplevel_ventana3.config(bg="white")
    Label(toplevel_ventana3, text="Actualmente vivo con\n mis papás\n Liceth Peñaloza Castro y Rosemberg Flórez Sierra\nMi hermana: Allison Flórez", bg="white").pack(pady=50)

def abrir_toplevel_ventana4():
    global toplevel_ventana4
    toplevel_ventana4 = Toplevel()
    toplevel_ventana4.title("EDUCACIÓN")
    toplevel_ventana4.resizable(False, False)
    toplevel_ventana4.geometry("400x300")
    toplevel_ventana4.config(bg="white")
    Label(toplevel_ventana4, text="He estado en varios colegios a lo largo de mi vida:\nNuestra Señora de la Paz(San Vicente de Chucurí)\nColegio municipal de Tona(Tona)\nCarlos  Martinez(Girón)\nColegio Guuanentá.", bg="white").pack(pady=50)

def abrir_toplevel_ventana5():
    global toplevel_ventana5
    toplevel_ventana5 = Toplevel()
    toplevel_ventana5.title("AMIGOS")
    toplevel_ventana5.resizable(False, False)
    toplevel_ventana5.geometry("500x300")
    toplevel_ventana5.config(bg="white")
    Label(toplevel_ventana5, text="Mis amiguitos del colegio los conocí en su mayoría en el grado séptimo y son:\nSaray(Dibujo técnico)\nManuel(Sistemas2)\nOscar(El mejor sistemas)\nJuanjosé(Sistemas2)\nLeyner(Dibujo)\nHenry(diseño)\nMiguel(El mejor sistemas).\nLos aprecio mucho aunque a veces sean muy ardidos en el fútbol", bg="white").pack(pady=50)

def abrir_toplevel_ventana6():
    global toplevel_ventana6
    toplevel_ventana6 = Toplevel()
    toplevel_ventana6.title("HOBBIES")
    toplevel_ventana6.resizable(False, False)
    toplevel_ventana6.geometry("450x300")
    toplevel_ventana6.config(bg="white")
    Label(toplevel_ventana6, text="Me gustan mucho ver series,\n" \
    " además de leer, considero que mi libro favorito es\nEl retrato de Dorian Grey,\n me gusta pintar y hacer programitas cuando entiendo", bg="white").pack(pady=50)

def abrir_toplevel_ventana7():
    global toplevel_ventana7
    toplevel_ventana7 = Toplevel()
    toplevel_ventana7.title("HORARIOS")
    toplevel_ventana7.resizable(False, False)
    toplevel_ventana7.geometry("500x300")
    toplevel_ventana7.config(bg="white")
    Label(toplevel_ventana7, text="Mi rutina es muy variada como tal me levanto a las /:00amn\nLos miércoles y viernes voy a clases de mi especialidad a las 6:00am\n normalmente mi horario de clase en la tarde es de 12:30-6:30\n Mi día termina normalmente a las 11:00pm ", bg="white").pack(pady=50)
   
def abrir_toplevel_ventana8():
    global toplevel_ventana8
    toplevel_ventana8 = Toplevel()
    toplevel_ventana8.title("ICFES")
    toplevel_ventana8.resizable(False, False)
    toplevel_ventana8.geometry("420x300")
    toplevel_ventana8.config(bg="white")
    Label(toplevel_ventana8, text="Intento prepararme leyendo mucho sobretodo en inglés\n ya que no es mi fuerte, tambein \n Practico algunos ejercicios en el salón de sistemas los días miércoles", bg="white").pack(pady=50)

def abrir_toplevel_ventana9():
    global toplevel_ventana9
    toplevel_ventana9 = Toplevel()
    toplevel_ventana9.title("PROYECTO DE VIDA")
    toplevel_ventana9.resizable(False, False)
    toplevel_ventana9.geometry("400x300")
    toplevel_ventana9.config(bg="white")
    Label(toplevel_ventana9, text="Mi proyecto al salir del colegio es\n estudiar \nIngeniería Química\n ya que es una área que me gusta mucho aunque me gustaría seguir con mis hobbies como la pintura.", bg="white").pack(pady=50)
   
def abrir_toplevel_ventana10():
    global toplevel_ventana10
    toplevel_ventana10= Toplevel()
    toplevel_ventana10.title("serie fav")
    toplevel_ventana10.resizable(False, False)
    toplevel_ventana10.geometry("800x600")
    toplevel_ventana10.config(bg="white")
    Label(toplevel_ventana10, text="Rebelde Way es una telenovela juvenil argentina creada por Cris Morena, emitida entre 2002 y 2003.\nLa historia transcurre principalmente en el Elite Way School,\nun colegio privado de prestigio donde conviven adolescentes de familias ricas con becados de origen humilde.\nLos protagonistas son Mía Colucci, Marizza Pía Spirito,\nPablo Bustamante y Manuel Aguirre,\nquienes al principio tienen choques por sus diferencias sociales y de carácter\n pero terminan formando una profunda amistad.\nLos cuatro crean una banda musical llamada Erreway, que se convierte en una parte clave de sus vidas\ny de la serie, ya que a través de la música expresan sus sentimientos,\nsueños y rebeldía.\nA lo largo de la trama se abordan temas típicos de la adolescencia como la amistad, el primer amor, los conflictos familiares,\nlas injusticias sociales,\nla identidad y la búsqueda de independencia.\nTambién aparecen intrigas escolares\n rivalidades, romances cruzados y enfrentamientos con adultos que representan la autoridad.\nLa serie tuvo 2 temporadas (318 capítulos en total)\ny marcó a toda una generación en varios países, siendo la base de adaptaciones posteriores como la mexicana Rebelde (RBD).", bg="white").pack(pady=50)

# salir
def salir():
    messagebox.showinfo("Todo de la vida de Soreth", "La app se cerrrá en breve...")
    ventana.destroy()



# etiqueta para el titulode la app
titulo = Label(ventana,text="Soreth Flórez")
titulo.config(bg="pink", fg="white",font=("arial",18))
titulo.place(x=310,y=80)


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
bt_ventana3 = Button(ventana, text="Educación", command=abrir_toplevel_ventana4)
bt_ventana3.place(x=10, y=310)

# boton para abrir Toplevel ventana5
bt_ventana3 = Button(ventana, text="Amigos", command=abrir_toplevel_ventana5)
bt_ventana3.place(x=10, y=350)

# boton para abrir Toplevel ventana6
bt_ventana3 = Button(ventana, text="Hobbies", command=abrir_toplevel_ventana6)
bt_ventana3.place(x=10, y=390)

# boton para abrir Toplevel ventana7
bt_ventana3 = Button(ventana, text="Horarios", command=abrir_toplevel_ventana7)
bt_ventana3.place(x=10, y=430)

# boton para abrir Toplevel ventana8
bt_ventana3 = Button(ventana, text="Planificación prueba saber 11 (ICFES)", command=abrir_toplevel_ventana8)
bt_ventana3.place(x=10, y=470)

# boton para abrir Toplevel ventana9
bt_ventana3 = Button(ventana, text="Proyecto de vida", command=abrir_toplevel_ventana9)
bt_ventana3.place(x=10, y=510)

# boton para abrir Toplevel ventana10
bt_ventana3 = Button(ventana, text="Mi serie fav", command=abrir_toplevel_ventana10)
bt_ventana3.place(x=10, y=550)



menu_salir = Menu(tearoff=0)
menu_salir.add_command(label="Salir", command=salir)


# boton para salir
bt_salir = Button(ventana,text="Salir", command=salir)
bt_salir.place(x=677, y=562, width=100, height=30)


ventana.mainloop()