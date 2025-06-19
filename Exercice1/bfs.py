class BFS :
    def __init__(self, graph):
        self.graph = graph
    def bfs(self, start, visited=None):
        """
            ATTENTIONNN : LA VARIABLE ORDER A  ÉTÉ AJOUTÉE CAR LA STRUCTURE DE DONNÉES SET NE PRESERVE PAS L'ORDRE D'INSERTION.
        """
        if visited is None:
            visited = set()
        queue = [start]
        visited.add(start)
        order = [start]
        while queue:
            current = queue.pop(0)
            for neighbor in self.graph.get(current, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    order.append(neighbor)
        return order