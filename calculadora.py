# Calculadora: el programa le pregunta al usuario dos valores numericos y después imprime las opciones de diferentes operaciones que puede realizar. Realiza la operación y muestra el resultado.

# Pedimos un valor numerico al usuario y cachamos el error si el usuario digita un str. Continúa preguntando hasta que el usuario digite un float.
print()

a = 0
while a == 0:
	try:
		num_1 = float(input("Introduce el primer valor númerico "))
		a += 1 
	except ValueError:
		print("¡Solo valores numericos!")
		print()
print()		
b = 0
while b == 0:
	try:
		num_2 = float(input("Introducer el segundo valor númerico: "))
		b += 1
	except ValueError:
		print("¡Solo valores numericos!")
		print()

# Opciones de posibles operaciones a realizar
print("""
	1- Suma
	2- Resta
	3- Múltiplicación
	4- División
	5- Potencia
	6- Raíz
	""")

# Preguntamos al usuario la operacion a realizar y cachamos el error si el usuario digita un str o un numero inexistente de operación. Continúa preguntando hasta que el usuario digite un numero correspondiente a una operación.
print()
c = 0
while c == 0:
	try:
		operation =int(input("Seleccióna la operación a realizar: ")) 
		print()
		if operation > 6:
			print("Esa no es una operación valida")
			print()
		else:
			c += 1	
	except ValueError:
		print("Digita el número de la operación a realizar")
		print()
	
# Operaciones matematicas
if operation == 1:
	result = num_1 + num_2
elif operation == 2:
	result = num_1 - num_2
elif operation == 3:
	result = num_1 * num_2
# Para la divición usamo la excepción ZeroDivisionError 	
elif operation == 4:  
	try:
		result = num_1 / num_2
	except ZeroDivisionError:
		print()
		result = "¡No puedes dividir entre cero!" 	
elif operation == 5:
	result = num_1 ** num_2
elif operation == 6:
	result = num_1 ** (num_1/num_2)

print()
print(f"El primer valor númerico es: {num_1}")
print(f"El segundo valor númerico es: {num_2}")
# Asiganmos su respectivo nombre a cada operación
if operation == 1:
	operation_done = "Suma"
elif operation == 2:
	operation_done = "Resta"
elif operation == 3:
	operation_done = "Múltiplicación"
elif operation == 4:
	operation_done = "División"
elif operation == 5:
	operation_done = "Potencia"
elif operation == 6:
	operation_done = "Raíz"
print(f"La operación realizada es: {operation_done}")
print(f"El resultado es: {result}")							 

