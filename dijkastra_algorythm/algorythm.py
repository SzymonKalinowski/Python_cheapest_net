from dataclasses import dataclass, field


def graph_to_edges(graph):
    edges = set()
    for city in graph:
        for neighbor, cost in graph[city]:
            edge = tuple(sorted((city, neighbor)) + [cost])
            edges.add(edge)
    return list(edges)


@dataclass
class UnionFind:
    parent: dict = field(default_factory=dict)

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        if root1 == root2:
            return False
        self.parent[root2] = root1
        return True


@dataclass
class Kruskal:
    cities: list
    edges: list

    def kruskal(self):
        uf = UnionFind()
        uf.parent = {node: node for node in self.cities}

        mst = []

        sorted_edges = sorted(self.edges, key=lambda x: x[2])

        for city1, city2, cost in sorted_edges:
            if uf.union(city1, city2):
                mst.append((city1, city2, cost))

        return mst