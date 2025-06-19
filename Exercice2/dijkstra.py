import heapq

class Dijkstra:

    def __init__(self, graph):
        self.graph = graph

    def dijkstra(self, start):
        queue = []
        heapq.heappush(queue, (0, start))
        distances = {vertex: float('inf') for vertex in self.graph}
        distances[start] = 0

        while queue:
            current_distance, current_vertex = heapq.heappop(queue)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.graph[current_vertex].items():
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(queue, (distance, neighbor))

        return distances