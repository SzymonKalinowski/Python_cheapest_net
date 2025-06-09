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
        if self.city_take not in self.data:
            raise ValueError(f"{self.city_take} doesn`t exist")
        if self.city_give not in self.data:
            raise ValueError(f"{self.city_give} doesn`t exist")
        for city in self.data:
            if


