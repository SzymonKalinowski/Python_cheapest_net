from parse_data.parse_distance_file import Distance
from parse_data.parse_electricity_production_file import ElectricityProduction



if __name__ == "__main__":
    a=Distance("distances.txt").open_file()
    b=ElectricityProduction("electricity_production.txt").open_file()