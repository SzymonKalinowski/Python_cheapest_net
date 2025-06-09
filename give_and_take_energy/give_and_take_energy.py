from dataclasses import dataclass

@dataclass
class GiveAndTakeEnergy:
    data: list
    city_take: str
    city_give: str
    how_much: float

    def GiveAndTakeEnergy(self):
        if self.city_take == self.city_give:
            raise ValueError("Cities cannot be the same")

        found_take = found_give = False
        for i, (city, energy) in enumerate(self.data):
            if city == self.city_take:
                self.data[i] = (city, energy - self.how_much)
                found_take = True
            if city == self.city_give:
                self.data[i] = (city, energy + self.how_much)
                found_give = True

        if not found_take:
            raise ValueError(f"{self.city_take} doesn't exist")
        if not found_give:
            raise ValueError(f"{self.city_give} doesn't exist")

        return self.data
