from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Formulario")

marcoPrincipal = ttk.Frame(raiz, padding= "30 30 30 30")
marcoPrincipal.grid(column=0, row=0)
marcoPrincipal.config(width=480,height=320)

marcoSecond = ttk.Frame(marcoPrincipal)
marcoSecond.pack()

raiz.config(bg="lightblue") 
marcoSecond.config(relief="sunken")
marcoSecond.config(width=300,height=280) 

#Textbox nombre
txtName = ttk.Entry(marcoSecond, width=20)
txtName.grid(column=1, row=0)

ttk.Label(marcoSecond, text="Nombre").grid(column=0, row=0)

#textbox a. paterno
txtPaterno = ttk.Entry(marcoSecond, width=20)
txtPaterno.grid(column=1, row=1)

ttk.Label(marcoSecond, text="A. Paterno").grid(column=0, row=1)

#textbox a. materno
txtMaterno = ttk.Entry(marcoSecond, width=20)
txtMaterno.grid(column=1, row=2)

ttk.Label(marcoSecond, text="A. Marterno").grid(column=0, row=2)

#textbox correo
txtCorreo = ttk.Entry(marcoSecond, width=20)
txtCorreo.grid(column=1, row=3)

ttk.Label(marcoSecond, text="Correo").grid(column=0, row=3)

#textbox movil
txtMovil = ttk.Entry(marcoSecond, width=20)
txtMovil.grid(column=1, row=4)

ttk.Label(marcoSecond, text="Movil").grid(column=0, row=4)

ocupación = StringVar()
Estudiante = ttk.Radiobutton(marcoPrincipal, text="Estudiante", variable=ocupación, value="Estudiante")
Empleado = ttk.Radiobutton(marcoPrincipal, text="Empleado", variable=ocupación, value="Empleado")
Desempleado = ttk.Radiobutton(marcoPrincipal, text="Desempleado", variable=ocupación, value="Desempleado")

#comboEstados = ttk.Combobox(raiz, textvariable=Estados)
#comboEstados.grid(column=3, row=1, padx= 40, pady= 20)
#comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacan")

#chkBoton = ttk.Checkbutton(raiz, text="Leer")
#chkBoton.grid(column=0, row=2)
#chkBoton = ttk.Checkbutton(raiz, text="Música")
#chkBoton.grid(column=1, row=2)
#chkBoton = ttk.Checkbutton(raiz, text="Videojuegos")
#chkBoton.grid(column=2, row=2)

#ttk.Button(marcoPrincipal, text="Guardar").grid(column=0, row=3)
#ttk.Button(marcoPrincipal, text="Cancelar").grid(column=2, row=3)


txtName.focus()
raiz.mainloop()