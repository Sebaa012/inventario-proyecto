def MENU():
    while True:
        print("\t\t\tInventario de Equipos Informáticos\n")
        print("\t1. Registrar datos de un equipo")
        print("\t2. Consultar datos de un equipo")
        print("\t3. Modificar datos de un equipo")
        print("\t4. Desincorporar un equipo del inventario")
        print("\t5. Ver reporte de inventario")
        print("\t6. Salir.")
        opcion = input("\tElija una opción: ")
        if opcion == "1":
            #ING()
            print("Usted ingresó en registro de datos\n")
        elif opcion == "2":
            #CONS()
            print("Usted ingresó en consulta de datos de un equipo\n")
        elif opcion == "3":
            #MODIF()
            print("Usted ingresó en modificar datos en el registro de un equipo\n")
        elif opcion == "4":
            #ELIM()
            print("Usted ingresó en desincorporar un dispositivo del inventario\n")
        elif opcion == "5":
            print("Usted ingresó en el reporte de inventario\n")
            #REPORT()
        elif opcion == "6":
            print("Sayonara Bye Bye\n")
            break
        else:
            print("Ingrese una opción del uno al seis, por favor\n")
        input("Continue pulsando cualquier tecla: ")
MENU()