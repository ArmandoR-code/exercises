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

#Usaremos una variable bool para indicar si el usuario desea continuar utilizando el programa o no
continue_ = True

#Creamos una clase para almacenar las publicaciones del usuario
class Board():
        """Clase para almacenar y editar los mensajes del usuario """
        def __init__(self):
            self.msg_usr = []
        #Guardamos un mensaje
        def pull_in(self, msg):
            self.msg_usr.append(msg)
        #Borramos el último mensaje escrito   
        def pull_out(self):
            return self.msg_usr.pop()
        def all_msg(self):
            return self.msg_usr
all_msg_usr = Board()

#Este ciclo se ejecuta hasta que el usuario desee salir
while continue_:
    #Preguntamos al usuario si desea escribir un mensaje
    post_msg = str(input("Escribir mensaje: S/N "))
    
    #Vamos a aceptar que el usuario ingrese un mensaje cuando escriban "S", "s", o nada
    if post_msg == "S" or post_msg == "s":
        msg_usr = Board()
        msg_usr.pull_in(input("¿En qué estas pensando? "))
        print()
        print("*" * 100)
        print(name, "dice:", msg_usr.all_msg())
        print("*" * 100)
    # Si la respuesta es negativa terminamos el ciclo
    elif post_msg == "N" or post_msg == "n":   
        delete = str(input("Borrar último mensaje enviado: S/N "))
        if delete == 'S' or delete == 's':
            msg_usr.pull_out()
        elif delete =='N' or delete == 'n':
            all_ = str(input("Ver mensajes publicados: S/N "))
            if all_ == 'S' or all_ == 's':
                print(all_msg_usr.all_msg())
            elif all_ == 'N' or all_ == 'n':                
                continue_ = False            
print()

change_name = True

while change_name:
    change = str(input("¿Quieres cambiar tu nombre de usuario? S/N "))
    
    if change == "S" or change == "s":
        print()
        print("Vamos a cambiar tu nombre!!")
        print()
        new = str(input("Escribe tu nuevo nombre: "))
        name = new
        print()
        print("Este es tu nuevo nombre: ", new)
    
    elif change == "N" or change == "n":
        change_name = False
print()
#Mensaje de salida, una vez que el ciclo ha terminado.
print("Gracias por usar Mi Red. ¡Hasta pronto!")                      
    
  
