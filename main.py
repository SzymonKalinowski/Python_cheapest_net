from parse_data.parse_distance_file import Distance
from parse_data.parse_electricity_production_file import ElectricityProduction
from calculate.calculate_energy_demand import EnergyDemandCalculator
from calculate.calculate_all_possible_tracks import AllPossibleTracks

distance = Distance(r"C:\Python_cheapest_net\distances.txt")
distance.open_file()
# print(distance.export_data())

electricityProduction = ElectricityProduction(r"C:\Python_cheapest_net\electricity_production.txt")
electricityProduction.open_file()

calculator = EnergyDemandCalculator(electricityProduction.export_data())
demand = calculator.calculate_energy_demand()
cities = calculator.cities_with_or_without_energy_plants()
# print(demand, cities)

possibleCities = AllPossibleTracks(distance.export_data())
possibleCities.find_unique_cities()
connected = possibleCities.all_city_conections()
print(connected)