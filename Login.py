from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("LogIn")

marcoPrincipal = ttk.Frame(raiz, padding= "20 20 20 20")
marcoPrincipal.grid(column=0, row=0)

txtUser = ttk.Entry(marcoPrincipal) 
txtUser.grid(column=0, row=1)

ttk.Label(marcoPrincipal, text="Username").grid(column=0, row=0)

txtUser = ttk.Entry(marcoPrincipal) 
txtUser.grid(column=0, row=3)

ttk.Label(marcoPrincipal, text="Password").grid(column=0, row=2)

ttk.Button(marcoPrincipal, text="Ingresar").grid(column=0, row=4)

for hijo in marcoPrincipal.winfo_children():
    hijo.grid_configure(padx=5, pady=5)

raiz.mainloop()