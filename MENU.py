from os import system
def MENU():
    while True:
        print("\t\t\tCONTROL DE INVENTARIO DE EQUIPOS\n")
        print("\t1.REGISTRAR DATOS DE UN EQUIPO\n\t2.CONSULTAR DATOS DE UN EQUIPO\n\t3.MODIFICAR DATOS DE UN EQUIPO\n\t4.DESINCORPORAR UN EQUIPO DEL INVENTARIO\n\t5.VER REPORTE DE INVENTARIO\n\t6.SALIR. \n")
        OPCION = input("\t\t\tELIJA UNA OPCIÓN: ")
        system("clear")
        if OPCION == "1":
            #INGRESO()
            print("\t\t\tINGRESÓ EN REGISTRO DE DATOS\n\n")
        elif OPCION == "2":
            #CONSULTA()
            print("\t\t\tINGRESÓ EN CONSULTA DE DATOS DE UN EQUIPO\n\n")
        elif OPCION == "3":
            #MODIF()
            print("\t\t\tINGRESÓ EN MODIFICAR DATOS EN EL REGISTRO DE UN EQUIPO\n\n")
        elif OPCION == "4":
            #DESINC()
            print("\t\t\tINGRESÓ EN DESINCORPORAR UN DISPOSITIVO DEL INVENTARIO\n\n")
        elif OPCION == "5":
            print("\t\t\tINGRESÓ EN EL REPORTE DE INVENTARIO\n\n")
            #REPORTE()
        elif OPCION == "6":
            print("\t\t\tHASTA PRÓXIMA\n\n")
            break
        else:
            print("\t\t\tOPCIÓN INVÁLIDA!\n\n")
        input("Pulse cualquier tecla para continuar...")
        system("clear")
MENU()