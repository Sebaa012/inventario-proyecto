from os import system
def Menu():
    while True:
        print("\t\t\tCONTROL DE INVENTARIO DE EQUIPOS\n")
        print("\t1.REGISTRAR DATOS DE UN EQUIPO\n\t2.CONSULTAR DATOS DE UN EQUIPO\n\t3.MODIFICAR DATOS DE UN EQUIPO\n\t4.DESINCORPORAR UN EQUIPO DEL INVENTARIO\n\t5.VER REPORTE DE INVENTARIO\n\t6.SALIR. \n")
        ELEC = input("\t\t\tELIJA UNA OPCIÓN: ")
        system("cls")
        if ELEC == "1":
            #Ingresar()
            print("\t\t\tINGRESÓ EN REGISTRO DE DATOS\n\n")
        elif ELEC == "2":
            #Consultar()
            print("\t\t\tINGRESÓ EN CONSULTA DE DATOS DE UN EQUIPO\n\n")
        elif ELEC == "3":
            #Modificar()
            print("\t\t\tINGRESÓ EN MODIFICAR DATOS EN EL REGISTRO DE UN EQUIPO\n\n")
        elif ELEC == "4":
            #Desincorporar()
            print("\t\t\tINGRESÓ EN DESINCORPORAR UN DISPOSITIVO DEL INVENTARIO\n\n")
        elif ELEC == "5":
            print("\t\t\tINGRESÓ EN EL REPORTE DE INVENTARIO\n\n")
            #Reporte()
        elif ELEC == "6":
            print("\t\t\tHASTA PRÓXIMA\n\n")
            break
        else:
            print("\t\t\tELECCIÓN INVÁLIDA!\n\n")
        input("Pulse cualquier tecla para continuar...")
        system("cls")
Menu()
