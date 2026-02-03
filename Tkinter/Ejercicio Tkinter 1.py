import tkinter as tk

ventana = tk.Tk()
ventana.title("VERBOS")
ventana.state('zoomed')

texto1 = tk.Label(ventana, text = 'Elige una opción: ', font = ('Pixel LCD7', 25))
texto1.place(x = 250, y = 30, width = 1200, height = 60)
texto2 = tk.Label(ventana, text = 'hiahiahia', font = ('Helvetica', 30))
texto2.pack()

ventana.mainloop()