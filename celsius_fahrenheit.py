# Solicita al usuario la temperatura en grados Celsius
# Convierte la temperatura en grados Fahrentheit
# Imprime la temperatura conversa

# Constantes para la formúla de conversión 
x = 1.8
n = 32

# Opciones de conversion
print("""
	1- Convertidor de Celsius a Fahrenheit
	2- Convertidor de Fahrenheit a Celsius
	""")

# Cachamos un error si el usuario digita un str por algún motivo
try:
	convert = int(input("Digita el numero de la conversion a realizar: ")) # Preguntamos la conversion a realizar
	print()
	
	if convert == 1:
		temp_cels = float(input("Digita la temperatura en grados Celsius: ")) # Preguntamos la temperatura en int

		temp_fahr = (temp_cels * x) + n
		
		print()
		print(f"La temperatura de {temp_cels}°C, es igual a {temp_fahr}°F") # Imprimimos la conversion

	elif convert == 2:
		temp_fahr = float(input("Digita la temperatura en grados Fahrenheit: ")) 

		temp_cels = (temp_fahr - n) / x

		print()
		print(f"La temperatura de {temp_fahr}°F, es igual a {temp_cels}°C")

	else:
		print("¡Solo existen 2 opciones!")	 

except ValueError:
	print("¡Solo puedes digitar numeros!")
