variable = "hola"
var1 = 2
var2 = 3.25
var3 = True
lista = [1, 2, 3, 4, 5, "hola"]
diccionario = {"nombre": "Juan", "apellido": "Perez"}

# print(type(diccionario))

"""
print(diccionario.keys())
print(diccionario.values())
"""

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

print(variable.upper())
print(variable.lower())
print(variable.capitalize())
print(variable.count("o"))
print(variable.find("o"))
print(variable.replace("hl", "x"))
print(variable.strip("h"))

print("hol" in variable)


# ******************* OPERACIONES ARITMETICAS *******************
print("OPERACIONES ARITMETICAS")
print( 5 + 10)
print( 5 - 10)
print( 5 * 10)
print( 10 / 3)
# Modulo
print( 10 % 5)
# Potencia
print( 5 ** 2)
# Division entera
print( 10 // 3)

# ******************* OPERADORES DE COMPARACION *******************
a = 10
b = 10

print("OPERADORES DE COMPARACION")

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
# En C && es el operador logico AND
print(a > b and b < c)
# Imprime True si a es mayor que b o b es menor que c
# En C || es el operador logico OR
print(a > b or b < c)
# Imprime True si a es mayor que b y b es menor que c
# En C ! es el operador logico NOT
print(not(a > b and b < c))

# ******************* CONDICIONALES *******************

# IF
if a < b:
    print("hola")
    if a < c:
        print("hola 2")
    print("a es menor que b")
    
# IF ELSE
if a > b:
    print("a es mayor que b")
else:
    print("a es menor que b")
    
# IF ELSE IF
if a > b:
    print("a es mayor que b")
    if a < c:
        print("hola 2")
elif a == b:
    nuevavar = "hola dfsdfds"
    print("a es igual que b")
    if a < c:
        print("If anidado")
else:
    print("a es menor que b XD")
    
print("A:", nuevavar)
    
print("hola " * 3)

# ******************* CICLOS *******************
print("Ciclos")
# ---------- FOR ----------
# Imprime los numeros del 0 al 4
for i in range(5):
    print(i)

print("------")
# Imprime los numeros del 5 al 9
for i in range(5, 11):
    print(i)

print("------")
# Imprime los numeros del 5 al 9 de 2 en 2
for i in range(5, 10, 2):
    print(i)

print("------")
# Bucle for para recorrer una lista
for i in lista:
    print(i)
    
# ---------- WHILE ----------
print("while")
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print("Fin del while")

print("-----------------")

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


