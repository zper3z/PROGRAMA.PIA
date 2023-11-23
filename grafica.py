import requests
import matplotlib.pyplot as plt

def obtener_datos_pokemon(nombre_pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{nombre_pokemon.lower()}'
    respuesta = requests.get(url)

    if respuesta.status_code == 200:
        datos_pokemon = respuesta.json()
        if datos_pokemon:
            caracteristicas = {
                'HP': datos_pokemon['stats'][0]['base_stat'],
                'Ataque': datos_pokemon['stats'][1]['base_stat'],
                'Defensa': datos_pokemon['stats'][2]['base_stat'],
                'Ataque Especial': datos_pokemon['stats'][3]['base_stat'],
                'Defensa Especial': datos_pokemon['stats'][4]['base_stat'],
                'Velocidad': datos_pokemon['stats'][5]['base_stat']
            }
        return caracteristicas
    else:
        print(f"No se pudo obtener la información del Pokémon {nombre_pokemon}")
        return None

def graficar_barras(nombre_pokemon, caracteristicas):
    colores = ['blue'] * len(caracteristicas.items())
    stat_maximo = max(caracteristicas.values())
    if stat_maximo == caracteristicas['HP']:colores[0]='red'
    if stat_maximo == caracteristicas['Ataque']:colores[1]='red'
    if stat_maximo == caracteristicas['Defensa']:colores[2]='red'
    if stat_maximo == caracteristicas['Ataque Especial']:colores[3]='red'
    if stat_maximo == caracteristicas['Defensa Especial']:colores[4]='red'
    if stat_maximo == caracteristicas['Velocidad']:colores[5]='red'
    plt.bar(caracteristicas.keys(), caracteristicas.values(), color = colores)
    plt.title(f'Características de {nombre_pokemon}')
    plt.xlabel('Característica')
    plt.ylabel('Valor base')
    plt.show()

def graficar_pastel(nombre_pokemon, caracteristicas):
    plt.pie(caracteristicas.values(), labels=caracteristicas.keys(), autopct='%1.1f%%')
    plt.title(f'Distribución de Características de {nombre_pokemon}')
    plt.show()

def graficar_lineal(nombre_pokemon, estadisticas):
    promedio = ( sum(estadisticas.values()) ) / len(estadisticas.values())
    plt.plot(estadisticas.keys(), estadisticas.values(), marker='o')
    plt.title(f'Estadísticas de {nombre_pokemon}')
    plt.suptitle(f'Promedio de estadisticas pokemon: {promedio}')
    plt.xlabel('Estadística')
    plt.ylabel('Valor')
    plt.show()

def graficar_estadisticas_pokemon(nombre_pokemon,caracteristicas):

    graficar_barras(nombre_pokemon, caracteristicas)
    graficar_pastel(nombre_pokemon, caracteristicas)
    graficar_lineal(nombre_pokemon, caracteristicas)
