def año_de_prueba(año):
	if año % 2 == 0:
		return True
	else:
		return False

test_data = [2000, 2001, 2002, 2003]
test_results = [True, False, True, False]

for i in range(len(test_data)):     # En el rango de los valores de "test_data".
	yr = test_data[i]				# "yr" es igual al valor del momento de "test_data".
	print(yr,"->",end=" ")			# Me printea el año seguido de un "->" con un argumento "end" de espacio vacio para no hacer un salto de linea.

	result = año_de_prueba(yr)		
	# "result" es igual a lo que de el return de la funcion "año_de_prueba" con el valor asigando 
	# de la variable "yr" que despues sera tomado en la misma funcion como el valor de "año".

	if result == test_results[i]:	# Si "result" tiene el mismo valor que el valor de "test_results[i]"...
		print("Bien")
	else:							# Si no...
		print("Mal")