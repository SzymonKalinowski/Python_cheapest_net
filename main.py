from parse_data.parse_distance_file import Distance
from parse_data.parse_electricity_production_file import ElectricityProduction
from calculate.calculate_energy_demand import EnergyDemandCalculator
from calculate.calculate_all_possible_tracks import AllPossibleTracks

distance = Distance(r"C:\Python_cheapest_net\distances.txt")
distance.open_file()
print(distance.export_data())
print("\n")

electricityProduction = ElectricityProduction(r"C:\Python_cheapest_net\electricity_production.txt")
electricityProduction.open_file()

calculator = EnergyDemandCalculator(electricityProduction.export_data())
demand = calculator.calculate_energy_demand()
cities = calculator.cities_with_or_without_energy_plants()
print(demand, cities)
print("\n")

possibleCities = AllPossibleTracks(distance.export_data())
connected = possibleCities.all_city_conections()
graph = possibleCities.convert_into_graph()
print(graph)
print("\n")