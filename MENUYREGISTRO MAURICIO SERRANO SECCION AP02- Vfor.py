import os
from time import sleep
from datetime import date

Hoy = date.today().strftime("%d/%m/%Y")
Fe_Reg = Hoy
Fe_Des = ("00/00/0000")
Fe_Mod = ("00/00/0000")

def Limpia():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

def Registrar():
    with open('Registro.txt', 'a') as BD:
        print("\t\t\tUsted ha ingresado en el registro del inventario\n")
        while True:
            try:
                cant = int(input("\t\tIngrese la cantidad de equipos que quiere guardar: "))
                if cant <= 0:
                    print(f"\t\tImposible! No puedes ingresar {cant} equipos!")
                    sleep(1)
                    Limpia()
                    continue
                else:
                    for c in range(cant):
                        Num_B_Pub = input("\tIngrese el Número de bien público del equipo: ").upper()
                        SeriaL = input("\tIngrese el serial del equipo: ").upper()
                        Marca = input("\tIngrese la marca del equipo: ").upper()
                        ModeLo = input("\tIngrese el modelo del equipo: ").upper()
                        BD.writelines(f"{Num_B_Pub} {SeriaL} {Marca} {ModeLo} {Fe_Reg} {Fe_Des} {Fe_Mod}\n")
                        if c < cant-1:
                            print("Siguiente equipo....")
                        else:
                            print("Se han guardado todos los equipos.")
                        sleep(1)
                        Limpia()
            except ValueError:
                    print("\t\tSolo puedes ingresar numeros.")
                    sleep(2)
                    continue
            break
            
def Menu():
    while True:
        print("\t\t\t================================")
        print("\t\t\tCONTROL DE INVENTARIO DE EQUIPOS")
        print("\t\t\t================================\n")
        print("\t1.REGISTRAR DATOS DE UN EQUIPO")
        print("\t2.CONSULTAR DATOS DE UN EQUIPO")
        print("\t3.MODIFICAR DATOS DE REGISTRO A UN EQUIPO")
        print("\t4.DESICORPORAR UN EQUIPO DEL INVENTARIO")
        print("\t5.VER REPORTE DE INVENTARIO")
        print("\t6.SALIR")
        ELEC = input("\t\t\tELIJA UNA OPCIÓN: ")
        Limpia()
        if ELEC == "1":
            Registrar()
        elif ELEC == "2":
            #Consultar()
            print("\t\t\tINGRESÓ EN CONSULTA DE DATOS DE UN EQUIPO\n\n")
        elif ELEC == "3":
            #Modificar()
            print("\t\t\tINGRESÓ EN MODIFICAR DATOS EN EL REGISTRO DE UN EQUIPO\n\n")
        elif ELEC == "4":
            #Desincorporar()
            print("\t\t\tINGRESÓ EN DESINSCORPORAR UN EQUIPO DEL INVENTARIO\n\n")
        elif ELEC == "5":
            print("\t\t\tINGRESÓ EN EL REPORTE DE INVENTARIO\n\n")
            #Reporte()
        elif ELEC == "6":
            print("\t\t\tSayonara Bye Bye\n\n")
            sleep(2)
            break
        else:
            print("\t\t\tOPCIÓN INVÁLIDA!\n\n")
        input("Pulse cualquier tecla para continuar...")
        Limpia()
Menu()
