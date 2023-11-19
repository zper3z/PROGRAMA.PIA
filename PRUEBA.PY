import requests

def buscar_pokemon():
    nombre = input("Ingresa el nombre o número del Pokémon: ")

    url = f"https://pokeapi.co/api/v2/pokemon/{nombre}"

    response = requests.get(url)

    if response.status_code == 200:
        datos = response.json()

        nombre = datos["name"]
        habilidad=[]
        habilidad_oc=[]
        for habilidades in datos["abilities"]: 
            if habilidades["is_hidden"] == True:
                habilidad_oc.append(habilidades["ability"]["name"])
            else:
                habilidad.append(habilidades["ability"]["name"])
        types = [t["type"]["name"] for t in datos["types"]]

        print("Nombre:", nombre)
        print("Habilidades:", ", ".join(habilidad))
        print("Habilidades ocultas:", ", ".join(habilidad_oc))
        print("Tipos:", ", ".join(types))
    else:
        print(f"No se encontró ningún Pokémon con el nombre o número '{nombre_pokemon}'.")

if __name__ == "__main__":
    buscar_pokemon()


