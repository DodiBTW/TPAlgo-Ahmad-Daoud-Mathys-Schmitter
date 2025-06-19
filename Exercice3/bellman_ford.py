class BellmanFord:
    def __init__(self, graph: dict):
        self.graph = graph

    def bellman_ford(self, start: str):
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0

        for _ in range(len(self.graph) - 1):
            for vertex in self.graph:
                for neighbor, weight in self.graph[vertex].items():
                    if distances[vertex] + weight < distances[neighbor]:
                        distances[neighbor] = distances[vertex] + weight
        for vertex in self.graph:
            for neighbor, weight in self.graph[vertex].items():
                if distances[vertex] + weight < distances[neighbor]:
                    raise ValueError("Le graphe contient un cycle de poids négatif.")

        return distances