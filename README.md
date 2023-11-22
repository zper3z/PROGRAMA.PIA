# graficas
programas con relacionados para la elaboracion de pia
mport matplotlib.pyplot as plt
import PRUEBA
import requests

def graficar(pokemon):
    info = PRUEBA.buscar(pokemon)

    # Gráfica de barras
    labels = ['HP', 'Ataque', 'Defensa', 'Ataque Especial', 'Defensa Especial', 'Velocidad']
    stats = [stat['base_stat'] for stat in PRUEBA.buscar_estadisticas(pokemon)]
    
    plt.bar(labels, stats, color=['red', 'blue', 'green', 'yellow', 'purple', 'orange'])
    plt.title(f'Estadísticas de {pokemon}')
    plt.xlabel('Estadísticas')
    plt.ylabel('Valor')
    plt.show()

    plt.pie(stats, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title(f'Estadísticas de {pokemon}')
    plt.show()

    if ciclo_si_no("Quieres comparar las estadísticas con otros Pokémon?"):
        comparar_estadisticas(pokemon)

def comparar_estadisticas(pokemon):
    comparar_pokemon = input("Ingresa el nombre o número del Pokémon para comparar: ")
    
    stats_pokemon = [stat['base_stat'] for stat in PRUEBA.buscar_estadisticas(pokemon)]
    stats_otro_pokemon = [stat['base_stat'] for stat in PRUEBA.buscar_estadisticas(comparar_pokemon)]

    labels = ['HP', 'Ataque', 'Defensa', 'Ataque Especial', 'Defensa Especial', 'Velocidad']

    plt.bar(labels, stats_pokemon, color='blue', label=pokemon)
    plt.bar(labels, stats_otro_pokemon, color='red', label=comparar_pokemon, alpha=0.5)
    plt.title(f'Comparación de Estadísticas entre {pokemon} y {comparar_pokemon}')
    plt.xlabel('Estadísticas')
    plt.ylabel('Valor')
    plt.legend()
    plt.show()

def ciclo_si_no(texto):
    opcion = input(f"{texto} (Si/No): ")
    if opcion.lower() == "si":
        return True
    elif opcion.lower() == "no":
        return False
    else:
        return ciclo_si_no(texto)
