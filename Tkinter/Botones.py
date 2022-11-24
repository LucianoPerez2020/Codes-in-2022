import tkinter

# Defino una funcion para hacer algo despues de presionar el boton
def saludo(nombre):
    print("Buenos dias " + nombre)

# Defino la ventana y el boton (con el tamaño de la casilla)
ventana = tkinter.Tk()
ventana.geometry("500x500")
casilla_de_texto = tkinter.Entry(ventana, font = "50")

# Creo un boton llamado "boton1" en la ventana "ventana" y le doy una dimension de 25x25
boton1 = tkinter.Button(ventana, text = "Click", pady = 25, padx = 25, command = lambda: saludo("python"))
boton2 = tkinter.Button(ventana, text = "Click", pady = 25, padx = 25, command = lambda: print("Buenas tardes python"))

# Mostramos los textos y botones en la ventana
boton1.pack()
boton2.pack(side = tkinter.BOTTOM)
casilla_de_texto.pack(side = tkinter.LEFT)

ventana.mainloop()