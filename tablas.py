print()
print("¡Tablas de multiplicar!")
print()

num  = int(input("¿Cual tabla de multiplicar quieres? "))

print()
print("La tabla del", num, "es: ")
print()

i = 1

while i <= 10:
    print(num, "x", i, "=", num*i)
    i = i+1