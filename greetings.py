# Solicita el nombre del usuario
# Le saluda con su nombre. 
# Solicita la edad del usuario
# Despliega en la pantalla si es mayor de edad o no (referencia 18 años).

user = input("¿Cuál es tu nombre? ") # Preguntamos el nombre al usuario
print()
print(f"¡Hola {user}, gusto en conocerte!")
print()

age_str = input(f"¿Cuantos años tienes {user}? ") # Preguntamos la edad al usuario
age = int(age_str) # Convertimos la edad a int

# Imprmimos un texto diferente dependiendo si el usuario es mayor o no de edad
if age >= 18:
	print(f"{user}, eres mayor de edad. ¡Adelante!")
else:
	print(f"{user}, no eres mayor de edad. ¡No puedes pasar!")
	





	