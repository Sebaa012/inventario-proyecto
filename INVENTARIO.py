import os #BIBLIOTECA "os" MÓDULO QUE NOS PERMITE INTERACTUAR CON EL SISTEMA OPERATIVO
print("==================================")
print("INVENTARIO DE EQUIPOS INFORMÁTICOS")
print("==================================")
RUTA_BD = 'BASE_DE_DATOS.txt'
if not os.path.exists(RUTA_BD): # "path" Y "exist" COMPRUEBAN SI EL ARCHIVO EXISTE EN EL SO 
    with open(RUTA_BD, 'w') as BASE_DAT: # LUEGO SE CREA SI NO EXISTE
        DATOS = BASE_DAT.write("")

print("MENU DE OPCIONES" + "\n")
print("1. INGRESAR UN EQUIPO AL INVENTARIO" + "\n" + 
"2. BUSCAR UN EQUIPO DENTRO DEL INVENTARIO" + "\n" + 
"3. MODIFICAR LOS DATOS DE UN EQUIPO EN EL INVENTARIO"+ "\n" +
"4. RETIRAR UN EQUIPO DEL INVENTARIO" + "\n" + 
"5. MOSTRAR TODOS LOS EQUIPOS DEL INVENTARIO" + "\n" + 
"6. SALIR DEL PROGRAMA")
OPCION = int(input("ELIJA UNA OPCION: "))
    
def HACER_BD(RUTA_BD):
        with open(RUTA_BD, 'r') as BASE_DAT:
            CONTENIDO = BASE_DAT.read()
            LISTA_CONT = CONTENIDO.splitlines() #Se utiliza el método splitlines() 
            #para dividir la cadena CONTENIDO en una lista de líneas.
            INVENTARIO = [LINEA.split(",") for LINEA in LISTA_CONT] # Aquí se utiliza una comprensión de lista para crear una nueva lista llamada INVENTARIO. 
            #Para cada LINEA en LISTA_CONT, se llama al método split(","), que divide cada línea en partes, utilizando la coma como separador. 
            #El resultado es que INVENTARIO será una lista de listas, 
            #donde cada sublista representa una línea del archivo y contiene los elementos separados por comas.
            return INVENTARIO
        
def AÑADE_EQUI(RUTA_BD, EQUIPOS):
    with open(RUTA_BD, 'a') as BASE_DAT:
        for ELEMENTO in EQUIPOS:
            DATOS = BASE_DAT.write(",".join(map(str, ELEMENTO)) + '\n') #convierte los elementos de ELEMENTO a cadenas, los une en una sola cadena separada por comas, 
            #añade un salto de línea al final y escribe esa cadena en el archivo BASE_DAT

def VER_CONT(RUTA_BD):
    with open(RUTA_BD, 'r') as BASE_DAT:
        CONTENIDO = BASE_DAT.read()
        return CONTENIDO
        
def BUSCAR_EQUIPO(INVENTARIO, BUSCA_SERIAL):
    for CONT in range(len(INVENTARIO)):
        if INVENTARIO[CONT][0] == BUSCA_SERIAL:
            return INVENTARIO[CONT]
        
def ELIMINAR_EQUIPO(INVENTARIO, BUSCA_SERIAL):
    for CONT in range(len(INVENTARIO)):
        if INVENTARIO[CONT][0] == BUSCA_SERIAL:
            del INVENTARIO[CONT]

def ACTUALIZAR_INVENT(RUTA_BD, INVENTARIO):
        with open(RUTA_BD, 'w') as BASE_DAT:
            for COMPONENTES in INVENTARIO:
                BASE_DAT.write(','.join(map(str, COMPONENTES)) + '\n') 

