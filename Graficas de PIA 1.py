import requests
import matplotlib.pyplot as plt
import statistics

def buscar_pokemon():
    nombre_pokemon = input("Ingresa el nombre o número del pokemon: ")

    url = f"https://pokeapi.co/api/v2/pokemon/{nombre_pokemon}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        name = data["name"]
        stats = data["stats"]

        stat_names = [stat["stat"]["name"] for stat in stats]
        base_stats = [stat["base_stat"] for stat in stats]
        media = statistics.mean(base_stats)
        print("promedio de pokemon", media)
        plt.bar(stat_names, base_stats, color = "blue")
        plt.title(f"Estadísticas Base de {name}")
        plt.xlabel("Estadísticas")
        plt.ylabel("Valor Base")
        plt.show()
    else:
        print(f"No se encontró ningún Pokémon con el nombre o número '{nombre_pokemon}'.")

if __name__ == "__main__":
    buscar_pokemon()
