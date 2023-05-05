from tkinter import *
from tkinter import ttk
import tkinter as tk

raiz = Tk()
raiz.title("Formulario")

marcoPrincipal = tk.Frame(bg='pink')
marcoPrincipal.grid(column=0, row=0)

marcoSecundario = tk.Frame(marcoPrincipal, bg='white', bd=15, relief=RIDGE)
marcoSecundario.grid(column=0, row=0) 

#Textbox nombre    
txtName = ttk.Entry(marcoSecundario, width=20)
txtName.grid(column=1, row=0, pady=10, padx=10)

tk.Label(marcoSecundario, text="Nombre", bg='white').grid(column=0, row=0, pady=10, padx=10, sticky=W)     

#textbox a. paterno
txtPaterno = ttk.Entry(marcoSecundario, width=20)
txtPaterno.grid(column=1, row=1)

tk.Label(marcoSecundario, text="A. Paterno", bg='white').grid(column=0, row=1, pady=10, padx=10, sticky=W)

#textbox a. materno
txtMaterno = ttk.Entry(marcoSecundario, width=20)
txtMaterno.grid(column=1, row=2)

tk.Label(marcoSecundario, text="A. Marterno", bg='white').grid(column=0, row=2, pady=10, padx=10, sticky=W)

#textbox correo
txtCorreo = ttk.Entry(marcoSecundario, width=20)
txtCorreo.grid(column=1, row=3)

tk.Label(marcoSecundario, text="Correo", bg='white').grid(column=0, row=3, pady=10, padx=10, sticky=W)

#textbox movil
txtMovil = ttk.Entry(marcoSecundario, width=20)
txtMovil.grid(column=1, row=4)

tk.Label(marcoSecundario, text="Movil", bg='white').grid(column=0, row=4, pady=10, padx=10, sticky=W)

#Tercer frame
marcoTercer = tk.Frame(marcoPrincipal, bg='blue', bd=5, relief=RIDGE)
marcoTercer.grid(column=0, row=1, pady= 10, sticky=W)

#tabla de aficiones

tk.Label(marcoTercer, text="Aficiones:", bg="blue").grid(column=0, row=0)

aficiones = StringVar()
chkBoton = tk.Checkbutton(marcoTercer, text="Leer", bg="blue")
chkBoton.grid(column=0, row=1)
chkBoton = tk.Checkbutton(marcoTercer, text="Música", bg="blue")
chkBoton.grid(column=1, row=1)
chkBoton = tk.Checkbutton(marcoTercer, text="Videojuegos", bg="blue")
chkBoton.grid(column=2, row=1)

#Botones

tk.Button(marcoPrincipal, text="Guardar", width=10, bg="orchid1").grid(column=0, row=3, sticky=W, pady=10, padx=10)
tk.Button(marcoPrincipal, text="Cancelar", width=10, bg="orchid1").grid(column=1, row=3, sticky=W)

#desplegable

Estados = StringVar()
comboEstados = ttk.Combobox(marcoPrincipal, textvariable=Estados)
comboEstados.grid(column=1, row=1, padx=20)
comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacan")

marcoCuatro = tk.Frame(marcoPrincipal, bg="pink")
marcoCuatro.grid(column=1, row=0)

#botones redondos
ocupación = StringVar()
Estudiante = tk.Radiobutton(marcoCuatro, text="Estudiante", variable=ocupación, value="Estudiante", bg="pink").grid(column=0, row=0, sticky=W)
Empleado = tk.Radiobutton(marcoCuatro, text="Empleado", variable=ocupación, value="Empleado", bg="pink").grid(column=0, row=1, sticky=W)
Desempleado = tk.Radiobutton(marcoCuatro, text="Desempleado", variable=ocupación, value="Desempleado", bg="pink").grid(column=0, row=2, sticky=W)


for hijo in marcoPrincipal.winfo_children():
    hijo.grid_configure(padx=10, pady=10)

txtName.focus()
raiz.mainloop()