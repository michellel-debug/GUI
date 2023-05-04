import tkinter as tk

# Crear la ventana principal
root = tk.Tk()

# Crear un frame y darle formato
frame = tk.Frame(root, bg='white', bd=5)
frame.place(relx=0.5, rely=0.5, relwidth=0.75, relheight=0.75, anchor='center')

# Agregar widgets al frame
label = tk.Label(frame, text='Ejemplo de frame con formato')
label.pack()

# Iniciar la ventana principal
root.mainloop()
