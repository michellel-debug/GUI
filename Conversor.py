from tkinter import *
from tkinter import ttk

def calcular(*args):
    try:   
        resultado = float(pies.get()) * 0.3048
        metros.set(resultado)
    except ValueError:
        pass

raiz = Tk()
raiz.title("Pies a metros")

marcoPrincipal = ttk.Frame(raiz, padding= "3 3 12 12")
marcoPrincipal.grid (column=0, row=0)

pies = StringVar()
metros = StringVar()

txtPies = ttk.Entry(marcoPrincipal, textvariable=pies)
txtPies.grid(column=1, row=0)

ttk.Label(marcoPrincipal, text="Pies").grid(column=2, row=0)
ttk.Label(marcoPrincipal, text="Son equivalentes a:").grid(column=0, row=1)
ttk.Label(marcoPrincipal, textvariable=metros).grid(column=1, row=1)
ttk.Label(marcoPrincipal, text="Metros").grid(column=2, row=1, sticky=N)

ttk.Button(marcoPrincipal, text="Calcular", command=calcular).grid(column=2, row=2)

txtPies.focus()
raiz.bind("<Return>", calcular)

raiz.mainloop()