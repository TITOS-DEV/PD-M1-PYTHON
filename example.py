"""
EJEMPLOS DE CONDICIONALES Y CICLOS EN PYTHON
=============================================
"""

# =============================================================================
# CONDICIONALES
# =============================================================================

print("=" * 50)
print("EJEMPLOS DE CONDICIONALES")
print("=" * 50)

# 1. IF simple
print("\n1. IF SIMPLE:")
edad = 18
if edad >= 18:
    print(f"Tienes {edad} años, eres mayor de edad")

# 2. IF-ELSE
print("\n2. IF-ELSE:")
temperatura = 15
if temperatura > 25:
    print("Hace calor")
else:
    print("No hace calor")

# 3. IF-ELIF-ELSE (múltiples condiciones)
print("\n3. IF-ELIF-ELSE:")
nota = 85
if nota >= 90:
    print("Calificación: A - Excelente")
elif nota >= 80:
    print("Calificación: B - Muy bien")
elif nota >= 70:
    print("Calificación: C - Bien")
elif nota >= 60:
    print("Calificación: D - Aprobado")
else:
    print("Calificación: F - Reprobado")

# 4. Operador ternario (condicional en una línea)
print("\n4. OPERADOR TERNARIO:")
edad = 20
mensaje = "Mayor de edad" if edad >= 18 else "Menor de edad"
print(f"Con {edad} años: {mensaje}")

# 5. Condicionales anidados
print("\n5. CONDICIONALES ANIDADOS:")
tiene_licencia = True
edad = 25
if edad >= 18:
    if tiene_licencia:
        print("Puedes conducir")
    else:
        print("Necesitas una licencia")
else:
    print("Eres menor de edad para conducir")

# 6. MATCH-CASE (Python 3.10+)
print("\n6. MATCH-CASE (Python 3.10+):")
dia = 3
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6 | 7:
        print("Fin de semana")
    case _:
        print("Día inválido")

# 7. Condicionales con operadores lógicos
print("\n7. CONDICIONALES CON OPERADORES LÓGICOS:")
usuario = "admin"
contraseña = "1234"

# AND
if usuario == "admin" and contraseña == "1234":
    print("Acceso concedido (AND)")

# OR
tiene_tarjeta = False
tiene_efectivo = True
if tiene_tarjeta or tiene_efectivo:
    print("Puedes pagar (OR)")

# NOT
esta_lloviendo = False
if not esta_lloviendo:
    print("Puedes salir sin paraguas (NOT)")

# =============================================================================
# CICLOS
# =============================================================================

print("\n" + "=" * 50)
print("EJEMPLOS DE CICLOS")
print("=" * 50)

# 1. FOR con range()
print("\n1. FOR CON RANGE:")
for i in range(5):
    print(f"  Iteración {i}")

# 2. FOR con lista
print("\n2. FOR CON LISTA:")
frutas = ["manzana", "banana", "naranja", "uva"]
for fruta in frutas:
    print(f"  Me gusta la {fruta}")

# 3. FOR con enumerate (índice y valor)
print("\n3. FOR CON ENUMERATE:")
colores = ["rojo", "verde", "azul"]
for indice, color in enumerate(colores):
    print(f"  Color {indice}: {color}")

# 4. FOR con diccionario
print("\n4. FOR CON DICCIONARIO:")
estudiante = {"nombre": "Juan", "edad": 20, "curso": "Python"}
for clave, valor in estudiante.items():
    print(f"  {clave}: {valor}")

# 5. WHILE loop
print("\n5. WHILE LOOP:")
contador = 0
while contador < 5:
    print(f"  Contador: {contador}")
    contador += 1

# 6. WHILE con condición compleja
print("\n6. WHILE CON CONDICIÓN COMPLEJA:")
numero = 1
suma = 0
while numero <= 10 and suma < 30:
    suma += numero
    print(f"  Número: {numero}, Suma acumulada: {suma}")
    numero += 1

# 7. FOR con BREAK (romper el ciclo)
print("\n7. FOR CON BREAK:")
for i in range(10):
    if i == 5:
        print(f"  Rompiendo el ciclo en {i}")
        break
    print(f"  Número: {i}")

# 8. FOR con CONTINUE (saltar iteración)
print("\n8. FOR CON CONTINUE:")
for i in range(10):
    if i % 2 == 0:  # Si es par, saltar
        continue
    print(f"  Número impar: {i}")

# 9. FOR con ELSE (se ejecuta si el loop termina normalmente)
print("\n9. FOR CON ELSE:")
for i in range(5):
    print(f"  Iteración: {i}")
else:
    print("  El ciclo terminó normalmente")

# 10. WHILE con BREAK y bandera
print("\n10. WHILE CON BREAK:")
intentos = 0
max_intentos = 5
while True:
    intentos += 1
    print(f"  Intento {intentos}")
    if intentos >= max_intentos:
        print("  Máximo de intentos alcanzado")
        break

# 11. Ciclos anidados
print("\n11. CICLOS ANIDADOS:")
for i in range(3):
    for j in range(3):
        print(f"  i={i}, j={j}")

# 12. List comprehension (ciclo for en una línea)
print("\n12. LIST COMPREHENSION:")
cuadrados = [x**2 for x in range(10)]
print(f"  Cuadrados: {cuadrados}")

# 13. List comprehension con condicional
print("\n13. LIST COMPREHENSION CON CONDICIONAL:")
pares = [x for x in range(20) if x % 2 == 0]
print(f"  Números pares: {pares}")

# 14. Dictionary comprehension
print("\n14. DICTIONARY COMPREHENSION:")
cuadrados_dict = {x: x**2 for x in range(5)}
print(f"  Diccionario de cuadrados: {cuadrados_dict}")

# 15. Set comprehension
print("\n15. SET COMPREHENSION:")
letras_unicas = {letra for letra in "programming"}
print(f"  Letras únicas: {letras_unicas}")

# 16. Ciclo con zip (iterar sobre múltiples listas)
print("\n16. CICLO CON ZIP:")
nombres = ["Ana", "Luis", "María"]
edades = [25, 30, 28]
for nombre, edad in zip(nombres, edades):
    print(f"  {nombre} tiene {edad} años")

# 17. Ciclo con reversed()
print("\n17. CICLO CON REVERSED:")
numeros = [1, 2, 3, 4, 5]
for num in reversed(numeros):
    print(f"  Número: {num}")

# 18. Ciclo con sorted()
print("\n18. CICLO CON SORTED:")
nombres = ["Carlos", "Ana", "Beatriz"]
for nombre in sorted(nombres):
    print(f"  Nombre: {nombre}")

print("\n" + "=" * 50)
print("FIN DE LOS EJEMPLOS")
print("=" * 50)
