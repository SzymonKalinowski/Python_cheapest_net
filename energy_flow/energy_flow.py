from collections import defaultdict, deque


def build_adjacency_from_mst(mst):
    graph = defaultdict(list)
    for a, b, cost in mst:
        graph[a].append((b, cost))
        graph[b].append((a, cost))
    return graph


def find_path(graph, start, end):
    visited = set()
    parent = {start: None}
    queue = deque([start])
    visited.add(start)

    while queue:
        current = queue.popleft()
        if current == end:
            break
        for neighbor, _ in graph[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)

    if end not in parent:
        raise ValueError(f"No path {start} to {end}")

    path = []
    node = end
    while parent[node] is not None:
        path.append((min(node, parent[node]), max(node, parent[node])))
        node = parent[node]
    return path[::-1]



def assign_power_flow(mst, cities_with, cities_without):
    mst_graph = build_adjacency_from_mst(mst)
    power_on_edge = defaultdict(float)

    producers = [(city, amount) for city, amount in cities_with]
    consumers = [(city, -amount) for city, amount in cities_without]

    for consumer_city, demand in consumers:
        while demand > 0 and producers:
            for i, (producer_city, supply) in enumerate(producers):
                if supply <= 0:
                    continue

                transfer = min(demand, supply)


                path = find_path(mst_graph, producer_city, consumer_city)
                for edge in path:
                    power_on_edge[edge] += transfer

                producers[i] = (producer_city, supply - transfer)
                demand -= transfer
                if demand <= 0:
                    break

    return power_on_edge


def calculate_total_cost(mst, power_on_edge):
    total_cost = 0.0
    for a, b, dist in mst:
        edge = (min(a, b), max(a, b))
        power = power_on_edge.get(edge, 0.0)
        total_cost += dist * power
    return total_cost
