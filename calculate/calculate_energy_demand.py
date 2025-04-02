from dataclasses import dataclass
from main import electricityProduction

@dataclass()
class EnergyDemandCalculator:
    data = electricityProduction.export_data()
    electricity_demand: float = 0
    cities_with: list = None
    cities_without: list = None

    def calculate_energy_demand(self):
        for d in self.data:
            self.electricity_demand += d[1]

        if self.electricity_demand < 0:
            raise ValueError("Energy demand cannot be negative")
        else:
            return self.electricity_demand

    def cities_with_or_without_energy_plants(self):
        self.cities_with = []
        self.cities_without = []
        for d in self.data:
            if d[1] > 0:
                self.cities_with.append(d)
            else:
                self.cities_without.append(d)

        sorted_with = sorted(self.cities_with, key=lambda x: x[1])
        sorted_without = sorted(self.cities_without, key=lambda x: x[1])

        return sorted_with, sorted_without

calculator = print(EnergyDemandCalculator().cities_with_or_without_energy_plants())


