

#      CYBERSHIELD.   # 


print("==========================================")
print("              CYBERSHIELD")
print("==========================================")
print("Protegemos tus equipos y tu información.")

# Precio por equipo
precio = 90000

# Lista para guardar las solicitudes
solicitudes = []

while True:
    print("\n========== MENÚ PRINCIPAL ==========")
    print("1. Ver servicios")
    print("2. Registrar solicitud de protección")
    print("3. Ver solicitudes registradas")
    print("4. Salir")
    print("===================================")

    opcion = input("Seleccione una opción: ")

    # OPCIÓN 1: VER SERVICIOS
    if opcion == "1":
        print("\n========== SERVICIOS DE CYBERSHIELD ==========")

        print("\n1. Antivirus y seguridad informática")
        print("   Detectamos y prevenimos amenazas que puedan afectar los equipos.")

        print("\n2. Protección de redes")
        print("   Evitamos que personas no autorizadas ingresen a las redes.")

        print("\n3. Seguridad de la información")
        print("   Mantenemos los datos de las empresas protegidos y seguros.")

        print("\n4. Detección de vulnerabilidades")
        print("   Encontramos debilidades que podrían poner en riesgo los sistemas.")

        print("\n5. Consultoría en ciberseguridad")
        print("   Brindamos recomendaciones para mejorar la seguridad digital.")

        print("\n6. Respaldo y recuperación de datos")
        print("   Creamos copias de seguridad para recuperar archivos en caso de pérdida.")

        print("\n==============================================")

        input("\nPresiona ENTER para volver al menú...")
        print()

    # OPCIÓN 2: REGISTRAR SOLICITUD
    elif opcion == "2":
        print("\n===== NUEVA SOLICITUD =====")

        nombre = input("Nombre del cliente: ")
        empresa = input("Nombre de la empresa: ")

        try:
            equipos = int(input("Cantidad de equipos a proteger: "))

            if equipos <= 0:
                print("Error: ingrese al menos un equipo.")

            else:
                total = equipos * precio

                solicitud = {
                    "nombre": nombre,
                    "empresa": empresa,
                    "equipos": equipos,
                    "total": total
                }

                solicitudes.append(solicitud)

                print("\nSolicitud registrada correctamente.")
                print(f"Cliente: {nombre}")
                print(f"Empresa: {empresa}")
                print(f"Equipos: {equipos}")
                print(f"Costo total: ${total:,.0f}")

        except ValueError:
            print("Error: debe ingresar una cantidad entera.")

        input("\nPresiona ENTER para continuar...")

    # OPCIÓN 3: VER SOLICITUDES
    elif opcion == "3":
        print("\n===== SOLICITUDES REGISTRADAS =====")

        if len(solicitudes) == 0:
            print("Todavía no hay registros.")

        else:
            for i in range(len(solicitudes)):
                print(f"\nSolicitud {i + 1}")
                print(f"Cliente: {solicitudes[i]['nombre']}")
                print(f"Empresa: {solicitudes[i]['empresa']}")
                print(f"Equipos: {solicitudes[i]['equipos']}")
                print(f"Total: ${solicitudes[i]['total']:,.0f}")

            print(f"\nTotal de solicitudes: {len(solicitudes)}")

        input("\nPresiona ENTER para volver al menú...")

    # OPCIÓN 4: SALIR
    elif opcion == "4":
        print("\nGracias por confiar en CyberShield.")
        print("¡Hasta pronto!")
        break

    else:
        print("Opción no válida. Seleccione del 1 al 4.")
