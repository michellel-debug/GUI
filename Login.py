from tkinter import *
from tkinter import ttk

raiz = Tk()
raiz.title("LogIn")

marcoPrincipal = ttk.Frame(raiz, padding= "30 30 30 30")
marcoPrincipal.grid(column=0, row=0)

txtUser = ttk.Entry(marcoPrincipal, width=15) #width define el tamaño de la text box
txtUser.grid(column=0, row=1)

ttk.Label(marcoPrincipal, text="Username").grid(column=0, row=0)

txtPassword = ttk.Entry(marcoPrincipal, width=15) 
txtPassword.grid(column=0, row=3)

ttk.Label(marcoPrincipal, text="Password").grid(column=0, row=2)

ttk.Button(marcoPrincipal, text="Log In").grid(column=0, row=4)

for hijo in marcoPrincipal.winfo_children():
    hijo.grid_configure(padx=10, pady=10)

txtUser.focus() #se usa cuando queremos que el cursor aparezca automáticamente

raiz.mainloop()