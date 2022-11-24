import tkinter

# Creamos la ventana a usar
ventana = tkinter.Tk()
ventana2 = tkinter.Tk()
ventana3 = tkinter.Tk()

# Definimos las dimenciones
ventana.geometry("500x500")
ventana2.geometry("500x500")
ventana3.geometry("500x500")

# Le damos un texto a poner en la msima ventana
etiqueta = tkinter.Label(ventana, text = "Ventana 1")
etiqueta2 = tkinter.Label(ventana2, text = "Ventana 2")
etiqueta3 = tkinter.Label(ventana3, text = "Ventana 3")

# Hace visible el texto
etiqueta.pack()
etiqueta2.pack()
etiqueta3.pack()

ventana.mainloop() 