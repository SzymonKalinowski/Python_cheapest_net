from dataclasses import dataclass, field

@dataclass
class Dijkstra:
    graph: dict
    start: str
    end: str = None
    distances: dict = field(init=False, default_factory=dict)
    previous_nodes: dict = field(init=False, default_factory=dict)

    def dijkstra_algorithm(self):
        if self.start not in self.graph:
            raise ValueError("Start node is not in the graph")

        self.distances = {node: float('inf') for node in self.graph}
        self.distances[self.start] = 0
        self.previous_nodes = {node: None for node in self.graph}
        visited = set()

        while len(visited) < len(self.graph):
            current_node = None
            current_min_distance = float('inf')
            for node in self.graph:
                if node not in visited and self.distances[node] < current_min_distance:
                    current_min_distance = self.distances[node]
                    current_node = node

            if current_node is None:
                break

            visited.add(current_node)

            for neighbor, weight in self.graph[current_node]:
                if neighbor not in visited:
                    new_distance = self.distances[current_node] + weight
                    if new_distance < self.distances[neighbor]:
                        self.distances[neighbor] = new_distance
                        self.previous_nodes[neighbor] = current_node

        if self.end:
            return self.get_path(), self.distances[self.end]
        return self.distances

    def get_path(self):
        if self.end not in self.distances or self.distances[self.end] == float('inf'):
            return None

        path = []
        current = self.end
        while current is not None:
            path.insert(0, current)
            current = self.previous_nodes[current]
        return path
