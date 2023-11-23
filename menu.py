import requests
from openpyxl import Workbook
import funciones
import grafica

def menu_principal():
    print("--- MENU POKEMON---") 
    print("1. CONSULTAR POKEMON")
    print("2. FAVORITOS")
    print("3. LISTAS")
    print("4. Salir")
    opcion = funciones.validador_opciones(4)
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
    funciones.imprimir(funciones.buscar(pokemon))

    if funciones.ciclo_si_no("¿Quisieras graficar las estadísticas de este Pokémon?"):
        menu_grafica(pokemon[0])
    
    while True:
        respuesta = funciones.ciclo_si_no("¿Quisieras volver al menú principal?")
        if respuesta:
            menu_principal()
            break
        else:
            print("Oh, perdón... esperaré un rato más")

def opcion_2():
    menu_lista("Favoritos") 

def opcion_3(): 
    print("---LISTAS---")
    contador = 1
    print(f"{contador} ESCOGER LISTA")
    print(f"{contador + 1} AGREGAR LISTA")
    print(f"{contador + 2} ELIMINAR LISTAS")
    print(f"{contador + 3} REGRESAR")

    opcion = funciones.validador_opciones(contador + 3)
    if opcion == contador:
        mostrar_listas()
    elif opcion == contador + 1:
        agregar_lista()
    elif opcion == contador + 2:
        eliminar_lista()
    elif opcion == contador + 3:
        menu_principal()

def mostrar_listas():
    contador = 0
    nombres_listas = [[],[]]
    for nombre in database.keys():
        if nombre == "Favoritos":
            continue
        contador += 1
        nombres_listas[0].append(contador)
        nombres_listas[1].append(nombre)
        print(f"{contador}.- {nombre}")
    if(len(nombres_listas[1])) != 0:   
        opcion = funciones.validador_opciones(contador)
        menu_lista(nombres_listas[1][opcion-1])
    else:
        print(f"No hay lista que escoger")
        opcion_3()

def agregar_lista():
    nombre = input("Ingrese el nombre de la nueva lista: ")
    database.update({nombre:[]})
    opcion_3()

def eliminar_lista(): 
    contador = 0
    nombres_listas = [[],[]]
    for nombre in database.keys():
        if nombre == "Favoritos":
            continue
        contador += 1
        nombres_listas[0].append(contador)
        nombres_listas[1].append(nombre)
        print(f"{contador}.- {nombre}")
    if(len(nombres_listas[1])) != 0:
        opcion = funciones.validador_opciones(contador)
        del database[nombres_listas[1][opcion-1]]
        opcion_3()
    else:
        print(f"No hay lista que borrar")
        opcion_3()

def opcion_4():
    if funciones.ciclo_si_no("Estas seguro?"):
        return 0
    else:
        menu_principal()

def menu_lista(nombre_lista):
    print(f"---{nombre_lista}---")
    print(f"1. EDITAR LISTA") 
    print(f"2. VER POKEMONS")  
    print(f"3. CREAR/ACTUALIZAR EXCEL")
    print(f"4. VOLVER")
    opcion = funciones.validador_opciones(4)
    if opcion == 1:
        modificar_lista(nombre_lista)
    elif opcion == 2:
        ver_lista(nombre_lista)
    elif opcion == 3:
        funciones.excel(database[nombre_lista], nombre_lista)
        menu_lista(nombre_lista)
    elif opcion == 4:
        menu_principal()

def modificar_lista(nombre_lista):
    print(f"---MODIFICAR LISTA {nombre_lista}---")
    print("1. AGREGAR POKEMON")
    print("2. ELIMINAR POKEMON")
    print("3. VOLVER")
    opcion = funciones.validador_opciones(3)
    if opcion == 1:
        agregar_pokemon(nombre_lista)
    elif opcion == 2:
        eliminar_pokemon(nombre_lista)
    elif opcion == 3:
        menu_lista(nombre_lista)

def agregar_pokemon(nombre_lista):
    pokemon = funciones.buscar(input("Ingresa el nombre o número del Pokémon: "))
    nombre = pokemon[0]
    database[nombre_lista].append(nombre)
    menu_lista(nombre_lista)

def eliminar_pokemon(nombre_lista):
    if not database[nombre_lista]:
        contador = 0
        nombres_listas = [[],[]]
        for pokemon in database[nombre_lista]:
            contador += 1
            nombres_listas[0].append(contador)
            nombres_listas[1].append(pokemon)
            print(f"{contador}.- {pokemon}")
            
        opcion = funciones.validador_opciones(contador)
        del database[nombre_lista][opcion-1]
        modificar_lista(nombre_lista)
    else:
        print("Ups, parece que aún no has capturado ningún Pokémon.")
    modificar_lista(nombre_lista)

def ver_lista(nombre_lista):
    print(f"--Viendo pokemons de {nombre_lista}:")
    
    if not database[nombre_lista]:
        print("Ups, parece que aún no has capturado ningún Pokémon.")
    else:
        for i in database[nombre_lista]:
            print(f">{i}")
    menu_lista(nombre_lista)

def menu_grafica(pokemon):
    print(f"1. GRAFICA DE BARRAS (CON MAYOR ESTADISTICA)")
    print(f"2. GRAFICA DE PASTEL (CON PORCENTAJES)")
    print(f"3. GRAFICA LINEAL (CON PROMEDIO)")
    print(f"4. CONTINUAR")
    opcion = funciones.validador_opciones(4)
    if opcion == 1:
        grafica.graficar_barras(pokemon,grafica.obtener_datos_pokemon(pokemon))
    if opcion == 2:
        grafica.graficar_pastel(pokemon,grafica.obtener_datos_pokemon(pokemon))
    if opcion == 3:
        grafica.graficar_lineal(pokemon,grafica.obtener_datos_pokemon(pokemon))
    if opcion != 4:menu_grafica(pokemon)
        
def actualizar_database():
    global database
    listas = funciones.importar_listas()
    database = {}
    for nombre, ruta in listas.items():
        info = funciones.consultar_lista(ruta)
        database[nombre] = []
        for pokemon in info:
            pokemon = pokemon[0]
            database[nombre].append(pokemon)
    del database[nombre][0]


database = {} 

if __name__ == "__main__":
    funciones.crear_carpetaListas()
    actualizar_database()
    menu_principal()
