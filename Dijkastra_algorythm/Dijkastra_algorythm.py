from dataclasses import dataclass

@dataclass
class Dijkstra:
    graph: dict
    start: str
    end: str = None

    def Dijkastra_algorythm(self):
        distances: int
        if self.start not in self.graph.keys():
            raise ValueError("Start node is not in graph")
        else:
            for i in self.graph.keys():
                if self.start == i:
                    distances = 0
                    for connections in self.graph[i]:
                        continue