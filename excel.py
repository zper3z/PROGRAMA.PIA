    import requests

    from openpyxl import Workbook

    def buscar_pokemon():
        nombre_pokemon = input("Ingresa el nombre o número del Pokémon: ")

        url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"

        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            name = data["name"]
            abilities = [ability["ability"]["name"] for ability in data["abilities"]]
            types = [t["type"]["name"] for t in data["types"]]

            workbook = Workbook()
            sheet = workbook.active

            sheet['A1'] = "Nombre"
            sheet['B1'] = "Habilidades"
            sheet['C1'] = "Tipos"
            sheet.append([name, ", ".join(abilities), ", ".join(types)])

            workbook.save(f"{name}.xlsx")
            print(f"La información de {name} se ha guardado en {name}.xlsx")
        else:
            print(f"No se encontró ningún Pokémon con el nombre o número '{nombre_pokemon}'.")

    if __name__ == "__main__":
        buscar_pokemon()