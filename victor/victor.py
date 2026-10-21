# =============================================================
# Tema 01 · Variables, tipos, entrada y salida · EJERCICIOS
# python-adso · SENA ADSO
#
# INSTRUCCIONES
#   1. Copia este archivo al repositorio de TU app como:
#        ejercicios/tema-01.py
#   2. Resuelve cada ejercicio debajo de su enunciado.
#   3. Ejecuta el archivo y prueba que todo funcione.
#   4. Súbelo a GitHub con el commit:
#        feat: tema 01 y bienvenida de la app
#
# Nombre completo:
# Mi app se llama:
# =============================================================


# -------------------------------------------------------------
# EJERCICIO 1 · Tarjeta de presentación
# -------------------------------------------------------------
# Crea tres variables: tu nombre (texto), tu edad (entero) y tu
# estatura en metros (decimal). Muestra las tres con UN solo print
# usando f-string.
#
# Así debe verse:
#   Soy Ana, tengo 19 años y mido 1.62 m.

# Tu código aquí:
 
nombre = "ALEX"
años = 17
estatura = 1.82

print(f"soy {nombre} tengo {17} años y mido {estatura:.2f}")


# -------------------------------------------------------------
# EJERCICIO 2 · ¿De qué tipo es?
# -------------------------------------------------------------
# Crea estas cuatro variables y muestra el tipo de cada una con type():
#   a = "100"
#   b = 100
#   c = 100.0
#   d = "cien"
#
# Después, en un comentario, responde: ¿por qué "100" y 100 no son
# lo mismo para Python?

# Tu código aquí:

print("---------------------------------------")

a="100"
b= 100
c= 100.00
d= "cien"

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print("---------------------------------------")

# Respuesta:

#el 100 sin comillas lo toma como tipo numero y si tiene comillas lo toma como tipo texto, las comillas hace que el tipo de dato cambie de number a string

# -------------------------------------------------------------
# EJERCICIO 3 · La cuenta del almuerzo
# -------------------------------------------------------------
# Pregunta con input():
#   - el valor de la cuenta
#   - cuántas personas van a pagar
#   - el porcentaje de propina (por ejemplo 10)
#
# Muestra: el valor de la propina, el total con propina y cuánto
# paga cada persona. Los valores en pesos, con separador de miles.
#
# Así debe verse (si escriben 85000, 3 y 10):
#   Propina:          $8,500
#   Total:            $93,500
#   Cada uno paga:    $31,167

# Tu código aquí:



valor = int(input("precio plata: "))
personas = int(input("personas pagar: "))
propina = int(input("precio propina: "))

propinaReal = valor * propina / 100
total = propinaReal + valor
pagoIndividual = total / personas

print(f"{propinaReal:,.0f}")
print(f"{total:,.0f}")
print(f"{pagoIndividual:,.0f}")

print("---------------------------------")

# print("---------------------------------------")
# -------------------------------------------------------------
# EJERCICIO 4 · Encuentra el error
# -------------------------------------------------------------
# Este código tiene 2 errores. Corrígelos y explica en un
# comentario qué estaba mal en cada uno.
#
#   precio = input("Precio del producto: ")
#   unidades = input("Unidades: ")
#   print("Total a pagar: " + precio * unidades)

# Tu código corregido aquí:



precio = int(input("precio del producto: "))
unidades = int(input("Unidades: "))

totalApagar = precio * unidades

print("total a pagar: " , totalApagar)

print("---------------------------------------")

# Error 1:NO SE LES ASIGNO UN TIPO DE DATO A LAS VARIABLES UNIDADES Y PRECIO , ESTO HACE QUE PYTHON NO LAS RECONOSCA

# Error 2:EN EL PRINT NO SE HACEN LAS OPERACIONES, ES NECESARIO CREAR UNA VARIABLE NUEVA QUE CONTENGA LA OPERACION Y IMPRIMIR ESA VARIABLE , ADEMAS QUE ESTA INTENTANDO CONCATENAR CON UN + 


# -------------------------------------------------------------
# EJERCICIO 5 · Inventario rápido
# -------------------------------------------------------------
# Pregunta el nombre de un producto, cuántas unidades hay y el
# precio de cada unidad. Muestra un resumen como este:
#
#   ===== INVENTARIO =====
#   Producto:   Tabla de pino
#   Unidades:   40
#   Precio:     $18,000
#   Valor total: $720,000
#   ======================

# Tu código aquí:


nombre = str(input("Ingrese el nombre del producto: "))
unidades = int((input("Ingrese la cantidad de unidades: ")))
precio = float(input("agregue el precio del prducto: "))

valorTotal = unidades * precio

print("===== INVENTARIO =====")
print("Producto:", nombre)
print("Unidades:", unidades)
print("Precio:", precio)
print("Valor total:", valorTotal)
print("======================")


# =============================================================
# EJERCICIO 6 · LLÉVALO A TU APP  (va en tu app.py, no aquí)
# =============================================================
# En el archivo app.py de tu proyecto, crea la pantalla de bienvenida
# de tu app. Debe:
#   1. Mostrar el nombre de tu app con un encabezado visible.
#   2. Preguntarle al usuario al menos 2 datos con input()
#      (por ejemplo: su nombre y algo que tenga sentido en tu app).
#   3. Responder con un mensaje que use esos datos (f-string).
#   4. Al menos un dato debe ser un número con el que hagas una cuenta.
#
# Ejemplo para una app de citas de barbería:
#   ==============================
#        BARBERÍA EL CORTE
#   ==============================
#   ¿Cómo te llamas? Carlos
#   ¿Cuántos cortes quieres agendar? 2
#   Hola Carlos, tus 2 cortes cuestan $50,000.
#
# Este es el primer paso de tu app: en los próximos temas le
# agregamos el menú, las listas y todo lo demás.
# =============================================================