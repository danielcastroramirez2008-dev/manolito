# Aquí empieza mi app


print("==============================")
print("        CYBER-SHEYD"           )
print("==============================")

nombre = input("¿Cómo te llamas?:  ")
empresa = input("¿Cuál es el nombre de tu empresa?:  ")
equipos = int(input("¿Cuántos equipos deseas proteger?:  "))

precio = 80000
valorTotal = equipos * precio

print(f"Hola {nombre} de la empresa {empresa} solicitaste proteger {equipos} equipos, el costo total es de ${valorTotal}")