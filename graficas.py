import requests
import matplotlib.pyplot as plt

def obtener_datos_pokemon(nombre_pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}'
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos_pokemon = respuesta.json()
        return datos_pokemon
    else:
        print(f"No se pudo obtener la información del Pokémon {nombre_pokemon}")
        return None

def graficar_barras(nombre_pokemon, caracteristicas):
    plt.bar(caracteristicas.keys(), caracteristicas.values())
    plt.title(f'Características de {nombre_pokemon}')
    plt.xlabel('Característica')
    plt.ylabel('Valor')
    plt.show()

def graficar_pastel(nombre_pokemon, caracteristicas):
    plt.pie(caracteristicas.values(), labels=caracteristicas.keys(), autopct='%1.1f%%')
    plt.title(f'Distribución de Características de {nombre_pokemon}')
    plt.show()

def graficar_lineal(nombre_pokemon, estadisticas):
    plt.plot(estadisticas.keys(), estadisticas.values(), marker='o')
    plt.title(f'Estadísticas de {nombre_pokemon}')
    plt.xlabel('Estadística')
    plt.ylabel('Valor')
    plt.show()

def graficar_estadisticas_pokemon(nombre_pokemon):
    datos_pokemon = obtener_datos_pokemon(nombre_pokemon)

    if datos_pokemon:
        caracteristicas = {
            'HP': datos_pokemon['stats'][0]['base_stat'],
            'Ataque': datos_pokemon['stats'][1]['base_stat'],
            'Defensa': datos_pokemon['stats'][2]['base_stat'],
            'Velocidad': datos_pokemon['stats'][5]['base_stat']
        }

        graficar_barras(nombre_pokemon, caracteristicas)
        graficar_pastel(nombre_pokemon, caracteristicas)

        estadisticas = {
            'Ataque': datos_pokemon['stats'][1]['base_stat'],
            'Defensa': datos_pokemon['stats'][2]['base_stat'],
            'Velocidad': datos_pokemon['stats'][5]['base_stat']
        }

        graficar_lineal(nombre_pokemon, estadisticas)

if __name__ == "__main__":
    nombres_pokemon = input("Ingrese los nombres de los Pokémon separados por comas: ")
    nombres_pokemon = nombres_pokemon.split(',')

    for nombre_pokemon in nombres_pokemon:
        nombre_pokemon = nombre_pokemon.strip()
        graficar_estadisticas_pokemon(nombre_pokemon)
