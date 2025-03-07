from os import system, rename, remove
from time import sleep
from datetime import date

Hoy = date.today().strftime("%d/%m/%Y")

def Registrar():
    Fe_Reg = Hoy
    Fe_Des = ("00/00/0000")
    Fe_Mod = ("00/00/0000")
    with open('BASE_DE_DATOS.txt', 'a') as BD:
        while True:
            print("\t\t\tREGISTRO DE INVENTARIO\n\n")
            Num_B_Pub = input("\t\tIngrese el Número de bien público: ").upper()
            SeriaL = input("\t\tIngrese el serial: ").upper()
            Marca = input("\t\tIngrese la marca: ").upper()
            dto = input("\t\tIngrese el departamento: ").upper()
            ModeLo = input("\t\tIngrese el modelo: ").upper()
            BD.writelines(f"{Num_B_Pub} {SeriaL} {Marca} {ModeLo} {dto} {Fe_Reg} {Fe_Des} {Fe_Mod}\n")
            while True:
                Seguir = input("\t\t¿REGISTRAR OTRO EQUIPO?-[S/N]: ").upper()
                if Seguir == "S":
                    print("\t\t\tCONTINUAMOS...")
                    sleep(1)
                    system("cls")
                    break
                elif Seguir == "N":
                    system("cls")
                    print("\t\t\tDATOS GUARDADOS.\n\n" +
                    "\tDe vuelta al MENÚ....")
                    return
                else:
                    print("\t\t\tINGRESE 'S' O 'N'")

def Consultar():
    while True:
        print("\t\t\tCONSULTA DE DATOS\n\n")
        BUSCA = input("\t\tIngrese el Número de Bien Público: ").upper()
        CONSEG = 0
        try:
            with open ('BASE_DE_DATOS.txt', 'r') as BD:
                    for Registr in BD:
                        CONS = Registr.strip().split()
                        if CONS[0] == BUSCA:
                            CONSEG = 1
                            print(f"\t\tNúmero de bien público: {CONS[0]}")
                            print(f"\t\tSerial:{CONS[1]}")
                            print(f"\t\tMarca: {CONS[2]}")
                            print(f"\t\tModelo:{CONS[3]}")
                            print(f"\t\tDepartamento: {CONS[4]}")
                            print(f"\t\tFecha de registro: {CONS[5]}")
                            print(f"\t\tFecha de modificación: {CONS[6]}")
                            print(f"\t\tFecha de desincorporación: {CONS[7]}")
                            break
            if CONSEG == 0:
                print("\t\t\tEQUIPO NO ENCONTRADO.")
                sleep(2)
                system("cls")
            while True:
                    Seguir = input("\n\t\t¿CONSULTAR OTRO EQUIPO?-[S/N]: ").upper()
                    if Seguir == "S":
                        print("\t\t\tCONTINUAMOS...")
                        sleep(1)
                        system("cls")
                        break
                    elif Seguir == "N":
                        system("cls")
                        print("\tDe vuelta al MENÚ....")
                        return
                    else:
                        print("\t\t\tINGRESE 'S' O 'N'")
        except FileNotFoundError:
            print("\t\t\tNO HAY ARCHIVO DE INVENTARIO.")
            sleep(2)
            break

def Desincorporar():
    while True:
        print("\t\t\tDESINCORPORAR UN EQUIPO.\n\n")
        BUSCA = input("\t\t\tIngrese el Número de Bien Público: ").upper()
        CONSEG = 0
        try:
            RESPAL = open("RESPALDO.txt", "a")
            DESIN = open("DESCARTOS.txt", "a")
            with open ('BASE_DE_DATOS.txt', 'r') as BD:
                for Registr in BD:
                    try:
                        CONS = Registr.strip().split()
                        if CONS[0] == BUSCA:
                            CONSEG = 1
                            print(f"\t\tNúmero de bien público: {CONS[0]}")
                            print(f"\t\tSerial:{CONS[1]}")
                            print(f"\t\tMarca: {CONS[2]}")
                            print(f"\t\tModelo: {CONS[3]}")
                            print(f"\t\tDepartamento: {CONS[4]}")
                            print(f"\t\tFecha de registro: {CONS[5]}")
                            print(f"\t\tFecha de modificación: {CONS[6]}")
                            print(f"\t\tFecha de desincorporación: {CONS[7]}")
                            BORRA = input("\t¿DESINCORPORAR EQUIPO?-[S/N]").upper()
                            if BORRA == "S":
                                Fe_Des = Hoy
                                CONS[7] = Fe_Des
                                ACTREGS = " ".join(CONS)
                                DESIN.write(ACTREGS + "\n")
                                print("\t\t\tEQUIPO DESINCORPORADO....")
                                sleep(2)
                            else:
                                RESPAL.write(Registr)
                        else:
                            RESPAL.write(Registr)
                    except IndexError:
                        break
            RESPAL.close()
            DESIN.close()
            remove("BASE_DE_DATOS.txt")
            rename("RESPALDO.txt", "BASE_DE_DATOS.txt")
            if CONSEG == 0:
                print("\t\t\tEQUIPO NO ENCONTRADO.")
                sleep(2)
                system("cls")
            while True:
                Seguir = input("\n\t\t¿DESINCORPORAR OTRO EQUIPO?-[S/N]: ").upper()
                if Seguir == "S":
                    print("\t\t\tCONTINUAMOS...")
                    sleep(1)
                    system("cls")
                    break
                elif Seguir == "N":
                    system("cls")
                    print("\tDe vuelta al MENÚ....")
                    return
                else:
                    print("\t\t\tINGRESE 'S' O 'N'")
        except FileNotFoundError:
            print("\t\t\tNO HAY ARCHIVO DE INVENTRARIO.")
            sleep(2)
            break 
            
