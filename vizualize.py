import pygame
import math

class PygameVisualizer:
    def __init__(self, graph, mst, power_flow, width=800, height=600):
        self.graph = graph
        self.mst = set(tuple(e) for e in mst)
        self.power_flow = power_flow
        self.width = width
        self.height = height
        self.node_positions = {}
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Wizualizacja sieci energetycznej")
        self.clock = pygame.time.Clock()
        self._compute_positions()

    def _compute_positions(self):
        n = len(self.graph)
        center_x, center_y = self.width // 2, self.height // 2
        radius = min(center_x, center_y) - 50
        cities = list(self.graph.keys())
        for i, city in enumerate(cities):
            angle = 2 * math.pi * i / n
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)
            self.node_positions[city] = (int(x), int(y))

    def _draw_edges(self):
        for u, neighbors in self.graph.items():
            for v, cost in neighbors:
                p1 = self.node_positions[u]
                p2 = self.node_positions[v]
                color = (200, 200, 200)
                width = 1
                if (u, v) in self.mst or (v, u) in self.mst:
                    color = (50, 50, 255)
                    width = 3
                pygame.draw.line(self.screen, color, p1, p2, width)
                mx, my = (p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2
                font = pygame.font.SysFont(None, 20)
                text = font.render(str(cost), True, (0, 0, 0))
                self.screen.blit(text, (mx, my))

    def _draw_nodes(self):
        for city, pos in self.node_positions.items():
            pygame.draw.circle(self.screen, (255, 100, 100), pos, 15)
            font = pygame.font.SysFont(None, 20)
            text = font.render(city, True, (0, 0, 0))
            self.screen.blit(text, (pos[0] + 18, pos[1] - 10))

    def _draw_flows(self):
        max_flow = max(self.power_flow.values()) if self.power_flow else 1
        for (u, v), flow in self.power_flow.items():
            p1 = self.node_positions[u]
            p2 = self.node_positions[v]
            width = max(1, int(5 * flow / max_flow))
            pygame.draw.line(self.screen, (255, 0, 0), p1, p2, width)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.fill((255, 255, 255))
            self._draw_edges()
            self._draw_flows()
            self._draw_nodes()
            pygame.display.flip()
            self.clock.tick(30)
        pygame.quit()
