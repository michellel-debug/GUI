from tkinter import *
from tkinter import ttk
import tkinter as tk

raiz = Tk()
raiz.title("Formulario")
#marcoPrincipal = ttk.Frame(raiz, padding= "10 10 10 10")
marcoPrincipal = tk.Frame(bg='pink')
marcoPrincipal.grid(column=0, row=0)

marcoSecundario = tk.Frame(marcoPrincipal, bg='white', bd=15, relief=RIDGE)
#marcoSecundario = ttk.Frame(padding= "10")
marcoSecundario.grid(column=0, row=0) 

#Textbox nombre    
txtName = ttk.Entry(marcoSecundario, width=20)
txtName.grid(column=1, row=0)

tk.Label(marcoSecundario, text="Nombre:", bg='white').grid(column=0, row=0)     

#textbox a. paterno
txtPaterno = ttk.Entry(marcoSecundario, width=20)
txtPaterno.grid(column=1, row=1)

tk.Label(marcoSecundario, text="A. Paterno", bg='white').grid(column=0, row=1)

#textbox a. materno
txtMaterno = ttk.Entry(marcoSecundario, width=20)
txtMaterno.grid(column=1, row=2)

tk.Label(marcoSecundario, text="A. Marterno", bg='white').grid(column=0, row=2)

#textbox correo
txtCorreo = ttk.Entry(marcoSecundario, width=20)
txtCorreo.grid(column=1, row=3)

tk.Label(marcoSecundario, text="Correo", bg='white').grid(column=0, row=3)

#textbox movil
txtMovil = ttk.Entry(marcoSecundario, width=20)
txtMovil.grid(column=1, row=4)

tk.Label(marcoSecundario, text="Movil", bg='white').grid(column=0, row=4)

#Tercer frame
marcoTercer = tk.Frame(marcoPrincipal, bg='blue', bd=5, relief=RIDGE)
marcoTercer.grid(column=0, row=5, pady= 10, sticky=W)

#tabla de aficiones

tk.Label(marcoTercer, text="Aficiones:", bg="blue").grid(column=0, row=5)

aficiones = StringVar()
chkBoton = tk.Checkbutton(marcoTercer, text="Leer", bg="blue")
chkBoton.grid(column=0, row=6)
chkBoton = tk.Checkbutton(marcoTercer, text="Música", bg="blue")
chkBoton.grid(column=1, row=6)
chkBoton = tk.Checkbutton(marcoTercer, text="Videojuegos", bg="blue")
chkBoton.grid(column=2, row=6)

#Botones

tk.Button(marcoPrincipal, text="Guardar", width=10, bg="orchid1").grid(column=0, row=7, sticky=W, pady=10, padx=10)
tk.Button(marcoPrincipal, text="Cancelar", width=10, bg="orchid1").grid(column=2, row=7, sticky=W)



txtName.focus()
raiz.mainloop()