import requests
from openpyxl import Workbook

def buscarguardar(nombre_pokemon):
    
    if nombre_pokemon != "":

      url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
      response = requests.get(url)

      if response.status_code == 200 :
          datos = response.json()

          nombre = datos["name"]
          habilidades = []
          habilidadoc= []
          tipos = [tipo["type"]["name"] for tipo in datos["types"]]
      
          for habilidad in datos["abilities"]:
              if habilidad["is_hidden"]:
                  habilidadoc.append(habilidad["ability"]["name"])
              else:
                  habilidades.append(habilidad["ability"]["name"])
                  
          
          print(f"Nombre: {nombre}")
          print("Habilidades:", ", ".join(habilidades))
          print("Habilidad Oculta:", ",".join(habilidadoc))
          print("Tipos:", ", ".join(tipos))
          
          libro_trabajo = Workbook()
          hoja = libro_trabajo.active

          
          hoja['A1'] = "Nombre"
          hoja['B1'] = "Habilidades"
          hoja['C1'] = "Habilidad Oculta"
          hoja['D1'] = "Tipos"
          
          hoja.append([nombre, ", ".join(habilidades), ",".join(habilidadoc), ", ".join(tipos)])

          libro_trabajo.save(f"{nombre}.xlsx")
          print(f"La información de {nombre} se ha guardado en {nombre}.xlsx")
      else:
          print(f"No se encontró ningún Pokémon con el nombre o número '{nombre_pokemon}'.")
          nombre = input("Ingresa el nombre o número del Pokémon: ")
          buscarguardar(nombre)

    else:
        print(f"Favor de ingresar los datos pedidos")
        nombre = input("Ingresa el nombre o número del Pokémon: ")
        buscarguardar(nombre)

pokemon = input("Ingresa el nombre o número del Pokémon: ")
buscarguardar(pokemon)

