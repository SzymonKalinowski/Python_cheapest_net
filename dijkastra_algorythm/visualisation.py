import pygame
import math
import time

class GraphVisualizer:
    def __init__(self, graph, energy_data, dijkstra_obj):
        pygame.init()
        self.graph = graph
        self.energy_data = dict(energy_data)
        self.dijkstra_obj = dijkstra_obj
        self.screen = pygame.display.set_mode((1000, 700))
        pygame.display.set_caption("Dijkstra Algorithm Animation")
        self.font = pygame.font.SysFont(None, 24)
        self.clock = pygame.time.Clock()
        self.positions = self.calculate_positions()
        self.visited = set()
        self.current = None
        self.distances = {}
        self.previous = {}
        self.path = []

    def calculate_positions(self):
        nodes = list(self.graph.keys())
        angle_step = 2 * math.pi / len(nodes)
        radius = 250
        center_x, center_y = 500, 300
        positions = {}
        for i, node in enumerate(nodes):
            angle = angle_step * i
            x = int(center_x + radius * math.cos(angle))
            y = int(center_y + radius * math.sin(angle))
            positions[node] = (x, y)
        return positions

    def draw_graph(self):
        self.screen.fill((255, 255, 255))

        for node in self.graph:
            for neighbor, weight in self.graph[node]:
                start = self.positions[node]
                end = self.positions[neighbor]
                color = (200, 200, 200)
                if node in self.path and neighbor in self.path:
                    i1 = self.path.index(node)
                    i2 = self.path.index(neighbor)
                    if abs(i1 - i2) == 1:
                        color = (255, 0, 0)
                elif node in self.visited and neighbor in self.visited:
                    color = (100, 200, 100)
                elif self.current in [node, neighbor]:
                    color = (255, 165, 0)
                pygame.draw.line(self.screen, color, start, end, 3)

                mid_x = (start[0] + end[0]) // 2
                mid_y = (start[1] + end[1]) // 2
                dist_text = self.font.render(str(weight), True, (0, 0, 0))
                self.screen.blit(dist_text, (mid_x, mid_y))

        for node, (x, y) in self.positions.items():
            if node == self.current:
                color = (255, 165, 0)
            elif node in self.visited:
                color = (100, 200, 100)
            else:
                color = (100, 100, 250)
            pygame.draw.circle(self.screen, color, (x, y), 20)
            name_text = self.font.render(node, True, (255, 255, 255))
            self.screen.blit(name_text, (x - 7, y - 10))

            energy = self.energy_data.get(node, 0)
            energy_text = self.font.render(f"{energy}", True, (0, 150, 0) if energy >= 0 else (200, 0, 0))
            self.screen.blit(energy_text, (x - 10, y + 25))

        pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(10, 600, 300, 90))
        pygame.draw.circle(self.screen, (255, 165, 0), (30, 630), 8)
        self.screen.blit(self.font.render("Obecnie przetwarzany", True, (0, 0, 0)), (45, 623))
        pygame.draw.circle(self.screen, (100, 200, 100), (30, 650), 8)
        self.screen.blit(self.font.render("Odwiedzone", True, (0, 0, 0)), (45, 643))
        pygame.draw.circle(self.screen, (255, 0, 0), (30, 670), 8)
        self.screen.blit(self.font.render("Najkrótsza ścieżka", True, (0, 0, 0)), (45, 663))

    def animate_dijkstra(self):
        graph = self.graph
        start = self.dijkstra_obj.start
        end = self.dijkstra_obj.end
        self.distances = {node: float('inf') for node in graph}
        self.distances[start] = 0
        self.previous = {node: None for node in graph}
        self.visited = set()

        while len(self.visited) < len(graph):
            self.current = None
            current_min = float('inf')
            for node in graph:
                if node not in self.visited and self.distances[node] < current_min:
                    self.current = node
                    current_min = self.distances[node]

            if self.current is None:
                break

            self.visited.add(self.current)
            self.draw_graph()
            pygame.display.flip()

            # *********************************
            # *********************************

            time.sleep(1.8) # Change speed of animation

            # *********************************
            # *********************************

            for neighbor, weight in graph[self.current]:
                if neighbor not in self.visited:
                    new_dist = self.distances[self.current] + weight
                    if new_dist < self.distances[neighbor]:
                        self.distances[neighbor] = new_dist
                        self.previous[neighbor] = self.current

        self.path = self.reconstruct_path(end)
        self.current = None
        self.draw_graph()
        pygame.display.flip()

    def reconstruct_path(self, end):
        path = []
        current = end
        while current is not None:
            path.insert(0, current)
            current = self.previous[current]
        return path

    def run(self):
        self.animate_dijkstra()
        running = True
        while running:
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.draw_graph()
            pygame.display.flip()

        pygame.quit()
