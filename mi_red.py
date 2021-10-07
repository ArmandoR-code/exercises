print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

#Primera interacción. Solicitamos al usuario que ingrese su nombre,
#y lo guardamos en una variable de tipo str
name = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", name, ", bienvenido a Mi Red")
print()

#Segunda interacción. Solicitamos el ingreso del año, y utilizamos este
#dato para estimar la edad de la persona.
import datetime
current_year  = datetime.date.today().year  
print()
birthday = (input("Para preparar tu perfil, dime en qué año naciste. "))
print()
try:
    year = int(birthday)
except:
    year = -1

if year > 0:
    print()
else:
    print("En numero por favor")

age = current_year - year
print()

#Tercera interacción. Solicitamos la estatura en metros.
#Utilizamos la conversión a 'int', y una expresión para convertir esto
#a una medida en metros y centímetros
try:
    hight = float(input("Cuéntame más de ti, para agregarlo a tu perfil. ¿Cuánto mides? Dímelo en metros. "))
    print()
    hight_m = int(hight)
    hight_cm = int( (hight - hight_m)*100 )
except ValueError:
    print()
    print("!!Estatura en numeros¡¡")    
    print()


#No. de celular
try:
    cell_number = int(input("Cual es tu número de celular? escribelo sin espacios "))
except ValueError:
    print()
    print("SOLO NUMEROS")   
print()
#Genero
gender = input("Dime cual es tu genero? ")
print()
#Pais
country = input("¿En que país vives? ")
print()
#Cuarta interacción. Consultamos cuántos amigos tiene el usuario.
num_frineds = (input("Muy bien. Finalmente, cuéntame cuantos amigos tienes. "))
   
#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", name, ". Entonces podemos crear un perfil con estos datos.")
print("-" * 100)
print("-" * 100)
print("Nombre:  ", name)
print("Edad:    ", age, "años")
try:
    print("Estatura:", hight_m, "metros y", hight_cm, "centímetros")
except NameError:
    print("Edad: Tus datos no fueron proporcionados de forma correcta")
try:        
    print("Tu número de celular es:", cell_number)
except NameError:
     print("Numero de celular: Tus datos no fueron proporcionados de forma correcta")   
print("Eres un(a):", gender)
print("Vives en:", country)
print("Amigos:  ", num_frineds)
     
print("-" * 100)
print("-" * 100)
print("Gracias por la información. Esperamos que disfrutes con Mi Red")
print()

#Finalmente, solicitamos un mensaje de prueba que sirva para publicar un estado del usuario.
mensaje = input("Ahora vamos a publicar tu primer mensaje. ¿Qué piensas hoy? ")
print()
print("*" * 100)
print(name, "dice:", mensaje)
print("*" * 100)
