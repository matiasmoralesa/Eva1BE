from Consola import Consola
from Bicicleta import Bicicleta
from Tv import Tv
from Scoter import Scoter

#lista de Eficiencia
listaEficiencia = ["A", "B", "C", "D", "E", "F"]

# Función para registrar un TV y agregarlo a la lista de TVs
def registrar_tv():
    print("Registrando un nuevo TV:")
    marca = input("Ingrese la marca: ")
    voltaje = int(input("Ingrese el voltaje (en voltios): "))
    precio = float(input("Ingrese el precio: "))
    eficiencia = input("Ingrese la eficiencia (A, B, C, D, E o F): ")
    tamanio = float(input("Ingrese el tamaño en pulgadas: "))

    # Validaciones simples
    if voltaje < 0 or precio < 0 or tamanio < 0 or eficiencia.upper() not in listaEficiencia:
        print("Error: Datos ingresados no válidos para registrar un TV.")
        return
    
    tv = Tv(marca, voltaje, precio, eficiencia, tamanio)
    listaTvs.append(tv)
    print("TV registrado exitosamente.")

# Función para registrar una consola y agregarla a la lista de consolas
def registrar_consola():
    print("Registrando una nueva Consola:")
    marca = input("Ingrese la marca: ")
    nombre_consola = input("Ingrese el nombre de la consola: ")
    version = input("Ingrese la versión (Lite u otra): ")
    voltaje = int(input("Ingrese el voltaje (en voltios): "))
    precio = float(input("Ingrese el precio: "))
    eficiencia = input("Ingrese la eficiencia (A, B, C, D, E o F): ")

    # Validaciones 
    if voltaje <= 0 or precio <= 0 or eficiencia.upper() not in listaEficiencia:
        print("Error: Datos ingresados no válidos para registrar una Consola.")
        return

    # Crear el objeto Consola y agregarlo a la lista
    consola = Consola(marca, nombre_consola, version, voltaje, precio, eficiencia)
    listaConsolas.append(consola)
    print("Consola registrada exitosamente.")

# Función para registrar una bicicleta y agregarla a la lista de bicicletas
def registrar_bicicleta():
    print("Registrando una nueva Bicicleta:")
    marca = input("Ingrese la marca: ")
    aro = float(input("Ingrese el aro: "))
    peso = float(input("Ingrese el peso en kg: "))
    precio = float(input("Ingrese el precio: "))

    # Validaciones 
    if aro < 0 or peso < 0 or precio < 0:
        print("Error: Datos ingresados no válidos para registrar una Bicicleta.")
        return

    # Crear el objeto Bicicleta y agregarlo a la lista
    bicicleta = Bicicleta(aro, peso, precio, marca)
    listaBicicletas.append(bicicleta)
    print("Bicicleta registrada exitosamente.")

def registrar_scooter():
    print("Registrando un nuevo Scooter:")
    marca = input("Ingrese la marca: ")
    voltaje = int(input("Ingrese el voltaje (en voltios): "))
    precio = float(input("Ingrese el precio: "))
    eficiencia = input("Ingrese la eficiencia (A, B, C, D, E o F): ")
    aro = float(input("Ingrese el aro: "))
    velocidad = int(input("Ingrese la velocidad (en km/h): "))
    peso = float(input("Ingrese el peso en kg: "))

    # Validaciones
    if voltaje <= 0 or precio <= 0 or aro <= 0 or velocidad <= 0 or peso <= 0 or eficiencia.upper() not in listaEficiencia:
        print("Error: Datos ingresados no válidos para registrar un Scooter.")
        return

    # Crear el objeto Scooter y agregarlo a la lista
    scooter = Scoter(marca, voltaje, precio, eficiencia, aro, velocidad, peso)
    listaScoters.append(scooter)
    print("Scooter registrado exitosamente.")    

# Función para cotizar los TVs y mostrar la información
def cotizar_tvs():
    print("Cotizando TVs:")
    for tv in listaTvs:
        print(tv.cotizar())

# Función para cotizar las consolas y mostrar la información
def cotizar_consolas():
    print("Cotizando Consolas:")
    for consola in listaConsolas:
        print(consola.cotizar())

# Función para cotizar los scooters y mostrar la información
def cotizar_scooters():
    for scooter in listaScoters:
        print(scooter.cotizar())

# Función para cotizar las bicicletas y mostrar la información
def cotizar_bicicletas():
    print("Cotizando Bicicletas:")
    for bicicleta in listaBicicletas:
        print(bicicleta.cotizar())

# Función para mostrar el menú de opciones
def menu():
    print("Menú:")
    print("1. Registrar TV")
    print("2. Registrar Consola")
    print("3. Registrar Bicicleta")
    print("4. Registrar Scoter")
    print("5. Cotizar TVs")
    print("6. Cotizar Consolas")
    print("7. Cotizar Scooters")
    print("8. Cotizar Bicicletas")
    print("9. Salir")

# Lista para almacenar los productos
listaTvs = []
listaConsolas = []
listaScoters = []
listaBicicletas = []

while True:
    menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        registrar_tv()
    elif opcion == 2:
        registrar_consola()
    elif opcion == 3:
        registrar_bicicleta()
    elif opcion == 4:
        registrar_scooter()    
    elif opcion == 5:
        cotizar_tvs()
    elif opcion == 6:
        cotizar_consolas()
    elif opcion == 7:
        cotizar_scooters()
    elif opcion == 8:
        cotizar_bicicletas()
    elif opcion == 9:
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

# Fin del programa