def Modificar():
    while True:
        print("\t\t\tMODIFICACIÓN DE DATOS.\n\n")
        BUSCA = input("\t\t\tIngrese el Número de Bien Público: ").upper()
        CONSEG = 0
        try:
            RESPAL = open("RESPALDO.txt", "a")
            with open ('BASE_DE_DATOS.txt', 'r') as BD:
                CAMBIO = 0
                for Registr in BD:
                    CONS = Registr.strip().split()
                    if CONS[0] == BUSCA:
                        CONSEG = 1
                        Fe_Mod = Hoy
                        print("\n\t\t\tDATOS MODIFICABLES: \n")
                        #print (f"\t\t1. Serial: {CONS[1]}")
                        print (f"\t\t1. Marca: {CONS[2]}")
                        print (f"\t\t2. Modelo: {CONS[3]}")
                        print (f"\t\t3. Departamento: {CONS[4]}")
                        print ("\t\t4. Salir sin modificar.")
                        ELEC = input("\t\tINDIQUE EL DATO A MODIFICAR: ").upper()
                        if ELEC == "1":
                            Marca = input("Ingrese una marca nueva: ").upper()
                            CONS[2] = Marca
                            CAMBIO = 1
                        elif ELEC == "2":
                            ModeLo = input("Ingrese un modelo nuevo: ").upper()
                            CONS[3] = ModeLo
                            CAMBIO = 1
                        elif ELEC == "3":
                            dto = input("Ingrese un departamento nuevo: ").upper()
                            CONS[4] = dto
                            CAMBIO = 1
                        elif ELEC == "4":
                            print("\tSIN MODIFICACIONES...\n")
                            RESPAL.write(Registr)
                        else:
                            print("\t\t\t¡OPCIÓN INVÁLIDA!\n\n")
                        if CAMBIO == 1:
                            CONS[6] = Fe_Mod
                            MODREGI = " ".join(CONS)
                            RESPAL.write(MODREGI + "\n")
                            print("\t\tDATOS ACTUALIZADOS\n")
                            sleep(2)
                    else:
                        RESPAL.write(Registr)
            RESPAL.close()
            remove('BASE_DE_DATOS.txt')
            rename('RESPALDO.txt', 'BASE_DE_DATOS.txt')
            if CONSEG == 0:
                print("\t\t\tEQUIPO NO ENCONTRADO.")
                sleep(2)
                system("cls")
            while True:
                Seguir = input("\n\t\t¿MODIFICAR OTRO EQUIPO?-[S/N]: ").upper()
                if Seguir == "S":
                    print("\t\t\tCONTINUAMOS...")
                    sleep(1)
                    system("cls")
                    break
                elif Seguir == "N":
                    system("cls")
                    print("\tDe vuelta al MENÚ....")
                    return
                else:
                    print("\t\t\tINGRESE 'S' O 'N'")
        except FileNotFoundError:
            print("\t\t\tNO HAY ARCHIVO DE INVENTARIO.")
                        
def Reporte():
    print("\t\t\tREPORTE DE INVENTARIO.\n\n")
    print(f"\t{'Número de Bien Público':<30} {'Serial':<15} {'Marca':<15} {'Modelo':<10}"
          f"{'Departamento':<15} {'Registro':<15} {'Modificación':<20} {'Desincorporación':<25}")
    try:
        with open('BASE_DE_DATOS.txt', 'r') as BD:
            for REGIST in BD:
                CONS = REGIST.strip().split()
                print(f"\t{CONS[0]:<30} {CONS[1]:<15} {CONS[2]:<15} {CONS[3]:<10}" 
                f"{CONS[4]:<15} {CONS[5]:<15} {CONS[6]:<20} {CONS[7]:<25}")
    except FileNotFoundError:
        print("\t\t\tNO HAY ARCHIVO DE INVENTARIO.")
            
def Menu():
    while True:
        print("\t\t\t================================")
        print("\t\t\tCONTROL DE INVENTARIO DE EQUIPOS")
        print("\t\t\t================================\n\n")
        print("\t\t\t1.REGISTRAR DATOS DE UN EQUIPO")
        print("\t\t\t2.CONSULTAR DATOS DE UN EQUIPO")
        print("\t\t\t3.MODIFICAR DATOS DE REGISTRO A UN EQUIPO")
        print("\t\t\t4.DESICORPORAR UN EQUIPO DEL INVENTARIO")
        print("\t\t\t5.VER REPORTE DE INVENTARIO")
        print("\t\t\t6.SALIR DEL PROGRAMA\n")
        ELEC = input("\t\t\tELIJA UNA OPCIÓN: ")
        system("cls")
        if ELEC == "1":
            Registrar()
        elif ELEC == "2":
            Consultar()
        elif ELEC == "3":
            Modificar()
        elif ELEC == "4":
            Desincorporar()
        elif ELEC == "5":
            Reporte()
        elif ELEC == "6":
            print("\t\t\tPROGRAMA FINALIZADO\n\n")
            sleep(1.5)
            break
        else:
            print("\t\t\t¡OPCIÓN INVÁLIDA!\n\n")
        input("Pulse 'ENTER' para continuar...")
        system("cls")
Menu()
