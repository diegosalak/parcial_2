# mi idea fue empezar por pedir y procesar todos los datos que conformaran la lista de la informacion del paciente dentro del diccionario
# esto de acuerdo a la informacion sobre LH las excepciones y lla forma de procesar el codigo (para accer el codigo opte por una secuencia de
# condicionales para que al final solo concatenara, el conteo lo use con un contador cada que entre a la opcion de agregar paciente.
# el contador lo coloco casi al final de la solicitud de la informacion para evitar que este quede en un numero si el programa se llegara a repetir
# por equivocarse 3 veces )
from datetime import datetime
from funciones_parcial import *
contador = 0
contador_pacientes = 0
diccionario_pacientes = {}
while contador < 3:
    contador = 0
    menu = int(input("""
que opcion desea ejecutar en nuestro programa
1. ingresar paciente
2. informe de afiliacion EPS
3. borrar paciente
4. salir
-> """))
    if menu == 1:
        lista_personal = []
        nombre_paciente = input("nombre del paciente \n -> ")
        lista_personal.append(nombre_paciente)
        fecha_nacimiento = validar_fecha_nacimiento()
        if fecha_nacimiento == False:
            continue
        else:
            lista_personal.append(fecha_nacimiento)
        edad = validar_edad()
        if edad == False:
            continue
        else:
            lista_personal.append(edad)
        documento = validar_documento()
        if documento == False:
            continue
        else:
            lista_personal.append(documento)
        genero = input("genero del paciente H (Hombre) o M (Mujer) \n -> ")
        menopaucia = int(input(""" 
1. tiene menopaucia
2. no tiene  menopaucia 
-> """))
        LH = validar_LH()
        tupla_diagnostico = ()
        if LH == contador:
            continue
        else:
            tupla_diagnostico += (LH,)
            if genero == "F":
                if menopaucia == 1:
                    if 14.2 <= LH <= 52.3:
                        nivel_LH = "niveles normales"
                    else:
                        nivel_LH = "niveles anormales"
                    tupla_diagnostico += (nivel_LH,)
                elif menopaucia == 2:
                    if 5 <= LH <= 25:
                        nivel_LH = "niveles normales"

                    else:
                        nivel_LH = "niveles anormales"
                    tupla_diagnostico += (nivel_LH,)
                elif 0 <= edad <= 18:
                    if 0 <= LH <= 5:
                        nivel_LH = "niveles normales"

                    else:
                        nivel_LH = "niveles anormales"
                    tupla_diagnostico += (nivel_LH,)
                else:
                    if 5 <= LH <= 25:
                        nivel_LH = "niveles normales"

                    else:
                        nivel_LH = "niveles anormales"
                    tupla_diagnostico += (nivel_LH,)
            elif genero == "H":
                if 0 <= edad <= 18:
                    if 1 <= LH <= 1.8:
                        nivel_LH = "niveles normales"

                    else:
                        nivel_LH = "niveles anormales"
                    tupla_diagnostico += (nivel_LH,)
                else:
                    if 1.8 <= LH <= 8.6:
                        nivel_LH = "niveles normales"

                    else:
                        nivel_LH = "niveles anormales"
                tupla_diagnostico += (nivel_LH,)
        lista_personal.append(tupla_diagnostico)
        afiliacion = input("""a que tipo de afiliacion pertenece EPS O SISBEN 
->  """).upper()
        if afiliacion == "EPS":
            tipo_EPS = input("""a cual eps pértenece 
SURA
COOMEVA
IPS UNIVERSITARIA
SALUD TOTAL 
-> """).upper()
            tipo_EPS = validar_eps(tipo_EPS)

            CODIGO = "EPS-{}-{}".format(tipo_EPS, contador_pacientes)
            lista_personal.append(CODIGO)
        if afiliacion == "SISBEN":
            CODIGO = "EPS-{}-{}".format(afiliacion, contador_pacientes)
            lista_personal.append(CODIGO)

        print(f" el paciente {nombre_paciente} identificado con la cedula {
              documento} ingreso exitosamente su resultado: \n {tupla_diagnostico}")
        diccionario_pacientes[documento] = lista_personal
        print(diccionario_pacientes)
    if menu == 2:
        menu_2 = int(input("""Que desea hacer
1. buscar paciente
2. ver cant. paciente 
3. ver cantidad pacientes menores a (x) años
4. ver cantidad de pacientes mayores a (x) años
-> """))
        if menu_2 == 1:
            buscador = validar_documento_2()
            lista_informacion = diccionario_pacientes.get(
                buscador, "el paciente con el numero de identificacion " + str(buscador) + " no existe en la base de datos ")
            print("los datos del usuario son: ")
            for datos in lista_informacion:
                print(datos)
        elif menu_2 == 2:
            numero_llaves = len(diccionario_pacientes)
            print(" la cantidad de pacientes es " + str(numero_llaves))
        elif menu_2 == 3:
            contador_menos_edad(validar_años, diccionario_pacientes)
        elif menu_2 == 4:
            contador_mayor_edad(validar_años, diccionario_pacientes)
        else:
            print(" no escogio una opcion valida del menu numero 2")

    if menu == 3:
        paciente_eliminar = validar_documento_2()
        diccionario_pacientes.pop(paciente_eliminar)
        print(" el nuevo diccionario quedo asi:   {}".format(diccionario_pacientes))
    if menu == 4:
        print("SALIO DEL PROGRAMA. ADIOS")
