import requests
from openpyxl import Workbook

def buscarguardar():
    nombre_pokemon = input("Ingresa el nombre o número del Pokémon: ")

    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"

    response = requests.get(url)

    if response.status_code == 200:
        datos = response.json()

        nombre = datos["name"]
        habilidades = [habilidad["ability"]["name"] for habilidad in datos["abilities"]]
        habilidadoc= ""
        tipos = [tipo["type"]["name"] for tipo in datos["types"]]
    
        for ability in datos["abilities"]:
            if ability["is_hidden"]:
                habilidadoc = ability["ability"]["name"]
                break
        
        print("Nombre:", nombre)
        print("Habilidades:", ", ".join(habilidades))
        print("Habilidad Oculta:", habilidadoc)
        print("Tipos:", ", ".join(tipos))
        
        libro_trabajo = Workbook()
        hoja = libro_trabajo.active

        
        hoja['A1'] = "Nombre"
        hoja['B1'] = "Habilidades"
        hoja['C1'] = "Habilidad Oculta"
        hoja['D1'] = "Tipos"
        
        hoja.append([nombre, ", ".join(habilidades), habilidadoc, ", ".join(tipos)])

        libro_trabajo.save(f"{nombre}.xlsx")
        print(f"La información de {nombre} se ha guardado en {nombre}.xlsx")
    else:
        print(f"No se encontró ningún Pokémon con el nombre o número '{nombre_pokemon}'.")

if __name__ == "__main__":
    buscarguardar()
