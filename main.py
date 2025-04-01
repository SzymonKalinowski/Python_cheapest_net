from parse_data.parse_distance_file import Distance
from parse_data.parse_electricity_production_file import ElectricityProduction

distance = Distance(r"C:\Python_cheapest_net\distances.txt").open_file()
electricityProduction = ElectricityProduction(r"C:\Python_cheapest_net\electricity_production.txt").open_file()