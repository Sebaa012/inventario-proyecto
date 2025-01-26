from time import sleep
def MENU():
    while True:
        def INGRESE():
            print("\tLa función 'Registrar información de un equipo' no está disponible todavía.")
        def CONSULTE():
            print("\tLa función 'Consultar información de un equipo' no está disponible todavía.")
        def MODIFIQUE():
            print("\tLa función 'Modificar información de un equipo' no está disponible todavía.")
        def DESINCORPORE():
            print("\tLa función 'Desincorporar un equipo del inventario' no está disponible todavía.")
        def REPORTE():
            print("\tLa función 'Ver informe de inventario' no está disponible todavía.")
        print("\t1. Registrar información de un equipo")
        print("\t2. Consultar información de un equipo")
        print("\t3. Modificar información de un equipo")
        print("\t4. Desincorporar un equipo del inventario")
        print("\t5. Ver informe de inventario")
        print("\t6. Salir.")
        SELEC = input("¿Qué desea realizar?: ")
        if SELEC == "1":
            INGRESE()
        elif SELEC == "2":
            CONSULTE()
        elif SELEC == "3":
            MODIFIQUE()
        elif SELEC == "4":
            DESINCORPORE()
        elif SELEC == "5":
            REPORTE()
        elif SELEC == "6":
            print("\tAdiós Mundo\n\n")
            break
        else:
            print("\tIngrese una opción correcta\n")
        sleep(2)
MENU()