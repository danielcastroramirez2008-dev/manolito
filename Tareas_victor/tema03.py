
#   1. Copia este archivo a tu repositorio practicas-python como:
#        tema-03.py
#   2. Resuelve cada ejercicio debajo de su enunciado.
#   3. Van de fácil a difícil: bronce, plata y oro. Avanza a tu ritmo.
#   4. Súbelo a GitHub con el commit:
#        feat: ejercicios del tema 03
#
# Nombre completo: DANIEL CASTRO RAMIREZ 
# Mi app se llama:  CYBERSHEID
# =============================================================


# =============================================================
# 🥉 BRONCE
# =============================================================

# -------------------------------------------------------------
# EJERCICIO 1 · Lista de invitados
# -------------------------------------------------------------
# Crea una lista con 5 nombres de compañeros de clase.
#   - Muestra el primero y el último (usa las posiciones).
#   - Con un for, saluda a cada persona.
#   - Al final, muestra cuántas personas hay con len().
#
# Así debe verse:
#   Primero: Ana   Último: Sara
#   Hola, Ana. Te damos la bienvenida
#   ...
#   Total de invitados: 5

# Tu código aquí:

compañerosDeClase = ["maria teresa de calcuta", "matias,aliaspolla.nequi", "donato", "castro","victor"]

print(compañerosDeClase)        # toda la lista
print(compañerosDeClase[0] , "primero") #primero
print(compañerosDeClase[4] , "ultimo") #ultimo

for compañerosDeClase in compañerosDeClase:
    print(f"HOLA, {compañerosDeClase} TE DAMOS LA BIENVENIDA")

print(f"TOTAL DE INVITADOS: {len(compañerosDeClase)}")

print("----------------------------------------------------------")
# -------------------------------------------------------------
# EJERCICIO 2 · La tabla de multiplicar
# -------------------------------------------------------------
# Pregunta un número con input() y muestra su tabla del 1 al 10
# usando for y range().
#
# Así debe verse (si escribe 7):
#   7 x 1 = 7
#   7 x 2 = 14
#   ...
#   7 x 10 = 70
#
# Pista: range(1, 11) va del 1 al 10.

# Tu código aquí:

numero = int(input("INGRESA UN MUNERO: "))
total = 0
for i in range(1, 11):
    total = numero * i
    print(f"{numero} x {i} = {total}")

print("---------------------------------------------")

# =============================================================
# 🥈 PLATA
# =============================================================

# -------------------------------------------------------------
# EJERCICIO 3 · Las notas del trimestre
# -------------------------------------------------------------
# notas = [4.2, 2.9, 3.5, 4.8, 2.5, 3.0]
#   - Con un for, muestra cada nota y si aprobó (>= 3.0) o no.
#   - Cuenta cuántas aprobaron.
#   - Calcula el promedio:  sum(notas) / len(notas)
#
# Así debe verse:
#   4.2 -> aprobó
#   2.9 -> no aprobó
#   ...
#   Aprobaron 4 de 6. Promedio: 3.48

# Tu código aquí:

notas = [4.2, 2.9, 3.5, 4.8, 2.5, 3.0]

aprobadas = 0
promedio = sum(notas) / len(notas)

for nota in notas:
    if nota >= 3.0:
        print(f"{nota} -> aprobó")
        aprobadas = aprobadas + 1
    else:
        print(f"{nota} -> no aprobó")

print(f"Aprobaron {aprobadas} de {len(notas)}.   PROMEDEIO: {round(promedio,2)}")

print("--------------------------------------------------------------------")

# -------------------------------------------------------------
# EJERCICIO 4 · Encuentra el error (1)
# -------------------------------------------------------------
# Este código tiene 3 errores. Corrígelos y explica en un
# comentario qué estaba mal en cada uno.
#
#   colores = ["rojo", "verde", "azul"]
#   print(colores[3])
#   for color in colores
#   print(color)

# Tu código corregido aquí:

colores = ["rojo", "verde", "azul"]
print(colores[2])
for color in colores:
  print(color)

