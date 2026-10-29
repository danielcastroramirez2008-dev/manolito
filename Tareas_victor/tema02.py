# =============================================================
# Tema 02 · Condicionales y menú con while · EJERCICIOS
# python-adso · SENA ADSO
#
# INSTRUCCIONES
#   1. Copia este archivo a tu repositorio practicas-python como:
#        tema-02.py
#   2. Resuelve cada ejercicio debajo de su enunciado.
#   3. Ejecuta el archivo y prueba cada caso (los que se cumplen
#      y los que no).
#   4. Súbelo a GitHub con el commit:
#        feat: ejercicios del tema 02
#
# Nombre completo:
# Mi app se llama:
# =============================================================


# -------------------------------------------------------------
# EJERCICIO 1 · ¿Alcanza el dinero?
# -------------------------------------------------------------
# Pregunta con input() cuánto dinero tiene el usuario y cuánto
# cuesta lo que quiere comprar.
#   - Si le alcanza: muestra cuánto le sobra.
#   - Si no: muestra cuánto le falta.
#
# Así debe verse (si escribe 20000 y 26500):
#   Te faltan $6,500

# Tu código aquí:

miDinero = int(input("CUANTO DINERO TIENES?: "))
costo = int(input("CUANTO CUESTA EL PRODUCTO?: "))

if miDinero >= costo:
    print(f"te sobra: {miDinero - costo:,.0f}")
else:
    print(f"te faltan: {costo - miDinero:,.0f}")

print("-------------------------------------------------")



# -------------------------------------------------------------
# EJERCICIO 2 · El nivel del usuario
# -------------------------------------------------------------
# Una app de ejercicio clasifica al usuario según los minutos que
# entrenó en la semana. Pregunta los minutos y muestra el nivel:
#   - 0 minutos:            "Sin actividad: ¡empieza hoy!"
#   - de 1 a 149 minutos:   "Nivel principiante"
#   - de 150 a 299 minutos: "Nivel activo"
#   - 300 o más:            "Nivel atleta"
#
# Usa if, elif y else. Prueba los cuatro casos.

# Tu código aquí:

tiempo = int(input("cuantos minutos llevas conectado?: "))

if tiempo == 0:
    print("Sin actividad: ¡empieza hoy!")
elif tiempo >= 1 and tiempo <= 149:
    print("Nivel principiante")
elif tiempo >= 150 and tiempo <= 299:
    print("Nivel activo")
else:
    print("Nivel atleta")

print("------------------------------------------------")

# -------------------------------------------------------------
# EJERCICIO 3 · ¿Se puede agendar la cita?
# -------------------------------------------------------------
# Una barbería atiende de 8 a 19 horas, de lunes a sábado.
# Pregunta el día (en minúsculas) y la hora (número entero).
#   - Si es domingo:                 "Los domingos no atendemos"
#   - Si la hora está fuera de 8–19: "Fuera del horario de atención"
#   - Si todo está bien:             "Cita disponible"
#
# Usa and / or en al menos una condición.
#
# Pista: si el usuario escribe "Domingo" con mayúscula, tu if no lo
# reconoce. Prueba:  dia = input("Día: ").lower()
# .lower() convierte el texto a minúsculas (.upper() a mayúsculas).

# Tu código aquí:

dia = str(input("QUE DIAS DE LA SEMANA ES?: ")).lower()
hora = int(input("QUE HORA ES?: "))

if dia == "domingo":
    print("Los domingos no atendemos")
elif hora < 8 and hora < 19:
    print("Fuera del horario de atención")
else:
    print("Cita disponible")

print("----------------------------------------------------------")

# -------------------------------------------------------------
# EJERCICIO 4 · Encuentra el error
# -------------------------------------------------------------
# Este código tiene 3 errores. Corrígelos y explica en un
# comentario qué estaba mal en cada uno.
#
#   clave = input("Clave: ")
#   if clave = "1234"
#   print("Bienvenido")
#   else:
#       print("Clave incorrecta")

# Tu código corregido aquí:

clave = input("Clave: ")
if clave == "1234":
  print("Bienvenido")
else:
      print("Clave incorrecta")

print("-------------------------------------------")

# Error 1: LA VARIABLE CLAVE Y EL IF Y ELSE TENIAN UN ESPACIO DETRAS DE ELLAS
# Error 2:FALTABA 1 IGUAL EN LA COMPARACION DEL IF
# Error 3:LE FALTABAN LOS : AL FINAL DE LA CONDICION DEL IF


# -------------------------------------------------------------
# EJERCICIO 5 · Caja registradora con menú
# -------------------------------------------------------------
# Haz un menú con while que se repita hasta que el usuario elija
# salir:
#   1. Agregar un producto (pregunta el precio y súmalo al total)
#   2. Ver el total
#   3. Salir
#
# Si escribe una opción que no existe, muestra "Opción no válida".
# Pista: crea total = 0 antes del while y en la opción 1 haz
#        total = total + precio
#
# Así debe verse:
#   1. Agregar producto  2. Ver total  3. Salir
#   Opción: 1
#   Precio: 4500
#   Opción: 1
#   Precio: 2000
#   Opción: 2
#   Total: $6,500

# Tu código aquí:


total = 0

while True:
    print("1. Agregar producto")
    print("2. Ver total")
    print("3. Salir")

    opcion = int(input("Opción: "))

    if opcion == 1:
        precio = float(input("Precio: "))
        total = total + precio

    elif opcion == 2:
        print(f"Total: ${total:,.0f}")

    elif opcion == 3:
        print("Saliendo...")
        break

    else:
        print("Opción no válida")


# =============================================================
# EJERCICIO 6 · LLÉVALO A TU APP  (va en src/app.py de tu app, no aquí)
# =============================================================
# Tu app ya saluda (tema 01). Hoy le das un MENÚ. En el archivo
# src/app.py de tu app:
#   1. Deja la bienvenida al inicio.
#   2. Agrega un menú con while con al menos 3 opciones
#      que tengan sentido para tu app, más "Salir".
#   3. Cada opción hace algo (aunque sea sencillo): preguntar un
#      dato, calcular algo o mostrar un mensaje.
#   4. Al menos una opción valida un dato con if
#      (por ejemplo: que un número no sea negativo).
#   5. Si eligen una opción que no existe: "Opción no válida".
#
# Ejemplo para una app de citas de barbería:
#   ===== BARBERÍA EL CORTE =====
#   1. Ver precios
#   2. Agendar cita
#   3. Calcular total de cortes
#   4. Salir
#
# Con esto tu app ya se ve como una app de verdad. En el próximo
# tema guardamos varias citas, productos o registros en listas.
# =============================================================