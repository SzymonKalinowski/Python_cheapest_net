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

        city_take_exists = False
        for city, energy in self.data:
            if city == self.city_take:
                city_take_exists = True
                break
        if not city_take_exists:
            raise ValueError(f"{self.city_take} doesn't exist")

        city_give_exists = False
        for city, energy in self.data:
            if city == self.city_give:
                city_give_exists = True
                break
        if not city_give_exists:
            raise ValueError(f"{self.city_give} doesn't exist")

        for city, energy in self.data:
            if city == self.city_take:
                energy -= self.how_much

        for city, energy in self.data:
            if city == self.city_give:
                energy += self.how_much
