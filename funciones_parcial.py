from datetime import *


def validar_edad():
    contador = 0
    while contador < 3:
        try:
            edad = int(input("cual es la edad del paciente \n -> "))
            return edad
        except ValueError:
            print("digite nuevamente la edad ")
            contador += 1
    return False


def validar_fecha_nacimiento():
    contador = 0
    while contador < 3:
        try:
            fecha_nacimiento = input(
                "Ingrese su fecha de nacimiento (formato YYYY-MES-DD): ")
            nacimimento = datetime.strptime(fecha_nacimiento, "%Y-%B-%d")
            if nacimimento.date() != datetime.now().date():
                return fecha_nacimiento
        except ValueError:
            contador += 1
            continue
    return False


def validar_documento():
    contador = 0
    while contador < 3:
        try:
            documento = int(input(" cual es el documento del paciente \n -> "))
            return documento
        except ValueError:
            print("digite nuevamente el documento ")
            contador += 1
    return False


def validar_documento_2():
    while True:
        try:
            documento = int(input(" cual es el documento del paciente \n -> "))
            return documento
        except ValueError:
            print("digite nuevamente el documento ")


def validar_LH():
    contador = 0
    while contador < 3:
        try:
            LH = float(
                input("cual es el nivel LH del paciente con un decimal \n -> "))
            return LH
        except ValueError:
            print("digite nuevamente los niveles LH con un decimal ")
            contador += 1
    return contador


def contador_menos_edad(complementaria, diccionario_pacientes):
    años = validar_años()
    cantidad_edad = list(filter(lambda datos: datos[2] < años, list(
        diccionario_pacientes.values())))
    numero_x_edad = len(cantidad_edad)
    print(f" hay {numero_x_edad} usuario con menos de la edad de {años}")
    return numero_x_edad


def contador_mayor_edad(complementaria, diccionario_pacientes):
    años = validar_años()
    cantidad_edad = list(filter(lambda datos: datos[2] > años, list(
        diccionario_pacientes.values())))
    numero_x_edad = len(cantidad_edad)
    print(f" hay {numero_x_edad} usuario mayores de la edad de {
          años}")
    return numero_x_edad


def validar_años():
    while True:
        try:
            años = int(
                input("introduzca la edad filtro \n -> "))
            return años
        except ValueError:
            print(
                "digite el numero de años que actuara como filtro ")
            continue


def validar_eps(tipo_EPS):
    while True:
        if tipo_EPS in ["SURA", "COOMEVA", "IPS UNIVERSITARIA", "SALUD TOTAL"]:
            return tipo_EPS
        else:
            tipo_EPS = input("""a cual eps pértenece 
SURA
COOMEVA
IPS UNIVERSITARIA
SALUD TOTAL 
-> """).upper()
            continue
