from dataclasses import dataclass, field

@dataclass
class AllPossibleTracks:
    data: list
    key: str = None
    connected_cities: set = field(default_factory=set)
    unique_cities: set = field(default_factory=set)
    city_connections: dict = field(default_factory=dict)

    def find_unique_cities(self):
        unique = set()
        for distance in self.data:
            unique.add(distance[0])
            unique.add(distance[1])
        self.unique_cities = sorted(list(unique))
        return self.unique_cities


    def all_city_conections(self):
        self.find_unique_cities()
        city_connections = {}
        for city in self.unique_cities:
            connected = set()
            for d in self.data:
                if d[0] == city:
                    connected.add(d[1])
                if d[1] == city:
                    connected.add(d[0])
            city_connections[city] = sorted(list(connected))
        return city_connections