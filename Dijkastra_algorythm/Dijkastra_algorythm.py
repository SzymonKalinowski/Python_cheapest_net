from dataclasses import dataclass

@dataclass
class Dijkstra:
    graph: dict
    start: str
    end: str = None

    def Dijkastra_algorythm(self):
        current_node = self.start
        all_c = []
        distances: int
        if self.start not in self.graph.keys():
            raise ValueError("Start node is not in graph")
        else:
            for i in self.graph.keys():
                if self.start == i:
                    current_node = i
                    distances = 0
                    all_c = [current_node]
                    self.graph[current_node][current_node] = 0
                    while current_node != self.end:
                        min_dist = float("inf")
                        for node in self.graph.keys():
                            if self.graph[current_node][node] < min_dist and node not in all_c:
                                min_dist = self.graph[current_node][node]
                                next_node = node
                        all_c.append(next_node)
                        current_node = next_node

