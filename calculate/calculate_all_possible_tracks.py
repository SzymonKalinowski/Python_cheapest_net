from dataclasses import dataclass, field

@dataclass
class AllPossibleTracks:
    data: list
    key: str = None
    connected_cities: set = field(default_factory=set)
    unique_cities: set = field(default_factory=set)
    city_connections: dict = field(default_factory=dict)

    def find_unique_cities(self):
        for distance in self.data:
            self.unique_cities.add(distance[0])
            self.unique_cities.add(distance[1])
        self.unique_cities = sorted(list(self.unique_cities))
        return self.unique_cities


    def all_city_conections(self):
        for city in self.unique_cities:
            self.key = city
            for d in self.data:
                if d[0] in city:
                    self.connected_cities.add(d[1])

                if d[1] in city:
                    self.connected_cities.add(d[0])

        self.connected_cities = sorted(list(self.connected_cities))
        self.city_connections[self.key] = self.connected_cities

        return self.city_connections


