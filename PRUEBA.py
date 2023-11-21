import requests
from openpyxl import Workbook
	
def buscar(nombre_pokemon):
	
  if nombre_pokemon != "":
		
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"
    response = requests.get(url)
    informacion = []
		
    if response.status_code == 200 :
			
      datos = response.json()
      nombre = datos["name"]
      habilidades = []
      habilidad_oc= ""
      tipos = [tipo["type"]["name"] for tipo in datos["types"]]
      for habilidad in datos["abilities"]: 
				
        if habilidad["is_hidden"]:
          habilidad_oc = habilidad["ability"]["name"]
        else:
          habilidades.append(habilidad["ability"]["name"])
      
      if habilidad_oc == "": habilidad_oc = "No tiene"
      informacion = [nombre, [], [], habilidad_oc]
      informacion[1].extend(tipos)
      informacion[2].extend(habilidades)
        

      return informacion


    else:
      print(f"No se encontró ningún Pokémon con el nombre o número '{nombre_pokemon}'.")
      nombre = input("Ingresa el nombre o número del Pokémon: ")
      return buscar(nombre)

  else:
    print(f"Favor de ingresar los datos pedidos")
    nombre = input("Ingresa el nombre o número del Pokémon: ")
    return buscar(nombre)


def imprimir(info):
	nombre = info[0]
	tipos = info[1]
	habilidades = info[2]
	habilidad_oc = info[3]
	print(f"Nombre: {nombre}")
	print("Tipos:", ", ".join(tipos))
	print("Habilidades:", ", ".join(habilidades))
	print("Habilidad Oculta:", habilidad_oc)


def excel(info):
	nombre = info[0]
	tipos = info[1]
	habilidades = info[2]
	habilidad_oc = info[3]
	
	libro_trabajo = Workbook()
	hoja = libro_trabajo.active
	
	hoja['A1'] = "Nombre"
	hoja['B1'] = "Tipos"
	hoja['C1'] = "Habilidades"
	hoja['D1'] = "Habilidad Oculta"
	
	hoja.append([nombre, ", ".join(tipos), ", ".join(habilidades),habilidad_oc])

	libro_trabajo.save(f"{nombre}.xlsx")
	libro_trabajo.close()
	print(f"La información de {nombre} se ha guardado en {nombre}.xlsx")

pokemon = input("Ingresa el nombre o número del Pokémon: ")
inf = buscar(pokemon)
imprimir(inf)
excel(inf)

