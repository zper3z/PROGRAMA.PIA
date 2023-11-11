import requests
import matplotlib.pyplot as plt

def buscar_pokemon():
    nombre_pokemon = input("Ingresa el nombre o número del Pokémon: ")

    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        stats = data["stats"]

        stat_names = [stat["stat"]["name"] for stat in stats]
        base_stats = [stat["base_stat"] for stat in stats]

        # Crear un gráfico de barras
        plt.bar(stat_names, base_stats)
        plt.title(f"Estadísticas Base de {name}")
        plt.xlabel("Estadísticas")
        plt.ylabel("Valor Base")
        plt.show()
    else:
        print(f"No se encontró ningún Pokémon con el nombre o número '{nombre_pokemon}'.")

if __name__ == "__main__":
    buscar_pokemon()