while OPCION > 0 or OPCION < 7:
    if OPCION == 1:
        CANT = int(input("INGRESA LA CANTIDAD DE EQUIPOS QUE QUIERES REGISTRAR: "))
        EQUIPOS = []
        for CONT in range(CANT):
            SERIAL = input("INGRESA EL SERIAL: ")
            MARCA = input("INGRESE LA MARCA: ")
            MODELO = input("INGRESE EL MODELO: ")
            RAM = int(input("INGRESE LA CANTIDAD DE MEMORIA RAM: "))
            ALMAC = int(input("INGRESE LA CANTIDAD DE ALMACENAMIENTO DEL EQUIPO: "))
            CPU = input("INGRESE EL PROCESADOR: ")
            print(f"SU SERIAL ES: {SERIAL}")
            EQUIPOS.append([SERIAL, MARCA, MODELO, RAM, ALMAC, CPU])
        AÑADE_EQUI(RUTA_BD, EQUIPOS)
        break

    elif OPCION == 2:
        BUSCA_SERIAL = input("INGRESE EL SERIAL DEL EQUIPO QUE DESEA MOSTRAR: ")
        INVENTARIO = HACER_BD(RUTA_BD)
        COMPONENTES = BUSCAR_EQUIPO(INVENTARIO, BUSCA_SERIAL)
        if COMPONENTES == None:
            print("NO ESTA EN EL INVENTARIO.")
            break
        print(f"SERIAL: {COMPONENTES[0]}, MARCA: {COMPONENTES[1]}, MODELO: {COMPONENTES[2]}, RAM:{COMPONENTES[3]}, ALMACENAMIENTO: {COMPONENTES[4]}, CPU: {COMPONENTES [5]}")
        break

    elif OPCION == 3:
        BUSCA_SERIAL = input("INGRESA EL SERIAL DEL EQUIPO QUE DESEA MODIFICAR: ")
        INVENTARIO = HACER_BD(RUTA_BD)
        COMPONENTES = BUSCAR_EQUIPO(INVENTARIO, BUSCA_SERIAL)
        if COMPONENTES == None:
            print("NO ESTA EN EL INVENTARIO.")
            break
        MODI = int(input("INGRESE EL DATO QUE DESEAS MODIFICAR" + "\n" + 
        "1. SERIAL" + "\n" + "2. MARCA" + "\n" + "3. MODELO" + 
        "\n" + "4. RAM" + "\n" +  "5. ALMACENAMIENTO" + "\n" + "6. CPU" + "\n"))
        if MODI == 1:
            COMPONENTES[0] = input("INGRESE EL NUEVO SERIAL: ")
        elif MODI == 2:
            COMPONENTES[1] = input("INGRESE UNA NUEVA MARCA: ")
        elif MODI == 3:
            COMPONENTES[2] = input("INGRESE UN NUEVO MODELO: ")
        elif MODI == 4:
            COMPONENTES[3] = input("INGRESE UNA NUEVA CANTIDAD DE MEMORIA RAM: ")
        elif MODI == 5:
            COMPONENTES[4] = input("INGRESE UNA NUEVA CANTIDAD DE ALMACENAMIENTO INTERNO: ")
        elif MODI == 6:
            COMPONENTES[5] = input("INGRESE UN NUEVO MODELO DE PROCESADOR: ")
        else:
            print("NO ES UNA OPCION VALIDA.")
            break
        ACTUALIZAR_INVENT(RUTA_BD, INVENTARIO)
        print(f"SERIAL: {COMPONENTES[0]}, MARCA: {COMPONENTES[1]}, MODELO: {COMPONENTES[2]}, RAM:{COMPONENTES[3]}, ALMACENAMIENTO: {COMPONENTES[4]}, CPU: {COMPONENTES [5]}")
        break

    elif OPCION == 4:
        BUSCA_SERIAL = input("INGRESA EL SERIAL DEL EQUIPO QUE DESEA RETIRAR: ")
        INVENTARIO = HACER_BD(RUTA_BD)
        COMPONENTES = ELIMINAR_EQUIPO(INVENTARIO, BUSCA_SERIAL)
        ACTUALIZAR_INVENT(RUTA_BD, INVENTARIO)
        BASE_ACT = VER_CONT(RUTA_BD)
        print(BASE_ACT)
        break

    elif OPCION == 5:
        INVENTARIO = HACER_BD(RUTA_BD)
        BD = VER_CONT(RUTA_BD)
        print(f"INVENTARIO TOTAL: \n {BD}")
        break
    
    elif OPCION == 6:
        print("EL PROGRAMA HA FINALIZADO.")
        break
    else:
        while OPCION < 0 or OPCION > 6:
            OPCION = int(input("INGRESE UNA OPCION VALIDA: "))