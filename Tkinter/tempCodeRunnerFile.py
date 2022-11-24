import tkinter
# import botones.py || como hago para importar otros programas a otros???

# Creo la funcion principal de mi programa
def examen():
    respuesta = ingresar_fecha.get()
    if respuesta == "4":
        print("Correcto")
        texto_respuesta = tkinter.Label(ventana, text = "Correcto")
        texto_respuesta.pack()
    else:
        print("Incorrecto")
        texto_respuesta = tkinter.Label(ventana, text = "Incorrecto")
        texto_respuesta.pack()

# Creo mi ventana
ventana = tkinter.Tk()
ventana.geometry("300x250") 

# Creo los textos, casillas y botonoes necesarios
texto = tkinter.Label(ventana, text = "Probando condicionales") 
pregunta = tkinter.Label(ventana, text = "Cuanto es 2+2?")
ingresar_fecha = tkinter.Entry(ventana, font = "25")
boton_evaluar = tkinter.Button(ventana, text = "Evaluar", pady = 10, padx = 10, command = examen)

# Defino los espacios que voy a usar
texto.pack()
pregunta.pack()
ingresar_fecha.pack()
boton_evaluar.pack(side = tkinter.BOTTOM)

ventana.mainloop()