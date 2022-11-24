import tkinter # Importamos la libreria

# Creamos la ventana a usar
ventana = tkinter.Tk()
ventana2 = tkinter.Tk()

# Le damos las dimenciones con las que se va a abrir la ventana
ventana.geometry("500x500") 
ventana2.geometry("500x500") 

# Le damos un texto a poner en la msima ventana
texto = tkinter.Label(ventana, text = "Ventana N°1", bg = "purple") 
texto2 = tkinter.Label(ventana, text = "Texto a lo largo", bg = "#73ffb4")
texto3 = tkinter.Label(ventana2, text = "Ventana N°2", bg = "green") 

# Centro la etiqueta de texto y muestra el texto en si
texto.pack()
texto2.pack(fill = tkinter.X) # Hago que el box del texto sea a lo largo de la ventana
texto3.pack(fill = tkinter.BOTH, expand = 1) # Hago que el box del texto sea a lo largo y ancho de la ventana
# both = ambos

ventana.mainloop()