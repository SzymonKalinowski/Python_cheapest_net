from parse_data.parse_distance_file import *
from parse_data.parse_electricity_production_file import *
from calculate.calculate_all_possible_tracks import *
from calculate.calculate_energy_demand import *
from dijkastra_algorythm.algorythm import *
from energy_flow.energy_flow import *


def main_logic():
    # 1. Wczytanie danych
    distance = Distance("distances.txt")
    distance.open_file()
    distance_data = distance.export_data()

    electricityProduction = ElectricityProduction("electricity_production.txt")
    electricityProduction.open_file()
    production_data = electricityProduction.export_data()

    # 2. Obliczenie zapotrzebowania i podział miast
    calculator = EnergyDemandCalculator(production_data)
    demand = calculator.calculate_energy_demand()
    cities_with, cities_without = calculator.cities_with_or_without_energy_plants()

    # 3. Zbudowanie grafu
    possible = AllPossibleTracks(distance_data)
    graph = possible.convert_into_graph()
    cities = possible.find_unique_cities()

    # 4. Zastosowanie Kruskala do znalezienia MST
    edges = graph_to_edges(graph)
    kruskal = Kruskal(cities, edges)
    mst = kruskal.kruskal()

    # 5. Wyznaczenie przepływów energii w MST
    power_flow = assign_power_flow(mst, cities_with, cities_without)

    # 6. Obliczenie całkowitego kosztu
    total_cost = calculate_total_cost(mst, power_flow)

    # 7. Wyniki
    print("Required connections:")
    for edge in mst:
        print(edge)
    print("\nEnergy flow:")
    for edge, amount in power_flow.items():
        print(f"{edge}: {amount}")
    print(f"\nCost: {total_cost}")

if __name__ == "__main__":
    main_logic()
