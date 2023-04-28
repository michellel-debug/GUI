from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("Formulario")

marcoPrincipal = ttk.Frame(raiz, padding= "30 30 30 30")
marcoPrincipal.grid(column=0, row=0)

ocupación = StringVar()
Estados = StringVar()

Estudiante = ttk.Radiobutton(text="Estudiante", variable=ocupación, value="Estudiante")
Empleado = ttk.Radiobutton(text="Empleado", variable=ocupación, value="Empleado")
Desempleado = ttk.Radiobutton(text="Desempleado", variable=ocupación, value="Desempleado")

comboEstados = ttk.Combobox(raiz, textvariable=Estados)
comboEstados.grid(column=3, row=1, padx= 40, pady= 20)
comboEstados['values'] = ("Jalisco", "Nayarit", "Colima", "Michoacan")

ttk.Button(marcoPrincipal, text="Guardar").grid(column=0, row=4)
ttk.Button(marcoPrincipal, text="Cancelar").grid(column=1, row=4)



raiz.mainloop()