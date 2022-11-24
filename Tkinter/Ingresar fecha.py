import tkinter

def mostrar_fecha():
    fecha = ingresar_fecha.get()
    print("Hoy es " + fecha)

ventana = tkinter.Tk()
ventana.geometry("300x300")

ingresar_fecha = tkinter.Entry(ventana, font = "25")
confimar_fecha = tkinter.Button(ventana, text = "Confimar fecha", pady = 10, padx = 10, command = mostrar_fecha)

ingresar_fecha.pack()
confimar_fecha.pack()

ventana.mainloop()


# Para que me sirve lambda