import requests
from openpyxl import Workbook
import PRUEBA

def menu_principal():
    print("--- MENU POKEMON---") ####FRANCO PELAME
    print("1. CONSULTAR POKEMON")
    print("2. FAVORITOS")
    print("3. LISTAS")
    print("4. Salir")
    opcion = PRUEBA.validador_opciones(4)
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
    
    if PRUEBA.ciclo_si_no("¿Quisieras graficar las estadísticas de este Pokémon?"):
        PLACEHOLDER_funcion_grafica_individual(pokemon)
    
    while True:
        respuesta = PRUEBA.ciclo_si_no("¿Quisieras volver al menú principal?")
        if respuesta:
            menu_principal()
            break
        else:
            print("Oh, perdón... esperaré un rato más")


def opcion_2():
    menu_lista("Favoritos") 
#hasta aqui esta bien

def opcion_3():
    print("---LISTAS---") #CHECA TODO LO QUE TIENE print
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
    print(f"{contador+2} GRAFICAR")
    print(f"{contador+3} REGRESAR")
    opcion = PRUEBA.validador_opciones(contador+3)
    if opcion >= contador:
        if opcion == contador:agregar_lista()
        if opcion == contador+1:eliminar_lista()
        if opcion == contador+2:menu_grafica()
        if opcion == contador+3:menu_principal()
    else:
        menu_lista(nombres_listas[1][opcion-1])

def agregar_lista():
    nombre = input("Ingrese el nombre de la nueva lista: ")#ACA TAMBIENN FRANCO
    database.update({nombre:[]})
    opcion_3()

def eliminar_lista(): 
    contador = 1
    nombres_listas = [[],[]]
    for nombre in database.keys():
        if nombre == "Favoritos":continue
        nombres_listas[0].append(contador)
        nombres_listas[1].append(nombre)
        print(f"{contador}.- {nombre}")#TAL VEZ ACA FRANCO
        contador += 1
    opcion = PRUEBA.validador_opciones(contador)
    del database[nombres_listas][1][opcion-1]
    opcion_3()

def opcion_4():
    if PRUEBA.ciclo_si_no("Estas seguro?"):
        return 0
    else:
        menu_principal()

def menu_lista(nombre_lista):
    print(f"---{nombre_lista}---")
    print(f"1. MODIFICAR LISTA") #(abre un sub menu con opciones de agregar pokemon y eliminar pokemon, falta la opcion de crear lista nueva)
    print(f"2. VER POKEMONS")  # agregar mensaje si la lista está vacía (solucionado)
    print(f"3. CREAR EXCEL DE INFORMACION")
    print(f"4. VOLVER")
    opcion = PRUEBA.validador_opciones(4)
    if opcion == 1:
        modificar_lista(nombre_lista)
    elif opcion == 2:
        ver_lista(nombre_lista)
    elif opcion == 3:
        PRUEBA.excel(database[nombre_lista], nombre_lista)
    elif opcion == 4:
        menu_principal()

def modificar_lista(nombre_lista):
    print("---MODIFICAR LISTA---")
    print("1. AGREGAR POKEMON")
    print("2. ELIMINAR POKEMON")
    print("3. VOLVER")
    opcion = PRUEBA.validador_opciones(3)
    if opcion == 1:
        agregar_pokemon(nombre_lista)
    elif opcion == 2:
        eliminar_pokemon(nombre_lista)
    elif opcion == 3:
        menu_lista(nombre_lista)

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

def ver_lista(nombre_lista, salir=True):
    print(f"--Viendo pokemons de {nombre_lista}:")
    
    if not database[nombre_lista]:
        print("Ups, parece que aún no has capturado ningún Pokémon.")
    else:
        for i in database[nombre_lista]:
            print(f">{i}")
    
    if salir:
        menu_lista(nombre_lista)


def menu_grafica():
    print(f"1. GRAFICA MEJORES ESTADISTICAS")#ACA TAMBIEN FRANCO
    print(f"2. GRAFICA DE TIPOS")
    opcion = PRUEBA.validador_opciones(2)
    if opcion == 1:
        pokemon = PRUEBA.buscar(input("Ingresa el nombre o número del Pokémon: "))
        nombre = pokemon[0]
        PLACEHOLDER_funcion_grafica2_estadisticas(nombre)
    if opcion == 2:
        pokemon = PRUEBA.buscar(input("Ingresa el nombre o número del Pokémon: "))
        nombre = pokemon[0]
        PLACEHOLDER_funcion_grafica3_tipos(nombre)


database = {"Favoritos":[], "lista1": [] } #base de datos predeterminada

if __name__ == "__main__":
    menu_principal()
