def mostrar_menu():
  print("--- MENU POKEMON---")
  print("1. FAVORITOS")
  print("2. LISTAS")
  print("3. GRAFICA")
  print("4. Salir")
  opcion = input("Selecciona su opción (1-4): ")
  if opcion == "1":
    opcion_1()
  elif opcion == "2":
    opcion_2()
  elif opcion == "3":
    opcion_3()
  elif opcion == "4":
    return 0
  else:
    print("Opción inválida")
    mostrar_menu()

def opcion_1():
  print("---POKEMONES FAVORITOS---")
  print("1. AGREGAR POKEMON")
  print("2. ELIMINAR POKEMON")
  print("3. VOLVER")

def opcion_2():
  print("---LISTAS---")
  contador = 1
  for i in len(database["listas"]:
    nombre = str(database["listas][i])
    print(f"{n}---{nombre}---")
    n += 1
  print(f"{n}REGRESAR")

def opcion_3():
  poke = input("Ingrese un pokemon para ver la grafica de las estaditiscas del pokemon base")
  
def opcion_4():
  return 0
  
def lista_pokemon(pokemon, agregar = True):
  if agregar:
    database["fav"].append(pokemon)
  else:
    database["fav"].remove(pokemon)
  


database = {"fav":[], "listas": [] }





mostrar_menu()
