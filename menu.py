import requests
from openpyxl import Workbook
import PRUEBA

def menu_principal():
    print("--- MENU POKEMON---")
    print("1. CONSULTAR POKEMON")
    print("2. FAVORITOS")
    print("3. LISTAS")
    print("4. Salir")
    opcion = validador_opciones(4)
    if opcion == 1:
        opcion_1()
    elif opcion == 2:
        opcion_2()
    elif opcion == 3:
        opcion_3()
    elif opcion == 4:
        opcion_4()

def opcion_1():
    pokemon = input("Ingresa el nombre o número del Pokémon: ")
    PRUEBA.imprimir(PRUEBA.buscar(pokemon))
    if ciclo_si_no("Quisieras graficar las estadisticas de este pokemon?"):
        graficar(pokemon) ####################################################### falta esta funcion
    while not(ciclo_si_no("Quisieras volver al menu principal?")):
        print("Oh perdon..esperaré un rato más")
    menu_principal()

def opcion_2():
    menu_lista("Favoritos") 

def opcion_3():
    print("---LISTAS---")
    contador = 1
    nombres_listas = [[],[]]
    for nombre in database.keys():
        if nombre == "Favoritos":continue
        nombres_listas[0].append(contador)
        nombres_listas[1].append(nombre)
        print(f"{contador}.- {nombre}")
        contador += 1
    print(f"{contador} AGREGAR LISTA")
    print(f"{contador+1} ELIMINAR LISTA")
    print(f"{contador+2} REGRESAR")
    opcion = validador_opciones(contador+2)
    if opcion >= contador:
        if opcion == contador+2:menu_principal()
        if opcion == contador+1:eliminar_lista()
        if opcion == contador:agregar_lista()
    else:
        menu_lista(nombres_listas[1][opcion-1])

def agregar_lista():
    nombre = input("Ingrese el nombre de la nueva lista: ")
    database.update({nombre:[]})
    opcion_3()

def eliminar_lista(): 
    contador = 1
    print(f"contador: {contador}")
    nombres_listas = [[],[]]
    for nombre in database.keys():
        if nombre == "Favoritos":continue
        nombres_listas[0].append(contador)
        nombres_listas[1].append(nombre)
        print(f"{contador}.- {nombre}")
        contador += 1
    opcion = validador_opciones(contador)
    del database[nombres_listas][1][opcion-1]
    opcion_3()

def opcion_4():
    if ciclo_si_no("Estas seguro?"):
        return 0
    else:
        menu_principal()

def menu_lista(nombre_lista):
    print(f"---{nombre_lista}---")
    print(f"1. AGREGAR POKEMON")
    print(f"2. VER POKEMONS")
    print(f"3. ELIMINAR POKEMON")
    print(f"4. CREAR EXCEL DE INFORMACION")
    print(f"5. VOLVER")
    opcion = validador_opciones(5)
    if opcion == 1:
        agregar_pokemon(nombre_lista)
    elif opcion == 2:
        ver_lista(nombre_lista)
    elif opcion == 3:
        eliminar_pokemon(nombre_lista)
    elif opcion == 4:
        PRUEBA.excel(database[nombre_lista],nombre_lista)
    elif opcion == 5:
        menu_principal()


def agregar_pokemon(nombre_lista):
    nombre_lista[0]
    pokemon = PRUEBA.buscar(input("Ingresa el nombre o número del Pokémon: "))
    nombre = pokemon[0]
    database[nombre_lista].append(nombre)
    menu_lista(nombre_lista)


def eliminar_pokemon(nombre_lista):
    ver_lista(nombre_lista, False)
    pokemon = PRUEBA.buscar(input("Ingresa el nombre o número del Pokémon: "))
    nombre = pokemon[0]
    database[nombre_lista].remove(nombre)
    menu_lista(nombre_lista)

def ver_lista(nombre_lista, salir = True):
    print(f"--Viendo pokemons de {nombre_lista}:")
    for i in database[nombre_lista]:
        print(f">{i}")
    if salir:menu_lista(nombre_lista)

def ciclo_si_no(texto):
    opcion = input(f"{texto} (Si/No): ")
    if opcion == "Si":
        return True
    elif opcion == "No":
        return False
    else:
        return ciclo_si_no(texto)
    
def validador_opciones(opcion_final):
    opcion_final = int(opcion_final)
    opcion = input(f"Selecciona su opción (1-{opcion_final}): ")
    for num in range(1,opcion_final+1,1):
        if opcion == str(num):break
    else:
        print(f"Opción inválida")
        return validador_opciones(opcion_final)
    return int(opcion)

database = {"Favoritos":[], "lista1": [] } #base de datos predeterminada

if __name__ == "__main__":
    menu_principal()

