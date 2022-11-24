import tkinter

# Creo una ventana de 350x350
ventana = tkinter.Tk()
ventana.geometry("350x350")

# Defino la etiqueta de los textos
texto_arriba = tkinter.Label(ventana, text = "Arriba")
texto_abajo = tkinter.Label(ventana, text = "Abajo")
texto_izquierda = tkinter.Label(ventana, text = "Izquierda")
texto_derecha = tkinter.Label(ventana, text = "Derecha")

# Defino el lugar donde los textos aparecen
texto_arriba.pack()
texto_abajo.pack(side = tkinter.BOTTOM)
texto_izquierda.pack(side = tkinter.LEFT)
texto_derecha.pack(side = tkinter.RIGHT)

ventana.mainloop()