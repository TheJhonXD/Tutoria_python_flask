# ******************* VARIABLES *******************

cadena = "hola"
numero = 42
decimal = 3.14
booleano = True
lista = [1, 2, 3, 4, 5]
diccionario = {"nombre": "Juan", "apellido": "Perez"}

# MOSTRANDO TIPOS
# Imprime el tipo de dato de la variable
print(type(cadena))
print(type(numero))
print(type(decimal))
print(type(booleano))
print(type(lista))
print(type(diccionario))

# Diccionario
# Imprime el valor de la clave "nombre" del diccionario
print(diccionario["nombre"])
# Imprime el valor de la clave "apellido" del diccionario
print(diccionario["apellido"])
# Asigna el valor "Pedro" a la clave "nombre" del diccionario
diccionario["nombre"] = "Pedro"
# Imprime el valor de la clave "nombre" del diccionario
print(diccionario["nombre"])
# Imprime las claves o llaves del diccionario
print(diccionario.keys())
# Imprime los valores del diccionario
print(diccionario.values())
# Imprime los items del diccionario
print(diccionario.items())

# METODOS DE CADENAS
# Imprime la cadena en mayusculas
print(cadena.upper())
# Imprime la cadena en minusculas
print(cadena.lower())
# Imprime la cadena con la primera letra en mayuscula
print(cadena.capitalize())
# Cuenta la cantidad de caracteres "o" en la cadena
print(cadena.count("o"))
# Imprime la posicion de la primera ocurrencia de la letra "o"
print(cadena.find("o"))
# Imprime la posicion de la primera ocurrencia de la letra "x"
print(cadena.find("x"))
# Reemplaza la letra "o" por la letra "x"
print(cadena.replace("o", "x"))
# Separa la cadena en una lista de cadenas, usando el caracter "o" como separador
print(cadena.split("o"))
# Quita los espacios en blanco al inicio y al final de la cadena
print(cadena.strip())
# Quita los caracteres "h" al inicio y al final de la cadena
print(cadena.strip("h"))
# Imprime True si existe la cadena "hol" en la variable "cadena"
print("hol" in cadena)

# ******************* OPERACIONES ARITMETICAS *******************
print( 5 + 10)
print( 5 - 10)
print( 5 * 10)
print( 10 / 5)
# Modulo
print( 10 % 5)
# Potencia
print( 5 ** 2)
# Division entera
print( 10 // 5)

# ******************* OPERADORES DE COMPARACION *******************
a = 5
b = 10

# Imprime True si a es mayor que b
print(a > b)
# Imprime True si a es menor que b
print(a < b)
# Imprime True si a es mayor o igual que b
print(a >= b)
# Imprime True si a es menor o igual que b
print(a <= b)
# Imprime True si a es igual que b
print(a == b)
# Imprime True si a es diferente que b
print(a != b)

# ******************* OPERADORES LOGICOS *******************
c = 15

# Imprime True si a es mayor que b y b es menor que c
print(a > b and b < c)
# Imprime True si a es mayor que b o b es menor que c
print(a > b or b < c)
# Imprime True si a es mayor que b y b es menor que c
print(not(a > b and b < c))

# ******************* CONDICIONALES *******************

# IF
if a > b:
    print("a es mayor que b")

# IF ELSE
if a > b:
    print("a es mayor que b")
else:
    print("a es menor que b")

# IF ELSE IF
if a > b:
    print("a es mayor que b")
elif a == b:
    print("a es igual que b")
else:
    print("a es menor que b")

# ******************* CICLOS *******************

# ---------- FOR ----------
# Imprime los numeros del 0 al 4
for i in range(5):
    print(i)

# Imprime los numeros del 5 al 9
for i in range(5, 10):
    print(i)

# Imprime los numeros del 5 al 9 de 2 en 2
for i in range(5, 10, 2):
    print(i)
    
# Bucle for para recorrer una lista
for i in lista:
    print(i)

# ---------- WHILE ----------
i = 0
while i < 5:
    print(i)
    i += 1

# ++++++++++ CONTROL DE FLUJO ++++++++++

# ---------- BREAK ----------
# Sale del bucle cuando i es igual a 3
i = 0
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1

# ---------- CONTINUE ----------
# Salta la iteracion cuando i es igual a 3 pero no rompe el ciclo
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

# ++++++++++ ENTRADA DE DATOS ++++++++++

# ---------- INPUT ----------
# Pide al usuario que ingrese un dato
nombre = input("Ingrese su nombre: ")
print("Hola " + nombre)

# ---------- CASTEO O CONVERSIÖN  ----------
# Convierte el dato o variable a entero
numero = int(input("Ingrese un numero: "))
print(numero)

# Convierte el dato o variable a decimal
decimal = float(input("Ingrese un decimal: "))
print(decimal)

# Convierte el dato o variable a cadena
cadena = str(input("Ingrese una cadena: "))
print(cadena)

# ******************* FUNCIONES *******************


    