print("-------------------------------------")

# Error 1: todo tenia sangria
# Error 2:  le faltaban los : al for
# Error 3:  esta pidiendo imprimir la posicion 3 cuando la lista solo llega a la segunda posicion


# -------------------------------------------------------------
# EJERCICIO 5 · Encuentra el error (2)
# -------------------------------------------------------------
# Este código debería sumar los precios y mostrar 15000, pero
# muestra 5000. Tiene UN error. Encuéntralo y explica por qué pasa.
#
#   precios = [5000, 5000, 5000]
#   for precio in precios:
#       total = 0
#       total = total + precio
#   print(total)

# Tu código corregido aquí:

precios = [5000, 5000, 5000]
total = 0
for precio in precios:
      total = total + precio
print(total)

print("----------------------------")
# ¿Qué pasaba?: la variable total=0 estaba dentro del for cuando deberia ir a fuera ademas de la sangria a la lista y al for


# =============================================================
# 🥇 ORO
# =============================================================

# -------------------------------------------------------------
# EJERCICIO 6 · La mini tienda
# -------------------------------------------------------------
# Haz un menú con while (como el del tema 02) que guarde
# productos en una lista:
#   1. Agregar producto (pregunta el precio y haz append a la lista)
#   2. Ver productos (muestra cada precio con un for)
#   3. Ver total con IVA (el 19 %)
#   4. Salir
#
# Reto extra: en la opción 3, crea la lista de precios con IVA
# en UNA sola línea con list comprehension.
#
# Pista: crea precios = [] (lista vacía) ANTES del while.

# Tu código aquí:


print("==============================")
print("            MENU              ")
print("==============================")

compras = []

while True:
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Ver total con IVA (el 19 %)")
    print("4. Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        producto = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio: $"))

        compras.append({"nombre": producto, "precio": precio})

        print("Producto agregado correctamente.")

    elif opcion == 2:
        if len(compras) == 0:
            print("No hay productos registrados.")
        else:
            print("===== LISTA DE PRODUCTOS =====")

            for producto in compras:
                print(f"PRODUCTO: {producto['nombre']} | PRECIO: ${producto['precio']:.2f}")

    elif opcion == 3:
        if len(compras) == 0:
            print("No hay productos para calcular el total.")
        else:
            subtotal = 0

            for producto in compras:
                subtotal += producto["precio"]

            iva = subtotal * 0.19
            total = subtotal + iva

            print("===== TOTAL DE LA COMPRA =====")
            print(f"SUBTOTAL: ${subtotal:.2f}")
            print(f"IVA (19%): ${iva:.2f}")
            print(f"TOTAL CON IVA: ${total:.2f}")

    elif opcion == 4:
        print("SALIENDO DEL PROGRAMA...")
        break

    else:
        print("OPCIÓN NO VÁLIDA. SELECCIONE 1, 2, 3 o 4.")


# =============================================================
# EJERCICIO 7 · LLÉVALO A TU APP  (va en src/app.py de tu app, no aquí)
# =============================================================
# Tu app ya tiene un menú (tema 02). Hoy aprende a GUARDAR
# varios registros mientras está abierta:
#   1. Crea una lista vacía antes del menú. Ejemplos: citas = [],
#      productos = [], metas = [], tareas = [].
#   2. Agrega la opción "Agregar ...": pregunta el dato y haz append.
#   3. Agrega la opción "Ver ...": muéstralos con un for, numerados.
#      Si la lista está vacía, muestra "Todavía no hay registros".
#   4. Muestra cuántos registros hay con len().
#
# Ejemplo para una app de citas de barbería:
#   1. Agendar cita
#   2. Ver citas
#   3. Salir
#   Opción: 2
#   1. Carlos - 10:00
#   2. Valentina - 11:30
#   Total de citas: 2
#
# Pista para numerar: for i in range(len(citas)):
#                         print(f"{i + 1}. {citas[i]}")
#
# OJO: cuando cierras la app, la lista se borra. Guardar en un
# archivo es un tema más adelante.
# =============================================================